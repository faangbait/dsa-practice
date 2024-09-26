# Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.

# An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

# Example 1:

# Input: strs = ["act","pots","tops","cat","stop","hat"]

# Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
# Example 2:

# Input: strs = ["x"]

# Output: [["x"]]
# Example 3:

# Input: strs = [""]

# Output: [[""]]
# Constraints:

# 1 <= strs.length <= 1000.
# 0 <= strs[i].length <= 100
# strs[i] is made up of lowercase English letters.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_strs = []
        hmap = {}
        for s in strs:
            sorted_strs += ["".join(sorted(list(s)))]
        
        sorted_strs = set(sorted_strs)
        
        for s in sorted_strs:
            hmap.update({s: []})
        
        for s in strs:
            for k in hmap.keys():
                if self.isAnagram(s,k):
                    hmap[k] = hmap[k] + [s]
        
        output = []
        for k,v in hmap.items():
            output += [v]
            
        return output

    def isAnagram(self, s: str, t: str) -> bool:
        t = list(t)
        try:
            for letter in s:
                t.remove(letter)
            if len(t) > 0:
                return False
            return True
        except Exception as e:
            return False
