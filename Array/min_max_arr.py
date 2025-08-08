# def minimum(array):
#     min = array[0]
#     for i in range(len(array)):
#         if min > array[i]:
#             min = array[i]
#     return min
        
# def maximum(array):
#     max = array[len(array) - 1]
#     for i in range(len(array)):
#         if max < array[i]:
#             max = array[i]
#     return max
#     # return [min, max]

# def min_max(array):
#     min_val = array[0]
#     max_val = array[0]
#     for i in range(1, len(array)):
#         if array[i] < min_val:
#             min_val = array[i]
#         elif array[i] > max_val:
#             max_val = array[i]
#     return min_val, max_val
def min_max(array):
    min = array[0]
    max = array[0]
    for i in array:
        if i < min:
            min = i
        if i > max:
            max = i
    return min, max

array = [1,8,9,6,4,3,7,2,1,]
# print("min element of array ",minimum(array))
# print("max element of array ",maximum(array))
min_val, max_val = min_max(array)
print("Minimum element of array:", min_val)
print("Maximum element of array:", max_val)
