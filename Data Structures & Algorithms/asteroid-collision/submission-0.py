class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = [asteroids[0]]

        for a in range(1,len(asteroids)):
            if asteroids[a] < 0 and stack[-1] < 0:
                stack.append(asteroids[a])
            elif asteroids[a] > 0 and stack[-1] > 0:
                stack.append(asteroids[a])
            elif asteroids[a] > 0 and stack[-1] < 0:
                stack.pop()
                stack.append(asteroids[a])
            elif asteroids[a] < 0 and stack[-1] > 0:
                if abs(asteroids[a]) == abs(stack[-1]):
                    stack.pop()
            
        
        return stack