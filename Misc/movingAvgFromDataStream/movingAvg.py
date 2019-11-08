# Moving Average from Data Stream
# (Given a stream of integers and a window size, 
# calculate the moving average of all integers 
# in the sliding window.)

from collections import deque

class MovingAverage:
    def __init__(self, size):
        self.size = size
        self.q = deque()
    
    def next(self, val: int):
        if len(self.q) == self.size:
            self.q.popleft()
        self.q.append(val)

        return float(sum(self.q))/float(len(self.q))

if __name__ == "__main__":
    size = 3
    ma = MovingAverage(size)
    a1 = ma.next(1)
    assert a1 == 1
    a2 = ma.next(6)
    assert a2 == (1+6)/2
    a3 = ma.next(3)
    assert a3 == (1+6+3)/3
    a4 = ma.next(4)
    assert a4 == (6+3+4)/3
    print(f"Computed final moving average with window size of {size}: {a4}")