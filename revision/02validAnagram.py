from typing import Counter
class Solution:
    def valid_anagram(self, strs1 : str, strs2 : str) -> bool :
        return Counter(strs1) == Counter(strs2)
    
    def valid_anagram2(self, strs1 : str, strs2 : str) -> bool :
        dict1 , dict2= {} , {}
        for char in strs1:
            dict1[char] = dict1.get(char,0)+1
        for char in strs2:
            dict2[char] = dict2.get(char,0)+1
        return dict1 == dict2


ans = Solution()
print(ans.valid_anagram("sanjay","jaysna"))
print(ans.valid_anagram2("sanjay","jaysna"))


