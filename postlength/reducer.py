#!/usr/bin/python

import sys

oldKey = None
pageList = list()
count = 0

for line in sys.stdin:
    data_mapped = line.strip().split("\t")

    word, node = data_mapped
    if oldKey and word.strip() != oldKey:
	print oldKey , "\t" , len(pageList) , "\t" , count , "\t", pageList
	pageList = list()
	count = 0

    oldKey = word.strip()
    pageList.append(node.strip())
    count += 1
    

if oldKey != None:
    print oldKey , "\t" , len(pageList) , "\t" , pageList



