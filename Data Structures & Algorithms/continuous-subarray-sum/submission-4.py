class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        rem_dict = {0:-1}
        total_sum = 0

        for i,num in enumerate(nums):
            total_sum += num
            remainder = total_sum % k

            if remainder in rem_dict:
                if i - rem_dict[remainder] >= 2:
                    return True
            
            else:
                rem_dict[remainder] = i
        
        return False

