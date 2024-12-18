# Finding the largest number from an array of integers(n)
n = [2, 5, 6, 20, 3, 15, 30, 76, 7, 90, 2]

#function to find the largest number
def find_max(arr):
    max_num = arr[0]
    
    for num in arr:
        if num > max_num:
            max_num = num
            
    return max_num

print(find_max(n))