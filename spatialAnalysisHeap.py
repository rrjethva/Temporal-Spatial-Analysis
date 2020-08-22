# spatialAnalysisHeap.py
# Temporal and Spatial analysis on a 10,000 element heap displaying occurences and frequencies with time and memory usage.
# NCU.edu
# School of Business & Technology Managment
# TIM-6110
# Author: Ravi Jethva
# Date: August 23, 2020

# import necessary packages
from collections import Counter
from time import process_time
import random
import heapq
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

# determine most frequent integers  occurring
def most_frequent(res):
    occurence_count = Counter(res)
    return occurence_count.most_common(10)

# convert array into heap data structure
heapq.heapify(Rand(start, end, num))

# display most frequent integers with occurences
print(most_frequent(Rand(start, end, num)))

# stop time
t1_stop = process_time();

# print elapsed time, memory usage, and heap structure
print("Elapsed time: ", t1_stop - t1_start)
print("="*10, "Memory Information", "="*10)
print(str(sys.getsizeof(Rand(start, end, num))) + " bytes used." )

# print("The created heap is : ", end="")
# print(Rand(start, end, num))