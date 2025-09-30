class Solution:
    """

    Time: O(n) (each char enters/leaves window at most once)

    Space: O(min(n, charset)) (set of chars, ≤ 26 or 128 or 256 depending on alphabet)

    Longest Substring Without Repeating Characters

    Given a string s, find the length of the longest substring without duplicate characters.

    A substring is a contiguous sequence of characters within a string.

    Example 1:

    Input: s = "zxyzxyz"
    Output: 3

    Explanation: The string "xyz" is the longest without duplicate characters.

    Example 2:

    Input: s = "xxxx"

    Output: 1
    """
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        seen = set()
        max_length = 0

        for right in range(len(s)):

            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            seen.add(s[right])

            max_length = max(max_length, right - left + 1)

        return max_length


