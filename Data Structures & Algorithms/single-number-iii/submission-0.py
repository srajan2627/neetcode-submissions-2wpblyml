class Solution:
    def singleNumber(self, nums: list[int]) -> list[int]:
        # Step 1: Get the XOR of the two unique numbers (a ^ b)
        combined_xor = 0
        for num in nums:
            combined_xor ^= num
            
        # Step 2: Isolate the rightmost set bit (the differing bit)
        # In Python, (x & -x) is a bitwise trick to isolate the lowest set bit.
        diff_bit = combined_xor & -combined_xor
        
        # Step 3: Partition the array into two groups and find the numbers
        unique_num1 = 0
        unique_num2 = 0
        
        for num in nums:
            # Group 1: Numbers that have the distinguishing bit set to 1
            if num & diff_bit:
                unique_num1 ^= num
            # Group 2: Numbers that have the distinguishing bit set to 0
            else:
                unique_num2 ^= num
                
        # Return the two isolated numbers
        return [unique_num1, unique_num2]