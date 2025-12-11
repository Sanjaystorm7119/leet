from typing import DefaultDict,List
class Solution:
    def countElements(self, nums: List[int], k: int) -> int:
        num_to_diff = DefaultDict(list)
        for i,num in enumerate(nums) :
            num_to_diff[num].append(nums[i] - num)
        return num_to_diff
    
ans = Solution()
print(ans.countElements([1,2,3,4],1))