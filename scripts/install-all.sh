#!/usr/bin/env bash
set -euo pipefail

SCRIPT_DIR="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
TOOLKIT_ROOT="$(cd "${SCRIPT_DIR}/.." && pwd)"

python3 "${TOOLKIT_ROOT}/scripts/install-all.py" --toolkit-root "${TOOLKIT_ROOT}" "$@"
