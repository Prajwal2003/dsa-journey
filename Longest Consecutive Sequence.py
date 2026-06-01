# import numpy as np

class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        
        if len(nums) == 0:
            return 0

        # l1 = 1
        # ml1 = 0
        # print(nums)
        # for i in range(1,len(nums)):
        #     print(nums[i], l1)
        #     if nums[i-1] + 1 == nums[i]:
        #         l1 += 1
        #     elif l1 > ml1:
        #         ml1 = l1
        #         l1 = 1
        #         print("ml1",ml1)
        
        # if ml1 < l1:
        #     ml1 = l1

        # nums.sort()
        # l = 1
        # ml = 0
        # print(nums)
        # for i in range(1,len(nums)):
        #     print(nums[i], l)
        #     if nums[i-1] + 1 == nums[i]:
        #         l += 1
        #     elif l > ml:
        #         ml = l
        #         l = 1
        #         print("ml",ml)
        # if ml < l:
        #     ml = l
        # if ml1 > ml:
        #     res = ml1
        # else:
        #     res = ml
        # return res

        # nums = np.unique(nums)
        # nums = sorted(set(nums))
        nums = list(set(nums))
        nums.sort()
        l = 1
        ml = 0
        for i in range(1,len(nums)):
            if nums[i-1] + 1 == nums[i]:
                l += 1
            elif l > ml:
                ml = l
                l = 1
            else:
                l = 1
        if ml < l:
            ml = l
        return ml
    
def main():
    nums = [100,4,200,1,3,2]
    print(Solution().longestConsecutive(nums))

if __name__ == "__main__":
    main()