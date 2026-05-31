from collections import defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        omg = defaultdict(list)
        for i in strs:
            omg[str(sorted(i))].append(i)
        return list(omg.values())
    
def main():
    strs = ["eat","tea","tan","ate","nat","bat"]
    print(Solution().groupAnagrams(strs))

if __name__ == "__main__":
    main()