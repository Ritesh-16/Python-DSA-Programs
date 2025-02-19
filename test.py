import heapq
def minOperations(nums,k):
    heapq.heapify(nums)
    count = 0
    while len(nums)>1 and nums[0] < k:
        x = heapq.heappop(nums)
        y = heapq.heappop(nums)

        res = min(x,y)*2 + max(x,y)
        heapq.heappush(nums,res)
        count += 1

    if nums[0]>= k:
        return count
    else:
        return -1
nums = [2,11,10,1,3]
k = 10
print(minOperations(nums,k))