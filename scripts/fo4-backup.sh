#!/bin/zsh
# Backups (APFS clones) and Steam update lock for Fallout 4 run through Not Proton.
set -euo pipefail

STEAMAPPS="$HOME/Library/Application Support/Steam/steamapps"
GAME="$STEAMAPPS/common/Fallout 4"
MANIFEST="$STEAMAPPS/appmanifest_377160.acf"
MO2="${FO4_MO2:-$HOME/Games/MO2}"
DEST="${FO4_BACKUP:-$HOME/FO4-Backups}"
STAMP=$(date +%Y-%m-%d_%H%M)

mkdir -p "$DEST"

case "${1:-}" in
  game)
    cp -cR "$GAME" "$DEST/game_$STAMP"
    echo "Game cloned to $DEST/game_$STAMP"
    ;;
  mo2)
    cp -cR "$MO2" "$DEST/mo2_$STAMP"
    echo "MO2 instance cloned to $DEST/mo2_$STAMP"
    ;;
  profile)
    PROFILE="${2:?Usage: fo4-backup.sh profile <MO2 profile name>}"
    cp -cR "$MO2/profiles/$PROFILE" "$DEST/profile_${PROFILE}_$STAMP"
    echo "Profile $PROFILE cloned to $DEST/profile_${PROFILE}_$STAMP"
    ;;
  lock)
    chflags uchg "$MANIFEST"
    echo "Steam updates locked"
    ;;
  unlock)
    chflags nouchg "$MANIFEST"
    echo "Steam updates unlocked"
    ;;
  *)
    echo "Usage: fo4-backup.sh game | mo2 | profile <name> | lock | unlock"
    exit 1
    ;;
esac
