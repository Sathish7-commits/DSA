from collections import defaultdict

class Solution:
    """
    Given an array of strings strs, group all anagrams together into sublists. You may return the output in any order.
    An anagram is a string that contains the exact same characters as another string, but the order of the characters can be different.

    Example 1:
        Input: strs = ["act","pots","tops","cat","stop","hat"]
        Output: [["hat"],["act", "cat"],["stop", "pots", "tops"]]
    
    Example 2:
        Input: strs = ["x"]
        Output: [["x"]]

    Example 3:
        Input: strs = [""]
        Output: [[""]]
    """

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = defaultdict(list) # This step is required otherwise you can't store the list as a key in dict (THIS 1)
    
        for word in strs:
            counts = [0] * 26

            for letter in word:
                counts[ord(letter) - ord("a")] += 1
            
            result[tuple(counts)].append(word) # (THIS 1) - Useful here, when list is converted to tuple and assigned a value against it
        
        return result.values()
