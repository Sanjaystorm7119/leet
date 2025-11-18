# from typing import DefaultDict
# class Solution:
#     def top_k_frequent(self , nums : list[int] , k : int) -> list[int] :
#         num_to_freq_dict = DefaultDict(list[int])
#         for i , num in enumerate(nums):
#             num_to_freq_dict[num].append(i)
#         # num_buckets = [[]]*(len(set(nums))+1) #dont create like this cuz they will all  have same ref

#         num_buckets = [[] for _ in range(len(nums)+1)]
#         for num , indices in num_to_freq_dict.items():
#             freq =  len(indices)
#             num_buckets[freq].append(num)

#         res = []
#         for freq in range(len(num_buckets)-1,-1,-1):
#             for num in num_buckets[freq]:
#                 res.append(num)

#                 if len(res)==k:
#                     return res        
#         return res

# ans = Solution()
# print(ans.top_k_frequent([1,2,1,3,2,2,4],2))


class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        freq_dict = {}
        for num in nums:
            freq_dict[num] = freq_dict.get(num,0)+1

        buckets = [[] for _ in range(len(nums)+1)]
        for num,count in freq_dict.items():
            buckets[count].append(num)
        res = []
        for i in range(len(buckets)-1,0,-1):
            for num in buckets[i]:
                res.append(num)
                if len(res) == k :
                    return res
ans = Solution()
print(ans.topKFrequent([1,2,1,3,2,2,4],2))

