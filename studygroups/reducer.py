#!/usr/bin/python

import sys

oldKey = None
contributorsList = []

for line in sys.stdin:
	data_mapped = line.strip().split("\t")
	node, author = data_mapped
	if oldKey and node != oldKey:
		print oldKey , "\t" , contributorsList
		contributorsList = []

	oldKey = node
	contributorsList.append(author)

if oldKey != None:
	print oldKey , "\t" , contributorsList 



