#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter=',', quotechar='"')

for line in reader:

	tags = line[2].strip().split()
	for tag in tags:
		print tag
