class Solution:
    def reverse(self, x: int) -> int:
        if x >= (2**31 - 1) or x <= (-2**31):
            return 0

        rev = 0
        for i in reversed(str(x)):
            if i == "-":
                rev = 0 - rev
            else:
                rev = rev * 10 + int(i)

        if rev >= (2**31 - 1) or rev <= (-2**31):
            return 0
        return rev

def main():
    sol = Solution()
    print(sol.reverse(123))

if __name__ == "__main__":
    main()