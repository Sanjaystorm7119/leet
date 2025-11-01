class Solution:
    def bestTime(self, prices : list[int])->int :
        left = 0
        right = 1
        maxP = 0
        while right < len(prices) :
            if prices[left] < prices[right]:
                profit = prices[right]-prices[left]
                maxP = max(maxP , profit)
            else :
                left = right
            right+=1
        return maxP
    
ans = Solution()
print(ans.bestTime([2,1,2,3,0,4,6,3,4]))
