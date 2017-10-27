#!/bin/bash

for i in *.mid; do
    [ -f "$i" ] || break
    filename=$(basename "$i")
	filename="${filename%.*}"
	extension=".xml"
    mscore "$i" -o "$filename$extension"
done
