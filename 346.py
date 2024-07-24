"""
346. Moving Average from Data Stream

Given a stream of integers and a window size, calculate the moving average of 
all integers in the sliding window.

Implement the MovingAverage class:
- MovingAverage(int size) Initializes the object with the size of the window 
  size.
- double next(int val) Returns the moving average of the last size values of 
  the stream.
"""


class MovingAverage:

    def __init__(self, size: int):
        self.elements = []
        self.capacity = size

    def next(self, val: int) -> float:
        if len(self.elements) >= self.capacity:
            self.elements.pop(0)
        self.elements.append(val)
        return self._avg()

    def _avg(self):
        return sum(self.elements) / len(self.elements)


# Your MovingAverage object will be instantiated and called as such:
# obj = MovingAverage(size)
# param_1 = obj.next(val)
