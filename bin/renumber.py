#!/usr/bin/python3

from argparse import ArgumentParser
import re


parser = ArgumentParser(description='Renumber ABC file.')

parser.add_argument('-n', '--number', type=int, help='Set the starting number')
parser.add_argument('input_file', help='Input file')
parser.add_argument('output_file', nargs='?', help='Output file')
args = parser.parse_args()

with open (args.input_file, 'r') as infile:
    lines = infile.readlines()
infile.close()

xnum = args.number if args.number else 1

for i in range(len(lines)):
    if re.match('X:\s*\d+\s*$', lines[i]):
    	lines[i] = 'X:%d\n' % xnum
    	xnum += 1

outfile_name = args.output_file if args.output_file else args.input_file

outfile = open(outfile_name, 'w')

outfile.writelines(lines)
outfile.close()