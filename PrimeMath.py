import math

##
#isPrime
#Description: Check if a given number is prime.
#
#Parameters:
#   n - The number to check.  Must be > 1.
#
#Return: True if the number if prime.  False otherwise.
##
def isPrime(n):
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True