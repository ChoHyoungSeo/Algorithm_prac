# # Beats 5.18% (240ms)
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         #preprocessing
#         strs = []
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
        
#         #isPalindrome
#         while len(strs) > 1:
#             if strs.pop(0) != strs.pop():
#                 return False
#         return True

# #Beats 35.90% (67ms)
# from collections import deque
# class Solution:
#     def isPalindrome(self, s: str) -> bool:
#         # strs: Deque = collections.deque()
#         strs = deque()
#         for char in s:
#             if char.isalnum():
#                 strs.append(char.lower())
#         while len(strs) > 1:
#             if strs.popleft() != strs.pop():
#                 return False
#         return True

# Beats 41.40% (64ms)
class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]', '', s)
        return s == s[::-1]