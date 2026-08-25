#!/usr/bin/env bash
set -euo pipefail
D="$(cd -- "$(dirname -- "${BASH_SOURCE[0]}")" && pwd)"
I="$HOME/.local/share/antigravity-sde-manager"
A="$HOME/.local/share/applications"
mkdir -p "$I" "$A"
cp -a "$D/src" "$I/"; cp -a "$D/scripts" "$I/"; cp "$D/VERSION" "$D/run.sh" "$I/"
chmod +x "$I/run.sh" "$I/src/main.py"
cat > "$A/antigravity-sde-manager.desktop" <<EOF
[Desktop Entry]
Name=Antigravity SDE Manager
Comment=Antigravity + Intel SDE
Exec=$I/run.sh
Terminal=false
Type=Application
Categories=Development;Utility;
StartupNotify=true
EOF
echo "Installed. Look for Antigravity SDE Manager without AES — Linux in the menu."
