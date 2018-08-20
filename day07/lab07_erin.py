## Exercise 1
## Write a function using recursion to calculate the greatest common divisor of two numbers

## Helpful link:
## https://www.khanacademy.org/computing/computer-science/cryptography/modarithmetic/a/the-euclidean-algorithm
def gcd(x, y):
	## get remainder
	r = x%y
	## base case, no remainder
	## then that "divisor" is answer
	if r == 0:
		return y
	## otherwise, call function again with new inputs
	return gcd(y, r)

## Exercise 2
## Write a function using recursion that returns prime numbers less than 121
def find_primes(me = 121, primes = []):
    if me == 2:
    	primes.append(2)
        return primes

    for i in range(2, me):
    	if me % i == 0:
        	break
    else:
    	primes.append(me)
    return find_primes(me-1, primes)







 