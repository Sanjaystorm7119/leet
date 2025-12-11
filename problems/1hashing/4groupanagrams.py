from typing import DefaultDict , List
class Solution:
    def group_anagrams(self , words: List[str]) -> List[List[str]] :
        res = DefaultDict(list)

        for word in words :
            char_bucket = [0]*26
            for char in word :
                char_bucket[ord(char) - ord('a')] += 1
            res[tuple(char_bucket)].append(word)
        return list(res.values())
    
ans = Solution()
print(ans.group_anagrams(["eat","tea","tan","ate","nat","bat"]))