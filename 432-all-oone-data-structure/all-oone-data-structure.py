class AllOne:

    def __init__(self):
        self.hash = {}
        self.keys = []

    def inc(self, key: str) -> None:
        if key not in self.hash:
            self.hash[key] = 0
            self.keys.append(key)
        self.hash[key] += 1

        value = self.hash[key]
        self.keys.remove(key)
        low, high = 0, len(self.keys)
        while low < high:
            mid = (low + high) // 2
            if self.hash[self.keys[mid]] < value:
                low = mid + 1
            else:
                high = mid
        self.keys.insert(low, key)

    def dec(self, key: str) -> None:
        self.hash[key] -= 1
        if self.hash[key] == 0:
            del self.hash[key]
            self.keys.remove(key)
        else:
            value = self.hash[key]
            self.keys.remove(key)
            low, high = 0, len(self.keys)
            while low < high:
                mid = (low + high) // 2
                if self.hash[self.keys[mid]] < value:
                    low = mid + 1
                else:
                    high = mid
            self.keys.insert(low, key)

    def getMinKey(self) -> str:
        return self.keys[0] if self.keys else ""

    def getMaxKey(self) -> str:
        return self.keys[-1] if self.keys else ""