class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        if len(set(nums)) == len(nums):
            return False
        else: 
            return True
    
def main():
    nums = [1,2,3,1]
    print(Solution().containsDuplicate(nums))

if __name__ == "__main__":
    main()