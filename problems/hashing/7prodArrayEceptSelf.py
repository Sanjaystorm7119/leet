class Solution:
    def prodArrayExceptSelf(self , nums : list[int]):
        left_mul = 1
        right_mul = 1
        res = [1]*len(nums)
        # right_Arr = [1]*len(nums)

        for i in range(len(nums)):
            res[i] *= left_mul
            left_mul *= nums[i]
        print(res)
        for i in range(len(nums)-1,-1,-1):
            res[i] *= right_mul
            right_mul *= nums[i]
        print(res)
        return res
       
        
res = Solution()
print(res.prodArrayExceptSelf([1,2,3,4]))


 