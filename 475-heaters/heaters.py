class Solution:
    def findRadius(self, houses, heaters):
        heaters.sort()
        result = float('-inf')
        for house in houses:
            min_rad = self.binary_search(house, heaters)
            result = max(result, min_rad)
        return result
        
    def binary_search(self, house, heaters):
        low = 0
        high = len(heaters) - 1
        min_dist = float('inf')
        while low <= high:
            mid = (low + high) // 2
            if heaters[mid] == house:
                return 0
            if heaters[mid] < house:
                low = mid + 1
            else:
                high = mid - 1
            min_dist = min(min_dist, abs(house - heaters[mid]))
        return min_dist
