import math
def min_eating_speed(piles, h):

    left = 1
    right = max(piles)

    answer = right

    while left <= right:

        mid = left + (right - left) // 2
        hours = 0

        # calculate total hours needed 
        for pile in piles:
            hours += math.ceil(pile/mid)
        
        if hours <= h:

            answer = mid

            # move in left
            right = mid - 1
        
        else:

            # too slow move in right
            left = mid + 1
    
    return answer

piles = [3, 6, 7, 11]
h = 8

print(min_eating_speed(piles, h))