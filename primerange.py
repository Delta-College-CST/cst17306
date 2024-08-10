# This program counts the number of prime numbers in a given range
# set by constant variables

LOWER = 2000  # Lower boundary of range
UPPER = 3000  # Upper boundary of range

count  = 0      # Will increment when a prime is detected

for number in range(LOWER,UPPER+1):

    # Check if number is prime
    isPrime = True
    endTestValue = number//2+1
    
    for testNumber in range(2, endTestValue):
        if number % testNumber == 0:
            isPrime = False

    # If prime, increment prime count and write number
    if isPrime == True:
        count = count + 1

print("Primes in range:", count)

