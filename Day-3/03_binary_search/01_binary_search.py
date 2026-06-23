def binary_search(arr, target):

    left = 0
    right = len(arr) - 1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:
            return mid
        
        elif arr[mid] < target:
            left = mid + 1

        elif arr[mid] > target:
            right = mid - 1

    return - 1
    
arr = [1, 2, 3, 4, 5, 6]
target = 4

print(binary_search(arr, target))
        
