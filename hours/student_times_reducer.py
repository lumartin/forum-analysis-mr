#!/usr/bin/python

# This reducer takes as input the sorted 
# author ids and hours for each post and
# outputs the most frequent hour for
# each user. It outputs ties as well 

import sys


# This function takes an array containing
# all hours for a single user and outputs
# the most frequent hours for this user
# (more than one only if there is a tie)
def frequentHours ( userHours ) :
	max = 0
	hoursTimes = dict({})
	for hour in userHours:
		if hoursTimes.has_key(hour):
			times = hoursTimes.get(hour)
			times = times + 1
			if times > max:
				max = times
			map = {hour : times}
			hoursTimes.update(map)
		else:
			map = {hour : 1}
			hoursTimes.update(map)
			if max == 0:
				max = 1
	mostFrequentHours = []
	for hour in hoursTimes:
		if hoursTimes.get(hour) == max:
			mostFrequentHours.append(hour)
	return mostFrequentHours		 
	
		
oldKey = None
currentUserHours = []

for line in sys.stdin:
	line = line.strip().split("\t")
	thisKey, hour = line
	if oldKey and oldKey != thisKey:
		for frequentHour in frequentHours(currentUserHours):
			print oldKey, "\t" , frequentHour
		currentUserHours = []
	oldKey = thisKey
	currentUserHours.append(hour)

if oldKey != None:
	for frequentHour in frequentHours(currentUserHours): 
		print oldKey, "\t" , frequentHour
