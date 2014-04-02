#!/usr/bin/python

# This mapper reads each line in the source 
# and outputs the author id and the hour for each post

import sys
import csv
import re
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
	if (len(line)) == 19 and line[0] != "id" :
		added_at = line[8]
		author_id = line[3]
		print author_id , "\t" , datetime.strptime(added_at, "%Y-%m-%d %H:%M:%S.%f+00").hour
	else:
		pass


