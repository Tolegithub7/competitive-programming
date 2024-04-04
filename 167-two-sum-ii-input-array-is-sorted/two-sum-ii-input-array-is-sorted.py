class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)-1
        while(left<=right):
            current_sum = numbers[left]+numbers[right]
            if current_sum>target:
                right-=1
            elif current_sum<target:
                left+=1
            else:
                return [left+1,right+1]
