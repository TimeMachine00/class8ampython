# def hello():
#     print("hello how are you hussain")
# hello()

# def hello(a,b):
#     c=a+b
#     return c
#
#
# a=int(input('enter first value'))
# b=int(input('enter second value'))
# z=hello(a,b)
# print(z)
#
# def fact(n):
#     if n==0:
#         return 1
#     else:
#         for i in range(1,n):
#             n=i*n
#     return n
#
# x=int(input("enter num to find a fact"))
# y=fact(x)
# print(y)

def fib(n):

    a=0
    b=1
    print(a)
    print(b)
    for i in range(1,n-1):
        c=a+b
        a=b
        b=c
        print(c,i)

x=int(input("enter how many fib you require"))
fib(x)

