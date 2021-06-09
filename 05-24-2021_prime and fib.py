# # n=int(input("enter number to check"))
# #
# #
# # for i in range(2,n):
# #     if n%i==0:
# #         print("not a prime")
# #         break
# # else:
# #     print("it is a prime")
#
# n=int(input("enter number to check"))
#
#
# for i in range(2,n):
#     if n*1==n and n%i==0:
#         print("it is not  prime")
#         break
#
# else:
#     print("it is prime")

n=int(input('how many fib number you want'))
a=0
b=1
print(a)
print(b)

for i in range(1,n-1):
    c=a+b
    a=b
    b=c
    print(c,i)



