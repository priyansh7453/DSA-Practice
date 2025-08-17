# Bubble sort implementation in Python
def bubble_sort(arr):
    n = len(arr)
    swap = False  # Initialize swap to True to enter the loop
    for i in range(n-1, -1, -1):
        for j in range(0,i):
            # If the element found is greater than the next element, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                swap = True
        # If no two elements were swapped by inner loop, then break 
        if not swap:
            break
        print("cnt")
    return arr
if __name__ == "__main__":
    # arr = [64, 34, 25, 12, 22, 11, 90]
    arr = [1,2,3,4,5,6,7,8,9,10]
    print("Original array:", arr)
    sorted_arr = bubble_sort(arr)
    print("Sorted array:", sorted_arr)  