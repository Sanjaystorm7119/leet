# def count(num:int)->int:
#     if num==0 :
#         return
#     count(num-1)
#     print(num)


# count(10)

#fact

def fact(n):
    if n == 1:
        return 1
    else :
        return n*fact(n-1)

print(fact(3))