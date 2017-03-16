from math import ceil
l=[(1,3),(1,5),(1,6),(3,10)]
#########################################
#				SUM						#
#########################################
def util_sum(l):
	sum=0.0
	for i in l:
		sum+=float(i[0])/float(i[1])
	return sum

#########################################
#			NECESSARY TEST				#
#########################################
def neccessary_test(l):
	if util_sum(l)<=1.0:
		return True
	else:
		return False

#########################################
#			SUFFICIENT TEST				#
#########################################
def sufficient_test(l,n):
	util_b=float(n)*(float(n**(-1))-1)
	if util_sum(l)<=util_b:
		return True
	else:
		return False

#########################################
#			PRECISE TEST				#
#########################################
def precise_test(l,n):
	flag=-1
	for i in xrange(1,n):
		x=[]
		if sufficient_test(l[:i+1],i+1)==False:
			sum=0.0
			for b in xrange(i+1):
				sum+=l[b][0]
			x.append(sum)
			if sum>l[i][1]:
				flag=i+1
				break
			a=sum
			while True:
				temp=l[i][0]
				for c in xrange(i):
					temp+=ceil(a/float(l[c][1]))*l[c][0]
				x.append(temp)
				if temp>l[i][1]:
					flag=i+1
					break
				a=temp
				if x[-1]==x[-2]:
					break
			if flag!=-1:
				return flag
n=4
print "Util_sum:",util_sum(l)
print "Neccessary test:",neccessary_test(l)
print "Suff test:",sufficient_test(l,n)
if precise_test(l,n)==-1:
	print "Precise test:",True
else:
	print "Precise test:",False,",Process:",precise_test(l,n)