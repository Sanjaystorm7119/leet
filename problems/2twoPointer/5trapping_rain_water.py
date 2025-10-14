class Solution:
    def trap(self, height: list[int]) -> int:
        left_max = 0
        right_max = 0
        left_arr = []
        right_arr = []
        most_water = 0
        n = len(height)

        # Build left max array using append
        for i in range(n):
            left_max = max(left_max, height[i])
            left_arr.append(left_max)

        # Build right max array using append (reverse loop)
        for i in range(n - 1, -1, -1):
            right_max = max(right_max, height[i])
            right_arr.append(right_max)
        right_arr.reverse()  # Align order with left_arr and height

        # Compute min of left and right max at each position
        min_left_right = [min(l, r) for l, r in zip(left_arr, right_arr)]

        # Compute total trapped water
        most_water = sum((m - h) if (m - h) > 0 else 0 for m, h in zip(min_left_right, height))

        return most_water

res = Solution()
print(res.trap([1,2,4,5,6,2,3,6,8,9]))
