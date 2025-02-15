def insertion_sort(InputList): 
    for i in range(1, len(InputList)): 
        j = i-1 
        # print(f"Starting with element at index {i}")
        nxt_element = InputList[i] 
        nxt_index = i
# Compare the current element with next one
        while (InputList[j] > nxt_element) and (j >= 0):
            InputList[j+1] = InputList[j] 
            # print(f"\t\tSwapping elements at index {j+1} and {j}")
            j=j-1 
        InputList[j+1] = nxt_element 
        # print(f"\tSwapping elements at index {j+1} and {nxt_index}")

list = [19,2,31,45,30,11,121,27]
# print('  0, 1,  2,  3,  4,  5,   6,  7')
# print(list)
insertion_sort(list) 
# print(list)
