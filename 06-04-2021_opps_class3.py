class A:
    def __init__(self):
        print("in class A init")

    def hai(self):
        print('hai')
class B():
    def __init__(self):
        print("in class B init")
        # super().__init__()

    def hello(self):
        print('hello')

class C(B,A):
    def wish(self):
        print('good evening')




a=A()
b=B()
c=C()

        