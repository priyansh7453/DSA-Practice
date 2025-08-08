#Swap alternate elements in an array
def swap_alternate(arr):
    for i in range(0, len(arr) - 1, 2):
        arr[i], arr[i + 1] = arr[i + 1], arr[i]
    return arr

# Example usage
arr = [1, 2, 3, 4, 5]
print(swap_alternate(arr))  # Output: [2, 1, 4, 3, 5]