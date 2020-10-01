from collections import deque

class Queue():
    def __init__(self):
        self.dq = deque()

    def enqueue(self, value):
        self.dq.appendleft(value) # O(1)

    def dequeue(self):
        return self.dq.pop()

    def __len__(self):
        return len(self.dq)


# deque  list

# O(1)   O(n)


# [4,6,1,8]


# q.__len__    =>  len(q)

# q.__str__   =>  print(q)
