from typing import List
class Solution:
    def duplicates(self , nums : List[int]) -> bool :
        num_freq_dict = {}
        for num in nums :
            num_freq_dict[num] = num_freq_dict.get(num,0)+1
        
        print(num_freq_dict)
        print([key for key,value in num_freq_dict.items() if value > 1])
        return any(value > 1 for value in num_freq_dict.values())
    
    
    def duplicates1(self , nums : List[int]) -> bool :
        return len(nums) != len(set(nums))
    
ans = Solution()
print(ans.duplicates([1,2,3,4,5,5,5,6,6,7,1]))
print(ans.duplicates1([1,2,3,4,5,5,5,6,6,7,1]))

