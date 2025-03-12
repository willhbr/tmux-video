#!/bin/sh

set -e

width="$(tput cols)"
height="$(tput lines)"

mkdir -p generated

python compile.py "$1" "$width" "$height"

./start.sh "$height"
