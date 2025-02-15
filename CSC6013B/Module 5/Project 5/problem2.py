
def Swap(A, i, j):
    temp = A[i]
    A[i] = A[j]
    A[j] = temp

def BubbleSort(A):
    # to keep total count outside the loops
    total_compare = 0
    total_swap = 0
    
    for i in range(len(A)-1):
        # counts per iteration
        compare = 0
        swap = 0
        # to see if another iteration is needed
        swapped = False
        
        for j in range(len(A)-i-1):
            compare += 1
            total_compare += 1
            # sees if next element is smaller
            if A[j+1] < A[j]:
                swap += 1
                total_swap += 1
                Swap(A, j+1, j)
                # set to True after each swap
                swapped = True
        print(f"After iteration {i}: Array is {A}, with {compare} comparisons and {swap} swaps.")
        # if a swap did not occur on last iteration, break out of loop early
        if not swapped:
            break
    print(f"\nTotal comparisons = {total_compare} and total swaps = {total_swap}")

A4 = [44, 63, 77, 17, 20, 99, 84, 6, 39, 52]

A5 = [52, 84, 6, 39, 20, 77, 17, 99, 44, 63]

A6 = [6, 17, 20, 39, 44, 52, 63, 77, 84, 99]

BubbleSort(A4)

BubbleSort(A5)

BubbleSort(A6)
