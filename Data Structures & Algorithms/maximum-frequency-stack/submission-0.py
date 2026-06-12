from collections import defaultdict

class FreqStack:

    def __init__(self):
        # Maps value to its current total frequency
        self.freq = {}
        
        # Maps a specific frequency to a list/stack of values with that frequency
        self.group = defaultdict(list)
        
        # Tracks the global maximum frequency currently in the stack
        self.max_freq = 0

    def push(self, val: int) -> None:
        # 1. Update the total frequency count for this value
        f = self.freq.get(val, 0) + 1
        self.freq[val] = f
        
        # 2. Update the maximum frequency seen so far if this beats it
        if f > self.max_freq:
            self.max_freq = f
            
        # 3. Add this value to the stack corresponding to its current frequency level
        self.group[f].append(val)

    def pop(self) -> int:
        # 1. Look at the stack belonging to the highest frequency level and pop the top element
        val = self.group[self.max_freq].pop()
        
        # 2. Decrement the frequency count for that popped value
        self.freq[val] -= 1
        
        # 3. If the highest frequency stack is now completely empty,
        # collapse the max_freq pointer down by 1 level
        if not self.group[self.max_freq]:
            self.max_freq -= 1
            
        return val


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(val)
# param_2 = obj.pop()