import math

def isPrime(n) :
 
    if (n < 2) :
        return False
    for i in range(2, n + 1) :
        if (i * i <= n and n % i == 0) :
            return False
    return True
def dirichletConvolution(f,g,n):
    """
    Returns the Dirichlet convolution of f and g.
    """
    arr = []
    result = []
    for i in range(1,n+1):
        if n%i == 0:
            arr.append(i)
    for d in arr:
        result.append((f(d)*g(n/d)))
    return sum(result)


def identity(n):
    """
    Returns the identity matrix of size n.
    """
    return n

def constant(n):
    """
    Returns the constant matrix of size n.
    """
    return 1

def multipIdentity(n):
    return math.floor(1/n)

def mobius(N):
    N = int(N)
    if (N == 1) :
        return 1

    p = 0
    for i in range(1, N + 1) :
        if (N % i == 0 and
                isPrime(i)) :

            if (N % (i * i) == 0) :
                return 0
            else :

                p = p + 1
 
    if(p % 2 != 0) :
        return -1
    else :
        return 1


def posMob(n):
    return math.fabs(mobius(n))

def omega(n):
    return int(math.log(dirichletConvolution(constant,posMob,n))/math.log(2))

def primeIndicator(n):
    return dirichletConvolution(omega,mobius,n)


def generate_primes(n):
    primes = []
    for possiblePrime in range(2, n + 1):
        isPrime = True
        for num in range(2, int(possiblePrime ** 0.5) + 1):
            if possiblePrime % num == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(possiblePrime)
    return primes



