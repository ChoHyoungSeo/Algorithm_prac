# Runtime: 48 ms, faster than 95.17% of Python3 online submissions for Palindrome Number.
# Memory Usage: 14.2 MB, less than 49.50% of Python3 online submissions for Palindrome Number.

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if str(x) == str(x)[::-1]:
            return True
        else:
            return False