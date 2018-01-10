

def gcd(n,m):
    """ input: two integers, n and m
        output: the greatest common divisor between n and m
        uses Euclid's algorithm, a recursive algorithm
    """
    print "gcd(",n,m,")="
    if n==0:
        return m
    elif m==0:
        return n
    else:
        print "gcd(",m,n%n,")"
        return gcd(m,n%m)

def relativePrimes(n,m):
    """ returns true if n is relatively prime to m
        returns false otherwise
    """
    return gcd(n,m)==1