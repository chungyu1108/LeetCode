from collections import deque  

class FirstUnique:  

    def __init__(self, nums):  
        self.queue = deque()  
        self.count = {}  

        for num in nums:  
            self.add(num)  

    def showFirstUnique(self):  
        while self.queue:  
            if self.count[self.queue[0]] == 1:  
                return self.queue[0]  
            self.queue.popleft()  
        return -1  

    def add(self, value):  
        if value in self.count:  
            self.count[value] += 1  
        else:  
            self.count[value] = 1  
            self.queue.append(value)


# Your FirstUnique object will be instantiated and called as such:
# obj = FirstUnique(nums)
# param_1 = obj.showFirstUnique()
# obj.add(value)