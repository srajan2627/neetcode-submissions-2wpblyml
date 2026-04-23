class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heapq.heapify(nums)

        curr = 0

        while len(nums) > k:
            heapq.heappop(nums)
            
        return nums[0]