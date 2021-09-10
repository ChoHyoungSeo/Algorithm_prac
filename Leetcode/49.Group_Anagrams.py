# temp
# Runtime: 174 ms, faster than 13.67% of Python3 online submissions for Group Anagrams.
# Memory Usage: 17.9 MB, less than 49.45% of Python3 online submissions for Group Anagrams.
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)
        return anagrams.values()