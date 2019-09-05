import sys

with open('tmptextfile.txt') as infile, open(sys.argv[1], 'w') as outfile:
    for line in infile:
        if not line.strip(): continue  # skip the empty line
        outfile.write(line)  # non-empty line. Write it to output