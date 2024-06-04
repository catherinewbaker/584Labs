# THIS CODE WAS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
# SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR.  Catherine W Baker

def isPrimitive(candidate, p):
    # for all 52 values
    for i in range(1, p-2):
        # candidate^i % p then we stop and have found the order
        if (pow(candidate, i, p) == 1):
            if( i == 52):
                return True
            else:
                return False
    # otherwise if weve cycled through 1-51 and didnt find the order then it must be 52
    return pow(candidate, p-1, p) == 1

# Check for primitive roots modulo 53
primes = 53
primitives = []
for a in range(2, primes):  # start at 2
    if isPrimitive(a, primes):
        primitives.append(a)

print("Primitive roots modulo 53:", primitives)