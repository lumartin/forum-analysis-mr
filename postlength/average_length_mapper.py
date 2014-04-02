#!/usr/bin/python

# This mapper outputs, for each node
# with type question or answer, the fields
# original node id, type and length
# being length the string length of
# the body field

import sys
import csv

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
   try:
        bodyLength = len(line[4])
	if line[0].strip() != 'id' and line[5].strip() != 'comment':
		if line[5].strip() == 'question':
			print line[0].strip() , "\t" , line[5].strip() , "\t" , bodyLength  
		else:
			print line[7].strip() , "\t" , line[5].strip() , "\t" , bodyLength 

   except:
	pass

