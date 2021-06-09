# x=lambda a,b:a+b
# y=x(3,4)
# print(y)
#
# def sum(a,b):
#     c=a+b
#     print(c)
# sum(4,5)
from functools import reduce
a=[1,2,3,4,5,6,7,8,9,10,11,12]
odds=list(filter(lambda n:n%2!=0,a))
print(odds)
triple=list(map(lambda n:n*3, odds ))
print(triple)
add=reduce(lambda c,d:c+d, triple)
print(add)

