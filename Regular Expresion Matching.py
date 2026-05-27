import re
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        if not re.fullmatch(p,s):
            return False
        else: return True

def main():
    sol = Solution()
    print(sol.isMatch("aa","a*"))

if __name__ == "__main__":
    main()