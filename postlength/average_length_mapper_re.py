#!/usr/bin/python

# In this case, a regular expression is used 
# to avoid irrelevant characters in the body field


import sys
import csv
import re

reader = csv.reader(sys.stdin, delimiter='\t')

for line in reader:
   try:
        body = line[4]
        wordList = re.split(r"[\,\n\s\"\.\t\?\!<>[\]()$\/=\-\\\';]", body)
	if line[0].strip() != 'id' and line[5].strip() != 'comment':
		bodyLength = len(wordList)
		if line[5].strip() == 'question':
			print line[0].strip() , "\t" , line[5].strip() , "\t" , bodyLength 
		else:
			print line[7].strip() , "\t" , line[5].strip() , "\t" , bodyLength 

   except:
	pass

