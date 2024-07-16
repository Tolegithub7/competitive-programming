class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
#with bubble sort
        n = len(heights)
        for i in range(n - 1):
            for j in range(n - i - 1):
                if heights[j] < heights[j + 1]:
                    heights[j], heights[j + 1] = heights[j + 1], heights[j]
                    names[j], names[j + 1] = names[j + 1], names[j]
        return names

#with selection sort
        # n = len(heights)
        # for i in range(n-1):
        #     min_index = i
        #     for j in range(i+1, n):
        #         if heights[j]>heights[min_index]:
        #             min_index = j
        #     heights[i], heights[min_index] = heights[min_index], heights[i]
        #     names[i], names[min_index] = names[min_index], names[i]
        # return names

#with insertion sort
        # n = len(heights)
        # for i in range(1, n):
        #     key = heights[i]
        #     name_key = names[i]
        #     j = i-1
        #     while j >= 0 and heights[j] < key:
        #         heights[j+1] = heights[j]
        #         names[j+1] = names[j]
        #         j -= 1
        #     heights[j+1] = key
        #     names[j+1] = name_key
        # return names


        # ans=[]
        # for i in range(len(heights)):
        #     ans.append([heights[i],names[i]])
        # ans=sorted(ans,reverse=True)
        # return[names for heights,names in ans]
        
        # return list(a for a, b in sorted(zip(names, heights), key=lambda x:-x[1]))