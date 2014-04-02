#!/usr/bin/python

# This reducer counts the number of times
# each tag appears in the input, makes a list
# and order it building a ranking. Then outputs
# the first ten tags. 

import sys

oldKey = None
hits = 0
tagFreqList = []

for line in sys.stdin:
	thisKey = line.strip().split()

	if oldKey and oldKey != thisKey:
		tagFreqList.append([oldKey, hits])
		hits = 0
	
	oldKey = thisKey
	hits += 1

if oldKey != None:
	tagFreqList.append([oldKey, hits])

tagFreqList.sort(key=lambda tup: tup[1])
top10 = tagFreqList[len(tagFreqList)-10 : len(tagFreqList)]

for tuple in reversed(top10):
	print tuple




