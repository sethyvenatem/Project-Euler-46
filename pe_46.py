import math
#This provides acces to sqrt
import time
start_time = time.time()

def P(n):
# This function makes a list of prime numbers smaller than n. I modified an algorithm taken from https://www.geeksforgeeks.org/python-program-to-print-all-prime-numbers-in-an-interval/
	pr = [1]
	for i in range(1, n):
		if i > 1:
			for j in range(2, i):
				if (i % j == 0):
					break
			else:
				pr.append(i)
#				print(i)
	return pr

max = 10000
for k in range(1,max,1):
	n=2*k+1
	primes = P(n)
	if n!= P(n+1)[-1]:
		for i in primes:
			if (math.sqrt((n-i)/2).is_integer() and math.sqrt((n-i)/2)>10**(-12)):
				break
				#Stop the inner loop immediately when there is an x. This saves time.
		if i==primes[-1]:
			break
if k<max:
	print(2*k+1)

print("--- %s seconds ---" % (time.time() - start_time)))
