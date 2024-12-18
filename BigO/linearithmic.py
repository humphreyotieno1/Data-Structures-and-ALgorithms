# merge sort
def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # split the array into two halves
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # recursively call merge_sort on the two halves
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # merge the two sorted halves
    return merge(left_sorted, right_sorted)

# function to merge two sorted arrays
def merge(left, right):
    sorted_array = []
    left_index, right_index = 0, 0
    
    # compare the elements of the two arrays and add the smaller element to the sorted array
    while left_index < len(left) and right_index < len(right):
        if left[left_index] < right[right_index]:
            sorted_array.append(left[left_index])
            left_index += 1
        else:
            sorted_array.append(right[right_index])
            right_index += 1
    
    # add the remaining elements of the left array to the sorted array
    sorted_array.extend(left[left_index:])
    sorted_array.extend(right[right_index:])
    
    return sorted_array

print(merge_sort([38, 27, 43, 3, 9, 82, 10]))