#!/usr/bin/env bash

TEXFILE=$1

latex "${TEXFILE%.*}.tex"
dvips "${TEXFILE%.*}.dvi"
ps2pdf "${TEXFILE%.*}.ps"

