#!/usr/bin/python

import sys

hitsTotal = 0
topSite = None
topHits = 0
oldKey = None


for line in sys.stdin:
    thisKey = line.strip().split()

	hitsTotal += 1
	if hitsTotal > topHits:
	   topHits = hitsTotal
           topSite = oldKey
        oldKey = thisKey;
        hitsTotal = 0
    
    oldKey = thisKey
    hitsTotal += 1 

print topSite, "\t", topHits

