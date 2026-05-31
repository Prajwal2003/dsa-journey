class Solution:
    def minElement(self, nums: List[int]) -> int:
        mini = 99999
        for i in nums:
            s = sum(int(digit) for digit in str(abs(i)))
            if s < mini:
                mini = s
        return mini

def main():
    nums = [123, 456, -789, 12]
    print(Solution().minElement(nums))

if __name__ == "__main__":
    main()