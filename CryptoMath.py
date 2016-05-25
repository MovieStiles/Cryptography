import math


def isPrime(n):
    """Check if a given number is prime.

    Args:
        n - The number to check.  Must be > 1.

    Returns:
        True if the number is prime.  False otherwise.
    """
    if n % 2 == 0 and n > 2:
        return False
    for i in range(3, int(math.sqrt(n)) + 1, 2):
        if n % i == 0:
            return False
    return True


##########################################
#   Finding the Multiplicative Inverse   #

# Straight from https://en.wikibooks.org/wiki/Algorithm_Implementation/Mathematics/Extended_Euclidean_algorithm
def egcd(a, b):
    """Recursive implementation of the Extended Euclidean Algorithm to find the gcd of two numbers.

    Args:
        a - The first of two numbers to find the gcd of.
        b - The second of the two numbers.

    Returns:
        (g, x, y) such that ax + by = g = gcd(a, b)
    """
    if a == 0:
        return b, 0, 1
    else:
        g, y, x = egcd(b % a, a)
        return g, x - (b // a) * y, y


def modinv(a, m):
    """Find the multiplicative inverse of a number under a certain field

    Args:
        a - The number to find the multiplicative inverse of
        m - The modulo of the field

    Returns:
        The multiplicative inverse of a if it exists
    """
    g, x, y = egcd(a, m)
    if g != 1:
        return None  # modular inverse does not exist
    else:
        return x % m

#   Finding the Multiplicative Inverse   #
##########################################
