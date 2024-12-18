# binary search
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    
    while left <= right:
        # find the middle index
        mid = (left + right) // 2
        
        # check if the target is at the middle index
        if arr[mid] == target:
            return mid
        # if the target is greater than the middle index, we search the right half
        elif arr[mid] < target:
            left = mid + 1
        # if the target is less than the middle index, we search the left half
        else:
            right = mid - 1
    
    # if the target is not in the array
    return -1

print(binary_search([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 5))