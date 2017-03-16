"""

EDF
Test cases:
3           
1 8
2 5
4 10

"""
from heapq import heappush,heappop
from fractions import gcd
l={}
count={}
n=0
hp=-1
heap=[]
def lcm(a,b):
	return (a*b)/gcd(a,b)
def necessary_test():
	util=0
	for i in l:
		util+=float(l[i][0])/l[i][1]
	if util<=1:
		return 1
	return 0
"""
Input
"""
n=input()
fl=1
for i in xrange(n):
	l[i]=map(int,raw_input().split())
	if fl:	
		hp=l[i][1]
	else:
		hp=lcm(hp,l[i][1])
	fl=0
for i in l:
	s=l[i][1]
	heappush(heap,(s,l[i][0],i+1))
if not necessary_test():
	print "Not Schedulable"
else:
	ti=prev=0
	while ti<=hp:
		if heap:
			curr=heappop(heap)
			print ti,"to",ti+curr[1],"P"+str(curr[2])
			prev=ti
			ti+=curr[1]
			for i in l:
				for j in xrange(prev+1,ti+1):
					if j%l[i][1]==0:				
						heappush(heap,(j+l[i][1],l[i][0],i+1))
		else:
			print prev,"to",ti,"Empty"
			prev=ti
			ti+=1
			for i in l:
				for j in xrange(prev+1,ti+1):
					if j%l[i][1]==0:				
						heappush(heap,(j+l[i][1],l[i][0],i+1))




