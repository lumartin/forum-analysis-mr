#!/usr/bin/python

import sys
import csv
import re
from datetime import datetime

reader = csv.reader(sys.stdin, delimiter='\t')
writer = csv.writer(sys.stdout, delimiter='\t', quotechar='"', quoting=csv.QUOTE_ALL)

for line in reader:
	if (len(line)) == 19 and line[0] != "id" :
		id,title, tagnames, author_id, body, node_type, parent_id, \
		abs_parent_id, added_at, score, state_string, last_edited_id, \
		last_activity_by_id, last_activity_at, active_revision_id, extra, \
		extra_ref_id, extra_count, marked = line
	
		print author_id , "\t" , datetime.strptime(added_at, "%Y-%m-%d %H:%M:%S.%f+00").hour
	else:
		pass


