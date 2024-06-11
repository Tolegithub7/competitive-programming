class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # new_array = []
        # last_array = []
        # arr1 = Counter(arr1)
        # for i in arr2:
        #     new_array += [i]*arr1[i]
        # for i in arr1:
        #     if i not in arr2:
        #         last_array += [i]*arr1[i]
        # return new_array+sorted(last_array)
        presentElements = {}
        lengthOfArr1 = len(arr1)

        for i in range(len(arr2)):
            presentElements[arr2[i]] = i

        def relativeSort(x):
            if x in presentElements:
                return presentElements[x]
            return x + lengthOfArr1

        arr1.sort(key = relativeSort)
        return arr1