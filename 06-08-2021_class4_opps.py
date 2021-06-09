#
# class hussain2:
#
#     def myqualities(self):
#         print("i play cricket")
#         print('i watch sci-fi movies')
#
#
#
# class hussain3:
#     def myqualities(self):
#         print("i play cricket")
#         print('i watch sci-fi movies')
#         print('he is not genuine')
#
#
# class hussain:
#
#     def quality(self,details):
#
#         details.myqualities()
#
# a=hussain2()
# b=hussain3()
#
# c=hussain()
#
# c.quality(a)



class student:
    def __init__(self,maths,commerce):
        self.maths=maths
        self.commerce=commerce


    # def result(self):
    #
    #     print(self.maths+self.commerce)

    def __add__(self, other):
        a=self.maths+other.maths
        b=self.commerce+other.commerce
        c=student(a,b)
        return c
    def __gt__(self, other):
        if self.maths>other.maths:
            return True
        else:
            return False


s1=student(20,32)
s2=student(12,15)

s3=s1+s2
print(s3.maths,s3.commerce)
s4=s1<s2
print(s4)