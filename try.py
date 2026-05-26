import re

class Solution:
    def myAtoi(self, s: str) -> int:
        pattern = r"^\s*([+-]?\d+)"
        match = re.search(pattern, s)
        
        if not match:
            return 0
        
        num = int(match.group(1))
        
        INT_MIN = -2147483648
        INT_MAX = 2147483647
        
        if num < INT_MIN:
            return INT_MIN
        if num > INT_MAX:
            return INT_MAX
            
        return num

def main():
    sol = Solution()
    print(sol.myAtoi("   -42"))

if __name__ == "__main__":
    main()