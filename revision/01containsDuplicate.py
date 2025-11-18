class Solution:
    def __init__(self):
        pass
    def containsDuplicate(self, nums : list[int]) -> bool :
        return len(nums) != len(set(nums))
    
ans = Solution()
print(ans.containsDuplicate([1,2,3]))