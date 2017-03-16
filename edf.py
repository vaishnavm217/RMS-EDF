l=[]
n=0
def necessary_test():
  util=0
  for i in range(n):
    util+=float(l[i][0])/l[i][1]
  if util<=1:
    return 1
  return 0
n=input()
for i in range(n):
  l[i]=map(int,raw_input().split())
 
  
