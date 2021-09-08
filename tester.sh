#!/usr/bin/env bash

# change to ../
file=push_swap

if [[ ! -f $file ]]
then
    make -C ../
    file=../push_swap
fi

# for different 
ARGS=$(python3 args.py)
sol=$(./$file)
echo "$sol" | python3 test.py $ARGS
