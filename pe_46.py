import math
#This provides acces to sqrt
import time
start_time = time.time()

def P(n): # This function makes a list of prime numbers smaller than n. I modified an algorithm taken from https://www.geeksforgeeks.org/python-program-to-print-all-prime-numbers-in-an-interval/
	pr = [1]
	for i in range(1, n):
		if i > 1:
			for j in range(2, i):
				if (i % j == 0):
					break
			else:
				pr.append(i) #When we find a prime number, append it to the list.
	return pr

max = 10000 #Make this big enough.
for k in range(1,max,1):
	n=2*k+1
	primes = P(n+1) #Generate a list of primes smaller than n.
	if n!= primes[-1]: #This check that n is not prime before getting to work.
		for i in primes:
			if math.sqrt((n-i)/2).is_integer():
				break #Stop the inner loop immediately when there is an x. This saves time.
		if i==primes[-1]:
			break #If we reach the end of the list without finding an integer x, then we have solved the problem: Stop.
if k<max:
	print(2*k+1)

print("--- %s seconds ---" % (time.time() - start_time))
