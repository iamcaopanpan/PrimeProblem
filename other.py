def isPrime(x):
    i = 2
    while i**2<=x:
        if not x%i:
            return False
        i = i+1
    return True