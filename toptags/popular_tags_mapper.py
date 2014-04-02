#!/usr/bin/python

# This mapper just outputs all tags in the dataset
# with repetitions

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter=',', quotechar='"')

for line in reader:

	tags = line[2].strip().split()
	for tag in tags:
		print tag
