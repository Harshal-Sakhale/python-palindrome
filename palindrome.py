'''
PALINDROME

N=length of string
K=unique chars in the string

eg. 
['abba' (N=4, K=2)]
['kayak' (N=5, K=3)]

'''
import random
import math

def getpal(N,K):
	pd=""
	charset=set()
	charstr=""
	
	while(len(charset) != K):
		rn=random.randint(ord('a'),ord('z'))
		charset.add("%c" % rn)	

	print("charset=",charset)

	for i in range(len(charset)):
		charstr += charset.pop()

	print("charstr=",charstr)

	hN=math.ceil(N/2)
	
	print("hN="+str(hN))

	pd = charstr
	while(len(pd) < hN):
		rn=random.randint(0,len(charstr)-1)
		pd += charstr[rn]

	if N%2 == 1: # Odd
		pd += pd[::-1][1:]
	else:	#even
		pd += pd[::-1]

	print("pd="+pd)
	return pd


print(getpal(2,2))

