l=[]
#########################################
#				SUM						#
#########################################
def util_sum():
	sum=0.0
	for i in l:
		sum+=float(i[0])/float(i[1])
	return sum

#########################################
#			NECESSARY TEST				#
#########################################
def neccessary_test():
	if util_sum()<=1.0:
		return True
	else:
		return False

#########################################
#			SUFFICIENT TEST				#
#########################################
def sufficient_test(int n):
	util_b=n*(float(2**n)-1)
	if util_sum()<=util_b:
		return True
	else:
		return False

#########################################
#			PRECISE TEST				#
#########################################
def precise_test(int n):
	x=[]
	flag=-1
	for i in xrange(1,n):
		sum=0.0
		for b in xrange(i+1):
			sum+=l[b][0]
		x.append(sum)
		if x[-1]==x[-2]:
			break
		if sum>l[i][1]:
			flag=i
			break
		else:
			temp=l[i][0]
			while temp<=l[i][1]:
				for c in xrange(i):
					temp+=ceil(temp/l[c][1])
				x.append(temp)
				if x[-1]==x[-2]:
					break
				if temp>l[i][1]:
					flag=i
					break
		if flag!=-1:
			break
	return flag

