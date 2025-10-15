class Solution:
    def dailyTemp(self , temearatures : list[int])->list[int]:
        res = [0]*len(temearatures)
        stack = [] #pair[temp,idx]

        for ind,temp in enumerate(temearatures):
            while stack and temp > stack[-1][0]:
                _ , stackInd = stack.pop()
                res[stackInd] = (ind-stackInd)
            stack.append([temp,ind])
        return res
ans = Solution()
print(ans.dailyTemp([10,20,30]))      
