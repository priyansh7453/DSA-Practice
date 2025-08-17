# Insertion sort implementation in Python
def insertion_sort(arr):
    for i in range(len(arr)):
        j = i
        # Move elements of arr[0..i-1], that are greater than key,
        # to one position ahead of their current position
        while j > 0 and arr[j-1] > arr[j]:
            arr[j], arr[j-1] = arr[j-1], arr[j]
            j -= 1
    return arr
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6]
    print("Original array:", arr)
    sorted_arr = insertion_sort(arr)
    print("Sorted array:", sorted_arr)
    