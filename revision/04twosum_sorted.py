class Solution:
    def two_sum_sorted(self , nums : list[int], target) -> list[int]:
        l , r = 0 , len(nums)-1
        while l < r :
            mid = (l+r)//2
            if nums[l] + nums[r] == target :
                return [l,r]
            elif nums[l] + nums[r] > target :
                r -= 1
            else :
                l += 1
        return []

ans = Solution()
print(ans.two_sum_sorted([1,2,3,4,5],10))