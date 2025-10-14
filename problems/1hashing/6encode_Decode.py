# # class Codec:
# #     def encode(self, strs: list[str]) -> str:
# #         """Encodes a list of strings to a single string.
# #         """
# #         res = []
# #         for word in strs:
# #             res.append(str(len(word))+"#"+word)
# #         return "".join(res)

# #     def decode(self, s: str) -> list[str]:
# #         """Decodes a single string to a list of strings.
# #         """
# #         res,i = [] , 0
# #         while i < len(s):
# #             j = i
# #             while s[j]!="#" :
# #                 j+=1
# #             length = int(s[i:j])
# #             print(length)
# #             res.append(s[j+1 : j+1+length])
# #             i = j+1+length

# #         return res
# # ans = Codec()
# # print(ans.encode(["hello","worlds"]))
# # print(ans.decode("5#hello6#worlds"))

# # Your Codec object will be instantiated and called as such:
# # codec = Codec()
# # codec.decode(codec.encode(strs))

# class Codec:
#     def encode(self,words :list[str]) -> str :
#         res = []
#         for word in words:
#             res.append(str(len(word))+"#"+word)
#         return "".join(res)
    
#     def decode(self , s: str) -> list[str] :
#         res = []
#         i = 0
#         while i < len(s):
#             j = i
#             while s[j] != "#" :
#                 j += 1
#             length = int(s[i:j])
#             res.append(s[j+1:j+1+length])
#             i= j+1+length
#         return res

# ans = Codec()
# print(ans.encode(["hello","jay"]))
# print(ans.decode('5#hello3#jay'))

# # ans = Codec()
# # print(ans.encode(["hello","jay"]))



# # i
# #   j   
# # 5 # h e l l o 3 # j a y
# # 0 1 2 3 4 5 6 7 8 9 10 11
# # "5" => 5

# # h e l l o => j+1 : j+1+length 
# # i = j+1+length => (0+1+5+1)=>7

# # i = 0
# # j = 1
# # 0:1 => 3
# # j+1 
# # j+1+len
# # [9:12] jay


class Codec:
    def encode(self , words :list[str]) -> str :
        res = []
        for word in words:
            res.append(str(len(word)) + "#"+word)
        return "".join(res)
    
    def decode(self , s:str) -> list[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != "#":
                j += 1
            length = int(s[i:j])
            res.append(s[j+1:j+1+length])
            i = j+1+length
        return res
ans = Codec()
print(ans.encode(["hello","jay"]))
print(ans.decode('5#hello3#jay'))
    
