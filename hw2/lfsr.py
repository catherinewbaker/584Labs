# THIS CODE WAS MY OWN WORK, IT WAS WRITTEN WITHOUT CONSULTING ANY
# SOURCES OUTSIDE OF THOSE APPROVED BY THE INSTRUCTOR.  Catherine W Baker

# n = number of bits in the register
# seed = initial seed (a binary string) that initializes the register
# tap = the tap position, indicating which bit is used for feedback
def lfsr(n, seed, tap):
    seedList = list(seed) # Convert seed to list for easier manipulation

    while 1:
        # Calculate the feedback bit (XOR of the last bit and the tap position bit)
        feedback = int(seedList[-1]) ^ int(seedList[tap-1])  # assuming tap is 1-4 so subtract 1 for index

        # Shift all bits to the right
        for i in range(n - 1, 0, -1):
            seedList[i] = seedList[i-1]

        seedList[0] = str(feedback) # Insert the feedback bit at the start (as string)

        yield seedList[-1]  # Output the last bit one at a time to show the pseuo-random generated numbers

# To test the function edit these parameters
n = 4  # Number of bits in the LFSR
seed = "1001" # Initial seed
tap = 3  # Tap position based on 1-4 scale

# Create an LFSR generator
lfsrGenerator = lfsr(n, seed, tap)

# Generate the first 10 pseudo-random bits - if you want more than 10 bits then change the range(10)
for i in range(10):
    print(next(lfsrGenerator)) # next() moves through the values in the given range to the yield operator
