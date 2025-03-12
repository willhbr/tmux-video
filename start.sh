#!/bin/sh

set -e

remaining="$1"
next=$(( $remaining - 1 ))

if [ "$remaining" -le 0 ]; then
  read
  exit
fi

TMUX= exec tmux -f tmux.conf new-session "./start.sh '$next'"
