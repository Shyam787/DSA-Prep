from collections import Counter
import heapq

def top_k_frequency(nums, k):

    freq = Counter(nums)
    heap = []

    for num, count in freq.items():
        # first count because python sorts tuples in lexicographical way 
        heapq.heappush(heap, (count, num))

        if len(heap) > k:
            heapq.heappop(heap)
        
    result = []

    while heap:
        result.append(heapq.heappop(heap)[1]) # [1] for extracting num from tuple which is at 2nd position (count, num)

    return result

nums = [1,1,1,2,2,3]
k = 2

print(top_k_frequency(nums, k))
