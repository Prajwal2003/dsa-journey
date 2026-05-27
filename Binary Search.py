class Solution:
    def search(self, nums: List[int], target: int) -> int:
        i = 0
        j = len(nums) - 1
        while i <= j:
            m = (i+j) // 2
            if nums[m] == target:
                return m
            if nums[m] < target:
                i = m + 1
            else:
                j = m - 1
        return -1

def main():
    nums = [-1,0,3,5,9,12]
    target = 9
    solution = Solution()
    print(solution.search(nums, target))

if __name__ == "__main__":
    main()