from collections import deque


class Solution:

    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        ans = []
        # The deque will store INDICES, not the actual values
        q = deque()

        for i, num in enumerate(nums):
            # 1. Pop elements from the back of the queue if they are smaller
            # than the current number (they can never be the maximum anymore)
            while q and nums[q[-1]] < num:
                q.pop()

            # 2. Add the current element's index to the back
            q.append(i)

            # 3. Check if the maximum element (at the front) has fallen
            # out of the left boundary of our sliding window
            if q[0] == i - k:
                q.popleft()

            # 4. Once our window reaches size k, start recording the maximums
            # The maximum is always at the front of the queue: nums[q[0]]
            if i >= k - 1:
                ans.append(nums[q[0]])

        return ans