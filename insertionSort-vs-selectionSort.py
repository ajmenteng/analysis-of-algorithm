"""
A script to compare the runtime performance of sorting algorithm 
(i.e. Insertion Sort and Selection Sort)

Author: John Wesly (johncha@bu.edu)
"""

import random
import time

def insertion_sort(a):
	found=False
	for j in range(1,len(a)):
		i=j-1		
		while a[j]<a[i] and i>=0:
			i-=1
			smaller=a[j]
			found=True
		if found:
			for k in range(j,i+1,-1):
				a[k]=a[k-1]
			a[k-1]=smaller	

def selection_sort(a):
	for i in range(0,len(a)):
		min_value=a[i]
		for j in range(i+1,len(a)):
			if a[j]<min_value:
				min_value=a[j]
				min_position=j
		if min_value<a[i]:
			temp=a[min_position]
			a[min_position]=a[i]
			a[i]=temp

def random_array_init(s):
	r=[]
	for i in range(1,s):
		r.append(random.randint(1,s))
	return r

def best_array_init(s):
	r=[]
	for i in range(1,s):
		r.append(i)
	return r

def worst_array_init(s):
	r=[]
	for i in range(s,1,-1):
		r.append(i)
	return r

def sort_all(myArr):
	start=time.time()
	insertion_sort(myArr)
	runtime=time.time()-start
	print("Insertion: %s sec" % runtime)
	start=time.time()
	selection_sort(myArr)
	runtime=time.time()-start
	print("Selection: %s sec" % runtime)


#=============================================
#BEST CASE
#=============================================
print("")
print("=====================================")
print("BEST CASE")
print("=====================================")
bestArr=best_array_init(100000)
print("Best Small Case")
sort_all(bestArr)
#=============================================

bestArr=best_array_init(200000)
print("Best Average Case")
sort_all(bestArr)
#=============================================

bestArr=best_array_init(300000)
print("Best Large Case")
sort_all(bestArr)
#=============================================

#=============================================
#RANDOM CASE
#=============================================
print("")
print("=====================================")
print("RANDOM CASE")
print("=====================================")
randomArr=random_array_init(100000)
print("Random Small Case")
sort_all(randomArr)
#=============================================

randomArr=random_array_init(200000)
print("Random Average Case")
sort_all(randomArr)
#=============================================

randomArr=random_array_init(300000)
print("Random Large Case")
sort_all(randomArr)
#=============================================

#=============================================
#WORST CASE
#=============================================
print("")
print("=====================================")
print("WORST CASE")
print("=====================================")
worstArr=worst_array_init(100000)
print("Worst Small Case")
sort_all(worstArr)
#=============================================

worstArr=worst_array_init(200000)
print("Worst Average Case")
sort_all(worstArr)
#=============================================

worstArr=worst_array_init(300000)
print("Worst Large Case")
sort_all(worstArr)
#=============================================