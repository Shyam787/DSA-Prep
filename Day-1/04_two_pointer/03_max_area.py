def max_area(heights):

    left = 0
    right = len(heights) - 1
    max_area = 0

    while left < right:

        width = right - left
        current_area = min(heights[left], heights[right]) * width

        max_area = max(max_area, current_area)

        if heights[left] < heights[right]:
            left += 1
        else:
            right -= 1

    return max_area

heights = [1,8,6,2,5,4,8,3,7]
print(max_area(heights))