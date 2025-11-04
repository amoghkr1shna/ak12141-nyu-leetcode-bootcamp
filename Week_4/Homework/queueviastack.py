from collections import deque

class MyQueue:

    def __init__(self):
        self.q = deque()

    def push(self, x: int) -> None:
        # Enqueue new element at back
        self.q.append(x)
        # Rotate the queue so that the new element moves to the front
        for _ in range(len(self.q) - 1):
            self.q.append(self.q.popleft())

    def pop(self) -> int:
        # Dequeue from front (top of stack)
        return self.q.popleft()

    def peek(self) -> int:
        return self.q[0]

    def empty(self) -> bool:
        return len(self.q) == 0



