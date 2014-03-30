#!/usr/bin/python

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter=',', quotechar='"')

for line in reader:

	body = line[4]
        if (len(body) > 0):
	  if (body.count('.') + body.count('!') + body.count('?') < 2) \
            & ((body[len(body)-1] == '.') \
            | (body[len(body)-1] == '!') \
            | (body[len(body)-1] == '?')) \
            | (body.count('.') + body.count('!') + body.count('?') < 1):
	        print line[0] , "\t" , line[4]
