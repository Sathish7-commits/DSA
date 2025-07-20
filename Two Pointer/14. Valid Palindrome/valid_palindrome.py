class Solution:
    """
    Given a string s, return true if it is a palindrome, otherwise return false.

    A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

    Example 1:

        Input: s = "Was it a car or a cat I saw?"

        Output: true
        Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

    Example 2:

        Input: s = "tab a cat"

        Output: false
        Explanation: "tabacat" is not a palindrome.

    """
    
    def isPalindrome(self, s: str) -> bool:
        left, right = 0, len(s) - 1
        
        while left < right:
            while left < right and not self.alpha_num(s[left]):
                left += 1
            while left < right and not self.alpha_num(s[right]):
                right -= 1
            
            if s[left].lower() != s[right].lower():
                return False
            left, right = left+1, right-1
        
        return True
    
    def alpha_num(self, letter):
        return (ord('A') <= ord(letter) <= ord('Z') or 
                ord('a') <= ord(letter) <= ord('z') or 
                ord('0') <= ord(letter) <= ord('9'))


s = Solution()
print(s.isPalindrome("Was it a car or a cat I saw?"))