'''
CSC 6301 Project 7
Finding Primes Analysis
James Zafiri
10/13/2023
Version 1.0.0
'''

import random
import cProfile

def guess():
    return random.randint(2, 5000)

def isPrime(x):
    for i in range(x):
        for j in range(x):
            if i * j == x:
                return False
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
