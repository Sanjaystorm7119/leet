from typing import List
class Solution:
    def two_sum_unsorted(self , nums:List[int], target:int) -> List[int]:
        compliment_dict = {}
        for ind , num in enumerate(nums) :
            compliment = target - num
            if compliment in compliment_dict:
                return [compliment_dict[compliment],ind]
            else :
                compliment_dict[num] = ind
        return []
    
    def two_sum_sorted(self , nums:List[int], target:int) -> List[int]:
        l , r = 0, len(nums)-1
        while l < r :
            if nums[l] + nums [r] == target :
                return [l,r]
            elif nums[l] + nums [r] > target :
                r -= 1
            else :
                l += 1
        return []
    
ans = Solution()
print(ans.two_sum_unsorted([1,1,3,2,5],5))
print(ans.two_sum_sorted([1,1,2,3,5],5))

