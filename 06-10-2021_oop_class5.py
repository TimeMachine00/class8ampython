a=int(input("enter first number"))
b=int(input("enter second number"))

try:
    print('open')
    c=a/b
    print(c)

except Exception as e:
    print(e)


finally:
    print('close')