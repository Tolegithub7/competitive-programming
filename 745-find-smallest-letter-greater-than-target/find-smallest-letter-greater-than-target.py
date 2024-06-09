class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    #     lists = []
    #     for i in letters:
    #         if i > target:
    #             lists.append(i)
    #     if lists == []:
    #         return letters[0]
    #     return min(lists)
        for i in letters:
            if i > target:
                return i
        return letters[0]
    # def nextGreatestLetter(self, letters: List[str], target: str) -> str:
    #     n = len(letters)
    #     l, r = 0, n - 1
    #     if target >= letters[r]:
    #         return letters[0]
    #     while l <= r:
    #         mid = l + (r-l)// 2
    #         if letters[mid] <= target:
    #             l = mid + 1
    #         else:
    #             if mid > 0 and letters[mid - 1] <= target:
    #                 return letters[mid]
    #             r = mid - 1
    #     return letters[l]