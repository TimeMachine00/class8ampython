# class employee:
#
#     company="micro soft"
#
#     def __init__(self,name,id):
#         self.name=name
#         self.id=id
#
#     def details(self):
#
#         print(self.name,self.id)
#
#
# employee.company='apple'
# emp1=employee('huss','55555')
# emp2=employee('raj','33333333333')
# emp1.company='nokia'
#
#
# print(emp1.company,emp2.company)
#
# emp1.details()
# emp2.details()


# class employee:
#
#     company='microsoft'
#
#     def __init__(self,name,id):
#
#         self.name=name
#         self.id=id
#
#     def details(self):
#
#         print(self.name,self.id)
#
#     @classmethod
#     def companyname(cls):
#         cls.company='apple'
#         print(cls.company)
#
#     @staticmethod
#     def greet():
#         print("good morning")
#
#
# emp1=employee('huss','333333')
# emp1.details()
#
# emp1.companyname()
# emp1.greet()

class fact:

    def __init__(self,n):

        self.n=int(input('enter a number'))

    def facval(self):

        f=1

        for i in range(1,self.n+1):
            f=f*i

        print(f)

a=fact(None)
a.facval()


