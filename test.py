from typing import DefaultDict
class Solution:
    def minDistance(self , nums:list[int])-> int :
        pos = DefaultDict(list)
        for i , num in enumerate(nums) :
            pos[num].append(i)
        print(pos)
        min_dist = float("inf")
        for ind_list in pos.values():
            if len(ind_list)>=3:
                for i in range(len(ind_list)-2):
                    a,b,c = ind_list[0], ind_list[1],ind_list[2]
                    total = abs(a-b) + abs(b-c) + abs(c-a)
                    min_dist = min(total,min_dist)
        return min_dist if min_dist < float("inf") else -1

ans = Solution()
print(ans.minDistance([1,2,3,4,5,1,6,7,1,9]))
