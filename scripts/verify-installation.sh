#!/usr/bin/env bash
set -euo pipefail

echo "=== Verifying ai-coding-toolkit installation ==="

for agent in kimi codex claude; do
    dir="${HOME}/.${agent}/skills"
    if [ -d "$dir" ]; then
        count=$(find "$dir" -maxdepth 2 -name "SKILL.md" | wc -l)
        echo "✓ ${agent}: ${count} skills found in ${dir}"
    else
        echo "✗ ${agent}: ${dir} not found"
    fi
done

echo ""
echo "Checking common CLI tools:"
for tool in git gh node npm pnpm python3; do
    if command -v "$tool" &> /dev/null; then
        echo "✓ ${tool}: $(command -v "$tool")"
    else
        echo "✗ ${tool}: not found"
    fi
done

echo ""
echo "Checking optional security/quality tools:"
for tool in semgrep trivy; do
    if command -v "$tool" &> /dev/null; then
        echo "✓ ${tool}: $(command -v "$tool")"
    else
        echo "○ ${tool}: not found (optional)"
    fi
done
