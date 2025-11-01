class Solution:
    def carfleet(self , position:list[int], speed: list[int], target:int)-> int :
        # pos_speed_pair = [[p,s] for p,s in zip(position,speed)]
        # # sorting and reversing based on position
        # pos_speed_pair.sort(reverse=True)
        pos_speed_pair = sorted(zip(position,speed), reverse=True)
        print(pos_speed_pair)
        stack = []
        for p,s in pos_speed_pair:
            stack.append((target-p)/s)
            if len(stack) >=2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)
ans= Solution()
print(ans.carfleet([4,5,7],[3,5,2],15))
