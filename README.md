# Project-Euler-46

I am starting to learn Python. I have decided to do this by solving problems from the project euler (https://projecteuler.net/) list.

This is my solution to problem 46 https://projecteuler.net/problem=46. It's another brute force solution that works.

The algorithm is
- look at every odd number n = 2k+1 (smaller than 2*max+1 = 20001)
- if n is not prime, then list all the prime numbers smaller than n. Actually the list generated as a byproduct of the primality check. If there is a way to check rapidly check for primality (without generating the whole list), then the code can be sped up since the list is not required when n is prime.
- run through the list of primes numbers smaller than n (primes[1],primes[2],...) and check if x=sqrt((n-primes[i])/2) is integer. If it is, then stop and move on to the next value of n.
- If we reach the end of the list without finding an integer x, then we have solved the problen, break out of the outer loop.

The value of max = 10000 has to be big enough to find a solution. This wokrs here because this is an easy problem. The people at project Euler were nice. If the solultion was a bigger number, it would take much longer.

The function P(n) is made from an algorithm that I took online (at https://www.geeksforgeeks.org/python-program-to-print-all-prime-numbers-in-an-interval/). I did not take the time to understand it, but it works.

I have learned:
- that there is no built-in function to list primes in Python.
- to use a timer.
- to work with arrays. [-1] is the last element of the list and .append() does what it says.
