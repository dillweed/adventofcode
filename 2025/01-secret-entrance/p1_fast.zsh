#!/usr/bin/env zsh
set -euo pipefail

input=${1:-input.txt}
typeset -i dial=50 count=0 step num

while IFS= read -r line; do
  dir=${line[1]}
  num=${line[2,-1]}
  case $dir in
    L) step=-num ;;
    R) step=num ;;
    *) print -u2 "bad dir: $dir"; exit 1 ;;
  esac
  (( dial = (dial + step) % 100 ))
  (( dial += 100, dial %= 100 ))
  if (( dial == 0 )); then
    (( ++count ))
  fi
done < "$input" || true

print $count
