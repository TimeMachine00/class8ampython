class fiveStarHotel:

    def __init__(self):
        self.veg=['chapati','rice','curd rice','tomoto rice']
        self.nonveg=['mutton biryani','chicken biryani','kabab','grilled chicken']
        self.deserts=['pepsi','thums up','ice cream','gulab jamun']

    def order(self):
        """this is ordering system"""
        waiter1=input('sir what do you want')
        if waiter1 =='veg':
            waiter2=input('choose is ur item from veg menu')
            for i in self.veg:
                if i==waiter2:
                    print(f"sir this your food  {i}")
                    break

            else:
                print('food not available')
        elif waiter1 =='nonveg':
            waiter3=input('choose your item from non veg menu')
            for j in self.nonveg:
                if j==waiter3:
                    print(f"sir this your non veg{j}")
                    break
            else:
                print("food not available")
        elif waiter1=='deserts':
            waiter4=input("choose your dessert")
            for k in self.deserts:
                if k==waiter4:
                    print(f"sir this is ur desert item {k}")
                    break


            else:
                print('item not available')
        else:
            if waiter1=='not required':
                print('thank you')
class orderAgain(fiveStarHotel):

    pass
if __name__=='__main__':
    order1=fiveStarHotel()
    # order2=fiveStarHotel()
    # order2=orderAgain()

    for l in range(1,4):

        order1.order()


    # order2.order()
    # order2.order()
