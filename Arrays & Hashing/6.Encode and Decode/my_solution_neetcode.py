class Solution:
    def encode(self, strs: List[str]) -> str:
        combined_string = ""
        for each_word in strs:
            combined_string += str(len(each_word)) + "#" + each_word
        return combined_string

    def decode(self, s: str) -> List[str]:
        i=0
        decoded_strings = []

        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j]) # 3#Two
            j = j+1 # Start of the word
            i = j + length # End of the word
            decoded_strings.append(s[j:i]) # Sliciing from start to end (Doesn't include end letter, exclusive)
            
        return decoded_strings

