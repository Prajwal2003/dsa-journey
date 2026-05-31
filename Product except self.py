import math

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        if nums.count(0) >= 2:
            return [0] * len(nums)
        
        product = 1
        product = math.prod(nums)
        product1 = math.prod(x for x in nums if x != 0)
        res = []
        allarezeros = not any(nums)
        for i in nums:
            if allarezeros:
                res.append(0)
            elif product == 0 and i != 0:
                res.append(0)
            elif product == 0 and i == 0:
                res.append(product1)
            else:
                res.append(product//i)

        return res
    
def main():
    nums = [1,2,3,4]
    print(Solution().productExceptSelf(nums))

if __name__ == "__main__":
    main()