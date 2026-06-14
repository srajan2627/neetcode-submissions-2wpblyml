class MyCircularQueue:

    def __init__(self, k: int):
        """
        Initializes the object with the size of the queue to be k.
        """
        self.queue = [0] * k
        self.capacity = k
        self.head = 0
        self.count = 0

    def enQueue(self, value: int) -> bool:
        """
        Inserts an element into the circular queue. 
        Return true if the operation is successful.
        """
        if self.isFull():
            return False
        
        # Calculate the next available position to insert the item
        target_idx = (self.head + self.count) % self.capacity
        self.queue[target_idx] = value
        self.count += 1
        return True

    def deQueue(self) -> bool:
        """
        Deletes an element from the circular queue. 
        Return true if the operation is successful.
        """
        if self.isEmpty():
            return False
        
        # Move the head pointer one step forward circularly
        self.head = (self.head + 1) % self.capacity
        self.count -= 1
        return True

    def Front(self) -> int:
        """
        Gets the front item from the queue. If the queue is empty, return -1.
        """
        if self.isEmpty():
            return -1
        return self.queue[self.head]

    def Rear(self) -> int:
        """
        Gets the last item from the queue. If the queue is empty, return -1.
        """
        if self.isEmpty():
            return -1
        
        # Calculate the exact position of the last inserted element
        tail_idx = (self.head + self.count - 1) % self.capacity
        return self.queue[tail_idx]

    def isEmpty(self) -> bool:
        """
        Checks whether the circular queue is empty or not.
        """
        return self.count == 0

    def isFull(self) -> bool:
        """
        Checks whether the circular queue is full or not.
        """
        return self.count == self.capacity


# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()