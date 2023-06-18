class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        #using two pointersRuntime
        # 226 ms
        # Beats
        # 37.86%
        # left, right = 0, len(s)-1
        # while left < right:
        #     s[left], s[right] = s[right], s[left]
        #     left += 1
        #     right -= 1

        #python
        #Runtime
        # 217 ms
        # Beats
        # 68.64%
#         s.reverse()


        # Runtime
        # 209 ms
        # Beats
        # 84.27%
        s[:] = s[::-1]