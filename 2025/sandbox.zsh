#!/usr/bin/env zsh
set -euo pipefail

typeset -i dial=50
typeset -i step=0
step=-52
dial=$((( $dial + $step + 100) % 100))
step=8
dial=$((( $dial + $step + 100) % 100))
print "dial=$dial"

zero_dial_counter=0

main() {
  print "zero_dial_counter=$zero_dial_counter"
}

main "$@"
