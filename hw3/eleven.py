# THIS CODE WAS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
# SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR.  Catherine W Baker

import sympy

# Count number of points on the elliptic curve y^2 = x^3 + ax + b over GF(103)
def countPoints(a, b):
    count = 1  # Start with 1 to account for infinity point
    for x in range(103):
        ySquared = ((x**3) + (a * x) + b) % 103 # Sub the value into y^2 equation 
        # Try all possible y values to see if y^2 = ySquared
        for y in range(103):
            if (y * y) % 103 == ySquared:
                count += 1
    return count


primeOrders = []

# Iterate over all possible a and b for y^2 equation
for a in range(103):
    for b in range(103):
        order = countPoints(a, b) # count # of points = order
        if sympy.isprime(order): # if the order is prime
            primeOrders.append((order, a, b)) # then append it to our list and log the a and b values

# Sort results to find the largest prime orders
primeOrders.sort(reverse=True, key=lambda x: x[0])

# Output the top 10 results
for order in primeOrders[:10]:
    print(f"Curve y^2 = x^3 + {order[1]}x + {order[2]}, Order: {order[0]}")