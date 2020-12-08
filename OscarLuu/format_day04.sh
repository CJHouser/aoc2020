#!/usr/bin/bash


cat $1 | tr ' ' '\n' | while read line;
do
    echo -ne "\"$line\""
    sed -r 's/[^:]+/"&"/g'
done  | tr '^\n' '\},\{' \
| sed "s/^/[{/" \
| sed "s/,$/}]/" \
| sed -r "s/,,/},{/g" \
| sed -r "s/\"\"//g" > $2

# Run python script
py oscar_aocday4_p1.py $2


