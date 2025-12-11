# from typing import DefaultDict
# class Solution:
#     def minDistance(self , nums:list[int])-> int :
#         pos = DefaultDict(list)
#         for i , num in enumerate(nums) :
#             pos[num].append(i)
#         print(pos)
#         min_dist = float("inf")
#         for ind_list in pos.values():
#             if len(ind_list)>=3:
#                 for i in range(len(ind_list)-2):
#                     a,b,c = ind_list[0], ind_list[1],ind_list[2]
#                     total = abs(a-b) + abs(b-c) + abs(c-a)
#                     min_dist = min(total,min_dist)
#         return min_dist if min_dist < float("inf") else -1

# ans = Solution()
# print(ans.minDistance([1,2,3,4,5,1,6,7,1,9]))

x = [1,2,3,4]
# y = [num*2 for num in x ]

# map1 = list(map(lambda n:n*2 , x))
# print(map1)
# filter1 = list(filter(lambda n:n%2==0 ,x))
# print(filter1)

# lis1 = (num for num in range(10))
# print(next(lis1))

# for i in lis1 :
#     print(next(lis1))
# class Addition :
#     @staticmethod
#     def add(*args):
#         return sum(args)

# ans = Addition()
# print(ans.add(1,2,3))

class Addition :
    
    def add(self,*args):
        return sum(args)

ans = Addition()
print(ans.add(1,2,3))