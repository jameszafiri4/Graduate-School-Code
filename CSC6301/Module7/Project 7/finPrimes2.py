'''
CSC 6301 Project 7
Finding Primes Analysis
James Zafiri
10/13/2023
Version 2.0.0
'''

import random
import cProfile

def guess():
    return random.randint(2, 5000)

def isPrime(x):
    if x <= 1:
        return False
    if x <= 3:
        return True
    if x % 2 == 0 or x % 3 == 0:
        return False
    i = 5
    while i * i <= x:
        if x % i == 0 or x % (i + 2) == 0:
            return False
        i += 6
    return True

def findPrimes(num):
    primes = []
    for i in range(num):
        p = guess()
        while not isPrime(p):
            p = guess()
        primes += [p]
    return primes

cProfile.run('print(findPrimes(500)[:10])')
