#!/usr/bin/python

import sys
import csv


reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
   try:
        author = line[3]
	if line[0].strip() != 'id':
		if line[5].strip() == 'question':
			print line[0].strip() , "\t" , author 
		else:
			print line[7].strip() , "\t" , author 

   except:
	pass

