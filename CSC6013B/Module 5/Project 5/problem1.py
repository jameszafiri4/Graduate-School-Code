
def Swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def SelectionSort(A):
    for i in range(len(A)-1):
        # counts per iteration
        compare = 0
        swap = 0
        iterate = 0
        # loop setting item to compare going backwards on list
        for j in range(len(A)-i-1, 0, -1):
            m = j
            # loop to compare the items
            for k in range(i, j):
                compare += 1
                if A[k] > A[m]:
                    m = k
            # making sure item is not the same from prior loop
            if m != j:
                swap += 1
                Swap(A, j, m)
                iterate += 1
                print(f"After iteration {iterate}: Array is {A}, with {compare} comparisons, and {swap} swaps.")
                compare = 0
                swap = 0

A1 = [63, 44, 17, 77, 20, 6, 99, 84, 52, 39]

A2 = [84, 52, 39, 6, 20, 17, 77, 99, 63, 44]

A3 = [99, 84, 77, 63, 52, 44, 39, 20, 17, 6]

SelectionSort(A1)

SelectionSort(A2)

SelectionSort(A3)
