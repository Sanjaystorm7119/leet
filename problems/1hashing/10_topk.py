class Solution:
    def topK(self , nums : list[int], k: int) -> list[int] :
        num_to_freq = {}
        for num in nums :
            num_to_freq[num] = num_to_freq.get(num , 0)+1

        in_list = [[] for i in range(len(nums)+1)]

        for num , freq in num_to_freq.items():
            in_list[freq].append(num)

        print(in_list)
        res = []
        for i in range(len(in_list)-1,-1,-1):
            for num in in_list[i]:
                res.append(num)
                if len(res) == k :
                    return res


ans = Solution()
print(ans.topK([1,1,2,3,4,5,4],5))