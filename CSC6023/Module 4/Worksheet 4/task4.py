'''
In this program we will run the Knapsack Greedy code
using the following format (list of items - [value, weight]):

We will now come up with one more knapsack test case of our own,
where more than one TYPE OF ITEM ends up in the knapsack.
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

'''
Here we will create our own test case that will occur in
more than one item ending up in the knapsack
'''
def main():
    values = [6, 10, 21]
    weights = [4, 3, 4]

    print(knapsack(values, weights, 15))
    
'''
After running the program, we were able to make the knapsack
have more than only one type of item inside of it. See output:

[2, 2, 2, 1]

'''

if __name__ == "__main__":
    main()
