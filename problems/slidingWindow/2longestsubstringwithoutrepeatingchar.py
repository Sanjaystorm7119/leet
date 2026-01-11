class Solution:
    def longest_substring_without(self , s: str) -> int :
        """
        abcabca => 3 abc
        """
        start , end = 0 , 0
        dic = {}
        max_len = 0
        while end < len(s):
            if s[end] in dic and dic[s[end]] >= start :
                start = dic[s[end]] + 1

            max_len = max(max_len, end - start + 1)
            dic[s[end]] = end
            end += 1
        print(s[start:end])
        return max_len
    
ans = Solution()
print(ans.longest_substring_without("abcabca"))