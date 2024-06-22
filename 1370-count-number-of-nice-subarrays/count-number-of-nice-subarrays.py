class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        count, i, j, temp, ans = 0, 0, 0, 0, 0
        while(j<len(nums)):
            if nums[j]%2!=0:
                temp+=1
                count = 0
            if temp==k:
                while(nums[i]%2==0):
                    count+=1
                    i+=1
                count+=1
                i+=1
                temp-=1
            ans +=count
            j+=1
        return ans

        # n = len(nums)
        # result = 0
        # a = b = 0
        # cnt = 0
        # for c in range(n):
        #     cnt += (nums[c] % 2 == 1)
        #     if cnt < k:
        #         b += (nums[b] % 2 == 0)
        #         continue
        #     if cnt > k:
        #         b += 1
        #         a = b
        #         cnt -= 1
        #         while nums[b] % 2 == 0:
        #             b += 1
        #     result += b - a + 1
        # return result
