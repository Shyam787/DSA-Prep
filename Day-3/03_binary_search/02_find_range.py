def first_find(arr, target):

    left = 0
    right = len(arr) - 1

    first = -1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:
            first = mid
            
            # continue searching left boundary
            right = mid - 1

        elif arr[mid] > target:
            right = mid - 1
        
        else:
            left = mid + 1

    return first

def last_find(arr, target):

    left = 0
    right = len(arr) - 1

    last = -1

    while left <= right:

        mid = left + (right - left) // 2

        if arr[mid] == target:
            last = mid
            
            # continue searching right boundary
            left = mid + 1

        elif arr[mid] > target:
            right = mid - 1
        
        else:
            left = mid + 1

    return last

def search_range(arr, target):

    return [
        first_find(arr, target),
        last_find(arr, target)
    ]

arr = [1, 2, 3, 3, 3, 4, 5]
target = 3
print(search_range(arr, target))