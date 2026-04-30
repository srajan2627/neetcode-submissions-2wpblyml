class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        car_dict = {}

        for i in range(len(position)):
            car_dict[position[i]] = speed[i]

        sort_car_dict = sorted(car_dict.items(),key = lambda car_dict: car_dict[0],reverse = True)

        stack = []

        for p,s in sort_car_dict:
            t = (target - p)/s
            stack.append(t)

            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        
        return len(stack)