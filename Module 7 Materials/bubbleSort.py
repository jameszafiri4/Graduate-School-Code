def bubblesort(list): 
    # Swap elements to arrange in order 
    for iter_num in range(len(list)-1,0,-1): 
        print(f"iter_num is {iter_num}")
        for idx in range(iter_num): 
            print(f"\tidx is {idx}")
            if list[idx]>list[idx+1]: 
                temp = list[idx] 
                list[idx] = list[idx+1] 
                list[idx+1] = temp
                print(f"\t\tFlipping {idx} and {idx+1}")
                print(f"\t\t{list}")

list = [19,2,31,45,6,11,121,27] 
bubblesort(list)
print(list)
