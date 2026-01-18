
class Solution:
    def insertion_sort(self,arr):
        for i in range(1,len(arr)):
            j = i-1
            while j >= 0 and arr[i] < arr[j]:
                arr[j+1] = arr[j]
                j-=1
            arr[j+1] = arr[i] 
        return arr
arr= [10,30,20,40,50,5]
ans = Solution()
print(ans.insertion_sort(arr))