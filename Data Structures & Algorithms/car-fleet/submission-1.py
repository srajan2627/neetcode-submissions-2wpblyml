class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        d = {}
        stack = []

        for i in range(len(position)):
            d[position[i]] = speed[i]
        
        sort_d = sorted(d.items(), key = lambda sort_d: sort_d[0], reverse = True)
        
        for p,s in sort_d:
            t = (target - p)/s
            stack.append(t)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)
        