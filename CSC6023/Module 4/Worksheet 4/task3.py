'''
In this program we will run the Knapsack Greedy code
for the following cases (list of items - [value, weight]):

([5,10] [8,20] [12,30]) - capacity 838

([3,17] [5,23] [7,29] [11,31] [13,37] - capacity 997

([5,25] [6,36] [7,49] [8,64]) - capacity 250

([5,25] [6,36] [7,49] [8,64]) - capacity 360

We will include the correct results in our comments for each case.
'''

def knapsack(v, w, cap):
    rwv = []         # triplet ratio, weight, value, index
    for i in range(len(v)):
        rwv.append([v[i]/w[i],w[i],v[i],i])
    rwv.sort(reverse=True)    # sort from high to low rate
    ans = []                     # the list of added items
    tw = 0                                  # total weight
    found = True
    while (found):        # until no fitting item is found
        found = False
        for t in rwv:              # search an item to add
            if (t[1] + tw) <= cap:      # if the item fits
                ans.append(t[3])                  # add it
                tw += t[1]
                found = True
                break
    return ans           # returns the list of added items

def main():
    items = int(input("Number of distinct items: "))
    values, weights = [],[]
    for i in range(items):
        v = int(input("Value of item "+str(i+1)+": "))
        w = int(input("Weight of item "+str(i+1)+": "))
        values.append(v)
        weights.append(w)
    capacity = int(input("Maximum weight (capacity): "))
    answer = knapsack(values, weights, capacity)
    tv, tw = 0, 0
    for a in answer:
        print("Item - Value:", values[a], "- Weight:", weights[a])
        tv += values[a]
        tw += weights[a]
    print("Items:", len(answer), "- Value:", tv, "- Weight:", tw)

'''
Case 1 - ([5,10] [8,20] [12,30]) - capacity 838

Solution 1 = Items: 83 - Value: 415 - Weight: 830 (only used [5,10])


Case 2 - ([3,17] [5,23] [7,29] [11,31] [13,37] - capacity 997

Solution 2 = Items: 32 - Value: 352 - Weight: 992 (only used [11,31])


Case 3 - ([5,25] [6,36] [7,49] [8,64]) - capacity 250

Solution 3 = Items: 10 - Value: 50 - Weight: 250 (only used [5,25])


Case 4 - ([5,25] [6,36] [7,49] [8,64]) - capacity 360

Solution 4 = Items: 14 - Value: 70 - Weight: 350 (only used [5,25])

'''


if __name__ == "__main__":
    main()

