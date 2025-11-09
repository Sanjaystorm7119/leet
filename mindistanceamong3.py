from typing import DefaultDict
class Solution:
    def minimumDistance(self, nums: list[int]) -> int:
        positions = DefaultDict(list)
        for i, num in enumerate(nums):
            positions[num].append(i)
        print(positions)
        min_dist = float('inf')
        for idx_list in positions.values():
            if len(idx_list) >= 3:
                for i in range(len(idx_list) - 2):
                    a, b, c = idx_list[i], idx_list[i+1], idx_list[i+2]
                    print(f"a :{a} , b:{b}, c :{c}")
                    dist = abs(a - b) + abs(b - c) + abs(c - a)
                    min_dist = min(min_dist, dist)

        return min_dist if min_dist < float('inf') else -1
    
ans = Solution()
print(ans.minimumDistance([1,4,3,1,5,9,1,2,3]))

