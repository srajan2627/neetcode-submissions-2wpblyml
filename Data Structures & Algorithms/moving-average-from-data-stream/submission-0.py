class MovingAverage:

    def __init__(self, size: int):
        self.size = size
        self.curr_sum = 0
        self.queue = deque()

    def next(self, val: int) -> float:
        self.queue.append(val)

        if len(self.queue) > self.size:
            left = self.queue.popleft()
            self.curr_sum = self.curr_sum - left + val
        
        else:
            self.curr_sum += val
            
        
        return self.curr_sum/len(self.queue)




# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
