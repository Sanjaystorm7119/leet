class Solution:
    def mostwatercontainer(self , heights:list[int])->int:
        l = 0
        r = len(heights)-1
        max_water = 0
        while l < r :
            max_water = max(max_water,min(heights[l],heights[r])*(r-l))
            if heights[l] > heights[r]:
                r -= 1
            else :
                l += 1
        return max_water
        
ans =  Solution()
print(ans.mostwatercontainer([1,2,6,7,5,4,2,1]))
            
