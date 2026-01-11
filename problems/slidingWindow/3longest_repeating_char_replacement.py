class Solution:
    def longest_repeating_char_replacement(self , s : str , k : int) -> int :
        start , end = 0 , 0
        max_len = 0
        majority = 0
        counts = {}
        while end < len(s):
            counts[s[end]] = counts.get(s[end],0)+1
            majority = max(majority , counts[s[end]])

            while majority + k < end - start + 1:
                counts[s[start]] = counts.get(s[start],0)-1
                start += 1
            max_len = max(max_len , end - start + 1)
            end += 1

        return max_len
    
ans = Solution()
print(ans.longest_repeating_char_replacement("ababc",2))