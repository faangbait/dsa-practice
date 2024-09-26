# Given a string s, return true if it is a palindrome, otherwise return false.

# A palindrome is a string that reads the same forward and backward. It is also case-insensitive and ignores all non-alphanumeric characters.

# Example 1:

# Input: s = "Was it a car or a cat I saw?"

# Output: true
# Explanation: After considering only alphanumerical characters we have "wasitacaroracatisaw", which is a palindrome.

# Example 2:

# Input: s = "tab a cat"

# Output: false
# Explanation: "tabacat" is not a palindrome.

import string

class Solution:
    def isPalindrome(self, s: str) -> bool:
        for x in string.whitespace:
            s = s.replace(x, "")
        for x in string.punctuation:
            s = s.replace(x, "")

        s = s.lower()

        rev_s = list(s)
        rev_s.reverse()

        rev_s = "".join(rev_s)

        if s == rev_s:
            return True
        return False
