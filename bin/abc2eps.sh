#!/usr/bin/env bash

TUNEPATH=${1:-'tunes'}

for i in $(find $TUNEPATH -iname '*.abc'); 
  do abcm2ps -F ./format/format.fmt -E $i -O "${i%.abc}.eps"; 
done
