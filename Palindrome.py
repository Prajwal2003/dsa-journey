class Solution:
    def isPalindrome(self, x: int) -> bool:
        i = 0
        j = len(str(x)) - 1
        st = str(x)
        while i <= j:
            if st[i] != st[j]:
                return False
            else:
                i = i + 1
                j = j - 1
        return True

def main():
    sol = Solution()
    print(sol.isPalindrome(121))

if __name__ == "__main__":
    main()