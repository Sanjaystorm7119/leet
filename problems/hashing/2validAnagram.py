from collections import Counter
class Solution:
    def valid_anagram(self, s:str, t:str) -> bool :
        s_dict = {}
        t_dict = {}
        for char in s :
            s_dict[char] = s_dict.get(char,0)+1
        for char in t :
            t_dict[char] = t_dict.get(char,0)+1
        print(s_dict , t_dict)
        return s_dict == t_dict
    def valid_anagram1(self, s:str, t:str) -> bool :
        return Counter(s) == Counter(t)
    
ans = Solution()
print(ans.valid_anagram("abdcd" , "abcdd"))
print(ans.valid_anagram1("abdcd" , "abcdd"))


