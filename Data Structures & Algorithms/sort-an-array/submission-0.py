class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        def maxheap(heaplen,index):
            left = 2 * index + 1
            right = 2 * index + 2

            largest = index

            if left < heaplen and nums[left] > nums[largest]:
                largest = left

            if right < heaplen and nums[right] > nums[largest]:
                largest = right
            
            if largest != index:
                nums[index], nums[largest] = nums[largest], nums[index]
                maxheap(heaplen,largest)

        for i in range(len(nums)//2 - 1, -1, -1):
            maxheap(len(nums), i)

        for i in range(len(nums) - 1, 0, -1):
            nums[i], nums[0] = nums[0], nums[i]
            maxheap(i,0)
        
        return nums