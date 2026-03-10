#!/usr/bin/env bash
set -euo pipefail

HOST="${1:-localhost}"
PORT="${2:-4000}"
URL="http://${HOST}:${PORT}"

cd "$(dirname "$0")"

echo "Preview URL: ${URL}"

echo "Working directory: $(pwd)"

if ! command -v bundle >/dev/null 2>&1; then
  echo "Error: bundler is not installed."
  echo "Install Ruby/Bundler first, then run this script again."
  exit 1
fi

bundle config set --local path 'vendor/bundle' >/dev/null

if bundle check >/dev/null 2>&1; then
  echo "Ruby gems already installed."
else
  echo "Installing Ruby gems into vendor/bundle ..."
  echo "This can take a while on the first run."
  bundle install
fi

echo "Starting Jekyll..."
echo "Open: ${URL}"
exec bundle exec jekyll serve -l -H "$HOST" -P "$PORT"
