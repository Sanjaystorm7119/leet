class Solution:
    def two_sum(self, nums : list[int], target : int) -> list[int]:
        compliment_dict = {}
        for i,num in enumerate(nums):
            compliment = target - num
            if compliment in compliment_dict :
                return [compliment_dict[compliment],i]
            else :
                compliment_dict[num] = i
        return []
    
ans = Solution()
print(ans.two_sum([1,2,4,5],5))
        