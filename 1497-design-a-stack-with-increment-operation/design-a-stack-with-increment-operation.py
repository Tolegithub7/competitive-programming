class CustomStack:

    def __init__(self, maxSize: int):
        self.arr = []
        self.size = maxSize

    def push(self, x: int) -> None:
        if len(self.arr) < self.size:
            self.arr.append(x)

    def pop(self) -> int:
        if len(self.arr) > 0:
            return self.arr.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        temp = min(k, len(self.arr))
        for i in range(0, temp):
            self.arr[i] += val