class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
      """
      Anagram Groups
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
      
        sorted_dict = {} # Empty dict to store the ordered word as keys and unordered words as values

        for each_word in strs:
            sorted_word = ''.join(sorted(each_word)) # Sorted will return sorted individual strings in a list

            if sorted_word not in sorted_dict:
                sorted_dict[sorted_word] = [each_word]
            
            else:
                sorted_dict[sorted_word].append(each_word)
        
        return sorted_dict.values() # Returns just the values
