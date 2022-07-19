# Runtime: 36 ms, faster than 58.61% of Python3 online submissions for Longest Common Prefix.
# Memory Usage: 14.2 MB, less than 81.73% of Python3 online submissions for Longest Common Prefix.
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        ans = ""
        tmp = True
        strs.sort(key = len)
        for i in range(len(strs[0])):
            ans += ((strs[0][i]))
            for alp in strs:
                try:
                    if ans[i] == alp[i]:
                        continue
                    else:
                        ans = ans[:-1]
                        tmp = False
                        break
                        return ans
                except:
                    break
                    return ans
            if not tmp:
                break
                return ans
        return ans