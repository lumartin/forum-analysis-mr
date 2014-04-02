#!/usr/bin/python

import sys

oldKey = None
questionLength = 0
count = 0
totalLength = 0


for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	node, type, length = data_mapped
	if oldKey and node != oldKey:
		if count > 0:
			mean = totalLength/count
		else: 
			mean = 0
		print oldKey , "\t" , questionLength , "\t" , mean
		questionLength = 0
		count = 0
		totalLength = 0

	oldKey = node
    	if type.strip() == 'answer':
		count += 1
		totalLength += float(length)
	else:
		questionLength = int(length)


if oldKey != None:
	if count > 0:
		mean = totalLength/count
	else:
		mean = 0
	print oldKey , "\t" , questionLength , "\t" , mean



