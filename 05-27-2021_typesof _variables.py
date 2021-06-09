# a=10
#
# def loc():
#     # global a
#     x=globals()['a']
#     globals()['a']=20
#
#     print(id(x))
#     a=2
#     print('inside function',a)
# print(id(a))
# print('outside function',a)
# loc()
# print('outside function',a)


# argument types

def info(**a):
    for i,j in a.items():
        print(i,j)

info(name='hussain',age=30,city='kurnool',num=5555)
