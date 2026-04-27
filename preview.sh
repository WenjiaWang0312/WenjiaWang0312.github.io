#!/usr/bin/env bash
set -euo pipefail

HOST="${1:-localhost}"
REQUESTED_PORT="${2:-4000}"
DEFAULT_LIVERELOAD_PORT="${LIVERELOAD_PORT:-35729}"

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

is_port_available() {
  local port="$1"

  ruby -rsocket -e '
    port = Integer(ARGV[0])
    begin
      server4 = TCPServer.new("127.0.0.1", port)
      server4.close
    rescue Errno::EADDRINUSE, Errno::EACCES
      exit 1
    end

    begin
      server6 = TCPServer.new("::1", port)
      server6.close
    rescue Errno::EADDRINUSE, Errno::EACCES
      exit 1
    end

    exit 0
  ' "$port"
}

find_available_port() {
  local port="$1"
  local attempts=20

  while (( attempts > 0 )); do
    if is_port_available "$port"; then
      echo "$port"
      return 0
    fi
    port=$((port + 1))
    attempts=$((attempts - 1))
  done

  return 1
}

# Initialize rbenv if available so we use the project Ruby version
if command -v rbenv >/dev/null 2>&1; then
  eval "$(rbenv init - bash)"
elif [[ -d "$HOME/.rbenv/bin" ]]; then
  export PATH="$HOME/.rbenv/bin:$PATH"
  eval "$(rbenv init - bash)"
fi

cd "$(dirname "$0")"
echo "Working directory: $(pwd)"

BUNDLE_CMD="$(find_bundle_cmd)" || {
  echo "Error: bundler is not installed."
  echo "Run: bash scripts/install_local_deps.sh"
  exit 1
}

"$BUNDLE_CMD" config set --local path 'vendor/bundle' >/dev/null

if "$BUNDLE_CMD" check >/dev/null 2>&1; then
  echo "Ruby gems already installed."
else
  echo "Installing Ruby gems into vendor/bundle ..."
  echo "This can take a while on the first run."
  "$BUNDLE_CMD" install
fi

echo "Starting Jekyll..."

PORT="$(find_available_port "$REQUESTED_PORT")" || {
  echo "Error: no free site port found near ${REQUESTED_PORT}."
  exit 1
}

if [[ "$PORT" != "$REQUESTED_PORT" ]]; then
  echo "Port ${REQUESTED_PORT} is busy; using ${PORT} instead."
fi

URL="http://${HOST}:${PORT}"
echo "Preview URL: ${URL}"
echo "Open: ${URL}"

JEKYLL_ARGS=(-H "$HOST" -P "$PORT")
if LIVERELOAD_PORT_SELECTED="$(find_available_port "$DEFAULT_LIVERELOAD_PORT")"; then
  if [[ "$LIVERELOAD_PORT_SELECTED" != "$DEFAULT_LIVERELOAD_PORT" ]]; then
    echo "LiveReload port ${DEFAULT_LIVERELOAD_PORT} is busy; using ${LIVERELOAD_PORT_SELECTED} instead."
  fi
  JEKYLL_ARGS=(-l --livereload-port "$LIVERELOAD_PORT_SELECTED" "${JEKYLL_ARGS[@]}")
else
  echo "Warning: no free LiveReload port found; starting without LiveReload."
fi

exec "$BUNDLE_CMD" exec jekyll serve "${JEKYLL_ARGS[@]}"
