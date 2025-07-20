class Solution:
"""
Design an algorithm to encode a list of strings to a single string. The encoded string is then decoded back to the original list of strings.
Please implement encode and decode

Example 1:
  Input: ["neet","code","love","you"]
  Output:["neet","code","love","you"]

Example 2:
  Input: ["we","say",":","yes"]
  Output: ["we","say",":","yes"]
  
"""
    def encode(self, strs: List[str]) -> str:
        combined_string = ""
        for each_string in strs:
            combined_string += str(len(each_string)) + "#" + each_string
        return combined_string

    def decode(self, s: str) -> List[str]:
        i = 0 # To track the starting index of the word
        decoded_string = []

        while i < len(s):
            j = i # To track the position of # and end of the word
            
            while s[j] != '#':
                j += 1 
            
            length = int(s[i:j]) # Now we get the 3 alone from 3#One
            i = j + 1 # starting index of the word 3#One -> i = 2 
            j = i + length  # ending index of the word 3#One -> j = 2 + 3 = 5

            decoded_string.append(s[i:j])
            
            i = j # Reassign the index of the next word
        
        return decoded_string
      
