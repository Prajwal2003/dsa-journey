class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if sorted(s) == sorted(t):
            return True
        else: 
            return False

def main():
    s = "anagram"
    t = "nagaram"
    solution = Solution()
    print(solution.isAnagram(s, t))

if __name__ == "__main__":
    main()