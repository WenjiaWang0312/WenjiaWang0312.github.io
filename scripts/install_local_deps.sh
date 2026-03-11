#!/usr/bin/env bash
set -euo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$REPO_ROOT"

log() {
  echo "[setup] $*"
}

warn() {
  echo "[setup] Warning: $*" >&2
}

die() {
  echo "[setup] Error: $*" >&2
  exit 1
}

SUDO=""
if [[ "${EUID}" -ne 0 ]] && command -v sudo >/dev/null 2>&1; then
  SUDO="sudo"
fi

find_bundle_cmd() {
  if command -v bundle >/dev/null 2>&1; then
    echo "bundle"
  elif command -v bundle3.0 >/dev/null 2>&1; then
    echo "bundle3.0"
  elif command -v bundler3.0 >/dev/null 2>&1; then
    echo "bundler3.0"
  else
    return 1
  fi
}

append_to_shell_rc() {
  local gem_bin="$1"
  local shell_name
  local rc_file
  local export_line

  shell_name="$(basename "${SHELL:-bash}")"
  case "$shell_name" in
    zsh)
      rc_file="$HOME/.zshrc"
      ;;
    bash|*)
      rc_file="$HOME/.bashrc"
      ;;
  esac

  export_line="export PATH=\"$gem_bin:\$PATH\""
  touch "$rc_file"

  if ! grep -Fqx "$export_line" "$rc_file"; then
    {
      echo
      echo "# Added by scripts/install_local_deps.sh"
      echo "$export_line"
    } >> "$rc_file"
    log "Added Bundler path to $rc_file"
  fi
}

install_with_apt() {
  local packages=("$@")
  local update_ok=1

  [[ "${#packages[@]}" -gt 0 ]] || return 0
  [[ -n "$SUDO" || "${EUID}" -eq 0 ]] || die "Need sudo or root privileges to install system packages."

  log "Installing system packages with apt: ${packages[*]}"
  if ! $SUDO apt-get update; then
    update_ok=0
    warn "apt-get update failed. This is often caused by an unrelated third-party repository."
    warn "Retrying package installation with the existing apt cache."
  fi

  if ! $SUDO apt-get install -y "${packages[@]}"; then
    if [[ "$update_ok" -eq 0 ]]; then
      die "apt package installation failed after apt-get update was blocked by a broken repository. Fix or disable the failing apt source, then rerun this script."
    fi
    die "apt package installation failed."
  fi
}

install_with_dnf() {
  local packages=("$@")

  [[ "${#packages[@]}" -gt 0 ]] || return 0
  [[ -n "$SUDO" || "${EUID}" -eq 0 ]] || die "Need sudo or root privileges to install system packages."

  log "Installing system packages with dnf: ${packages[*]}"
  $SUDO dnf install -y "${packages[@]}"
}

install_with_brew() {
  local packages=("$@")

  [[ "${#packages[@]}" -gt 0 ]] || return 0
  command -v brew >/dev/null 2>&1 || die "Homebrew is required on macOS. Install it first: https://brew.sh/"

  log "Installing packages with Homebrew: ${packages[*]}"
  brew install "${packages[@]}"
}

install_system_dependencies() {
  local need_ruby="$1"
  local need_node="$2"

  if command -v apt-get >/dev/null 2>&1; then
    local packages=()
    if [[ "$need_ruby" == "1" ]]; then
      packages+=(ruby-full ruby-dev build-essential gcc make zlib1g-dev)
    fi
    if [[ "$need_node" == "1" ]]; then
      packages+=(nodejs npm)
    fi
    install_with_apt "${packages[@]}"
    return
  fi

  if command -v dnf >/dev/null 2>&1; then
    local packages=()
    if [[ "$need_ruby" == "1" ]]; then
      packages+=(ruby ruby-devel gcc gcc-c++ make redhat-rpm-config)
    fi
    if [[ "$need_node" == "1" ]]; then
      packages+=(nodejs npm)
    fi
    install_with_dnf "${packages[@]}"
    return
  fi

  if [[ "$(uname -s)" == "Darwin" ]]; then
    local packages=()
    if [[ "$need_ruby" == "1" ]]; then
      packages+=(ruby)
    fi
    if [[ "$need_node" == "1" ]]; then
      packages+=(node)
    fi
    install_with_brew "${packages[@]}"
    return
  fi

  die "Unsupported system package manager. Install Ruby, Bundler, Node.js, and npm manually."
}

ensure_bundler() {
  local bundler_cmd=""

  if bundler_cmd="$(find_bundle_cmd)"; then
    log "Bundler already installed: $($bundler_cmd -v)"
    return
  fi

  command -v gem >/dev/null 2>&1 || die "RubyGems is not available. Install Ruby first."

  log "Installing Bundler with RubyGems..."
  if ! gem install bundler --user-install; then
    if [[ -n "$SUDO" || "${EUID}" -eq 0 ]]; then
      $SUDO gem install bundler
    else
      die "Bundler installation failed and sudo is unavailable."
    fi
  fi

  local gem_bin
  gem_bin="$(ruby -r rubygems -e 'print File.join(Gem.user_dir, "bin")')"

  if [[ -d "$gem_bin" ]]; then
    export PATH="$gem_bin:$PATH"
    append_to_shell_rc "$gem_bin"
  fi

  bundler_cmd="$(find_bundle_cmd)" || die "Bundler was installed but is still not on PATH."
  log "Bundler ready: $($bundler_cmd -v)"
}

install_project_dependencies() {
  local bundler_cmd

  bundler_cmd="$(find_bundle_cmd)" || die "Bundler is not available."

  log "Installing Ruby gems into vendor/bundle..."
  "$bundler_cmd" config set --local path "vendor/bundle" >/dev/null
  "$bundler_cmd" install

  if [[ -f package.json ]]; then
    if command -v npm >/dev/null 2>&1; then
      log "Installing npm dependencies..."
      npm install
    else
      warn "package.json exists but npm is not installed."
    fi
  fi
}

need_ruby=0
need_node=0

if ! command -v ruby >/dev/null 2>&1 || ! command -v gem >/dev/null 2>&1; then
  need_ruby=1
fi

if ! command -v node >/dev/null 2>&1 || ! command -v npm >/dev/null 2>&1; then
  need_node=1
fi

if [[ "$need_ruby" == "1" || "$need_node" == "1" ]]; then
  install_system_dependencies "$need_ruby" "$need_node"
fi

ensure_bundler
install_project_dependencies

log "Setup complete."
log "Next step: ./preview.sh"
