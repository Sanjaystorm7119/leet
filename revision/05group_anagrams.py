
from typing import DefaultDict 
class Solution:
    def group_anagrams(self, strs : list[str]) -> list[list[str]] :
        group = DefaultDict(list)
        for word in strs :
            char_buckets = [0]*26
            for char in word :
                char_buckets[ord('a')-ord(char)] += 1
            group[tuple(char_buckets)].append(word)
        return list(group.values())
    
ans = Solution()
print(ans.group_anagrams(["eat","ate","ant","tan","lol"]))

"""
 a,b,c,d,e,f
[0,0,0,0,0,0]


abc : 1 1 1 0 0 0 => abc, bca, cab , acb , bac , cba
cde : 0 0 1 1 1 0 => cde, dec , ecd, edc , ced , dce
fa  : 1 0 0 0 0 1 => fa , ef 

"""