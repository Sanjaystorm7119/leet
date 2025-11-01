class Solution:
    def singleNonDuplicate(self, nums: list[int]) -> int:
        # freq_dict = {}
        # for num in nums:
        #     freq_dict[num] = freq_dict.get(num,0)+1

        # for num,count in freq_dict.items():
        #     if count == 1:
        #         return num

        l = 0
        r = len(nums)-1
        while l<=r :
            mid = (l+r)//2
            if ((mid-1<0 or nums[mid] != nums[mid-1]) and (mid+1==len(nums) or nums[mid] !=  nums[mid+1])):
                return nums[mid]
            leftsize = mid-1 if nums[mid-1] == nums[mid] else mid
            if leftsize %2 :
                r = mid-1
            else :
                l = mid+1
ans = Solution()
print(ans.singleNonDuplicate([1,1,2,2,3,4,4,5,5]))