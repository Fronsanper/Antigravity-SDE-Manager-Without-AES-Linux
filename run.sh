#!/usr/bin/env bash
set -u
D="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
exec python3 "$D/src/main.py" "$@"
