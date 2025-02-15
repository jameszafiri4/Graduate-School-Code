'''
In this program we will run the Dynamic Array test function trying to find values of
initialSize and probRemove that delivers a probability of costly operations of at least
1%. "Try" is the key word in the previous sentence. If it is not possible, we will include
comments explaining why it is not possible (or easy to do) and the significance of that point.
'''

from random import randrange

def test(initialSize, probRemove):
    accCheap, accCosty = 0, 0
    s = initialSize
    m = 2*s
    for i in range(100000):
        if (randrange(100) < probRemove):
            if (s > 0):
                s -= 1
        else:
            if (s == m):
                m = m*2
                s += 1
                accCosty += 1
            else:
                s += 1
                accCheap += 1
    print("Initial size:", initialSize, "Prob Remove:", probRemove, "out of 100")
    print("Costy: {:7} ({:3.1}%)".format(accCosty,accCosty/(accCosty+accCheap)))
    print("Cheap: {:7} ({:3.1}%)".format(accCheap,accCheap/(accCosty+accCheap)))

def main():
    test(10, 1)
    test(10, 5)
    test(20, 1)
    test(20, 5)
    test(50, 1)
    test(50, 5)
    test(100, 1)
    test(100, 5)
    test(1, .0001)
    test(1, 0)
    test(0,0)
    test(100,0)
    test(1, 1)
    test(1, 50)
    test(1, 10)
    

main()

'''
Some things to note are that maximizing the probability of removal will lower the amount
of costly operations since the array will get smaller more often. Not only would it never
increase the odds of costly operations, but it will lower the chance that an append would
result in a costly operation. Also, the bigger the initial size of the array, there will be
a lot less costly operations since it is so big to begin with.

I started with the beginning examples and took what I first observed. I tried to start with a
very small array, and very low probability of removal since we know the opposite decreases your
chance. I went from .001% to .002% so some slight progress was made. I was barely able to make any
progress and only got to .002%. This was a fun problem to play around with but also very difficult
to get to 1% since which ever direction you want to take, the other side moves with it and keeps
your probability the same.
'''
