class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs:
            return ""
        for i in range(len(strs[0])):
            char = strs[0][i]
            for j in strs[1:]:
                if len(j) <= i or char != j[i]:
                    return strs[0][:i]
        return strs[0]
    
def main():
    s = Solution()
    print(s.longestCommonPrefix(["flower","flow","flight"]))
    print(s.longestCommonPrefix(["dog","racecar","car"]))

if __name__ == "__main__":
    main()