def remove_duplicates(arr):
    # index = 1
    # for i in range(1,len(arr)):
    #     if arr[i] != arr[i-1]:
    #         arr[index] = i
    #         arr[index] += 1
    
    # print(index)
    elem_count = {}
    
    # Step 1: Count occurrences of each character
    for ele in arr:
        elem_count[ele] = elem_count.get(ele, 0) + 1

    # Step 2: Collect characters that appear more than once
    repeated = {}
    for ele, count in elem_count.items():
        if count == 1:
            repeated[ele] = count
    # return repeated.keys()
    return repeated


arr = [1, 2, 2, 3, 4, 4, 4, 5, 5]
print(remove_duplicates(arr))