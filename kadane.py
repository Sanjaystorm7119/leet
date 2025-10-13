def maxsubarray(nums : list):
    max_sum = float('-inf')
    current_sum = 0
    
    for i in range(len(nums)):
        current_sum += nums[i]
        max_sum = max(max_sum , current_sum)

        if current_sum < 0 :
            current_sum = 0
    print(max_sum)

maxsubarray([-1,-2,-3,-4])
