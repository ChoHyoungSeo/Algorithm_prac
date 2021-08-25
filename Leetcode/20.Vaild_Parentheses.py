# Runtime: 24 ms, faster than 95.46% of Python3 online submissions for Valid Parentheses.
# Memory Usage: 14.2 MB, less than 64.64% of Python3 online submissions for Valid Parentheses.
class Solution:
    def isValid(self, s: str) -> bool:
        temp = []
        tmp_ans = "True"
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "{" or s[i] == "[":
                temp.append(s[i])
            elif s[i] == ")":
                if temp and temp[-1] == "(":
                    del temp[-1]
                else:
                    return False
            elif s[i] == "}":
                if temp and temp[-1] == "{":
                    del temp[-1]
                else:
                    return False
            elif s[i] == "]":
                if temp and temp[-1] == "[":
                    del temp[-1]
                else:
                    return False
        if temp or tmp_ans == "False":
            return False
        else:
            return True