class Solution:
    def trap(self, height: list[int]) -> int:
        left , right = 0 , len(height)-1
        left_max , right_max = height[left] , height[right]
        max_water = 0
        while left < right :
            #check for lower bound
            if height[left] < height[right] :
                max_water += left_max - height[left]
                left += 1
                left_max = max(left_max , height[left])
            else :
                max_water += right_max - height[right]
                right -= 1
                right_max = max(right_max , height[right])
        return max_water

res = Solution()
print(res.trap([1,2,4,5,6,2,3,6,8,9]))

                        