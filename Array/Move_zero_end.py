# Moving all zeros to the end of the array
def move_zero_end(arr):
    temp = []
    
    for i in range(len(arr)):
        if arr[i] != 0:
            temp.append(arr[i])
            
    for i in range(len(arr)):
        if arr[i] == 0:
            temp.append(arr[i])
            
    # return temp

    for i in range(len(arr)):
        arr[i] = temp[i]
        
    return arr

# Example usage
arr = [0, 1, 0, 3, 12]
print(move_zero_end(arr))  # Output: [1, 3, 12, 0, 0]
# --- IGNORE ---