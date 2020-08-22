# spatialAnalysisArray.py
# Temporal and Spatial analysis on a 10,000 element array displaying 10 most occurences and frequencies with time and memory usage.
# NCU.edu
# School of Business & Technology Managment
# TIM-6110
# Author: Ravi Jethva
# Date: August 23, 2020

# import necessary packages
from collections import Counter
from time import process_time
import random
import sys
from sys import getsizeof

# start time
t1_start = process_time()

# create array with 100,000 random elements between 1 & 10,000
def Rand(start, end, num): 
	res = [] 
	for j in range(num): 
		res.append(random.randint(start, end)) 
	return res
	
num = 10000000
start = 1
end = 10000

# determine most frequent integers occurring
def most_frequent(res):
    occurence_count = Counter(res)
    return occurence_count.most_common(10)

# display most frequent random integers
print(most_frequent(Rand(start, end, num)))
# end time
t1_stop = process_time();

# display temporal and spatial analysis
print("Elapsed time: ", t1_stop - t1_start)
print("="*10, "Memory Information", "="*10)
print(str(sys.getsizeof(Rand(start, end, num))) + " bytes used." )