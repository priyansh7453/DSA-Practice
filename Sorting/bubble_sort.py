# Bubble sort implementation in Python
def bubble_sort(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        for j in range(0,i):
            # If the element found is greater than the next element, swap them
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr
if __name__ == "__main__":
    arr = [64, 34, 25, 12, 22, 11, 90]
    print("Original array:", arr)
    sorted_arr = bubble_sort(arr)
    print("Sorted array:", sorted_arr)  