class Solution:
    def intToRoman(self, num: int) -> str:
        dictRtoN = {
            1000: "M", 900: "CM", 500: "D", 400: "CD",
            100: "C", 90: "XC", 50: "L", 40: "XL",
            10: "X", 9: "IX", 5: "V", 4: "IV", 1: "I"
        }
        
        roman = ""
        # Iterate through the sorted keys in descending order
        for value in (dictRtoN.keys()):
            while num >= value:
                roman += dictRtoN[value]  # add Roman symbol
                num -= value              # subtract the value from the number
        
        return roman

ans = Solution()
print(ans.intToRoman(400))