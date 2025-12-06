#!/usr/bin/env zsh
set -euo pipefail

typeset -i dial=50
typeset -i step=0
input="input.txt"
typeset -i zeroCounter=0

parseLine() {
	local instr=$1
	local dir=${instr[1]}
	local -i num=${instr[2,-1]}

	case $dir in
		L) signed=$(( - num )) ;;
		R) signed=$((    num )) ;;
		*) print -u2 "bad dir: $dir"; return 1 ;;
	esac
	step=$signed
}

readInput() {
	while read line; do
		# print $line
		parseLine $line
		twistDial
		if (( dial == 0 )); then
			(( zeroCounter += 1 ))
			# print $zeroCounter
		fi
	done < $input
}

twistDial() {
	dial=$((( $dial + $step + 100) % 100))
}

main() {
	readInput
	print "Zero Dial Counter = $zeroCounter"
}

main "$@"
