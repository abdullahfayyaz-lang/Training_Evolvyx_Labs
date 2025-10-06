class Student:
    def __init__(self,name,marks_1,marks_2,marks_3):
        self.name=name
        self.marks_1=marks_1
        self.marks_2=marks_2
        self.marks_3=marks_3
    
    def print_average(self):
        sum=self.marks_1+self.marks_2+self.marks_3
        avg=sum/3
        print(self.name,"your average marks are :",avg)




# s1=Student("Abdullah",100,98,78)

# s1.print_average()


class Account:
    def __init__(self,acc_no,balance):
        self.acc_no=acc_no
        self.balance=balance

    def print_balance(self):
        print("Your acount blance :",self.balance)

    def credit(self,amount):
        self.balance+=amount

    def debit(self,amount):
        self.balance-=amount


a1=Account(1,10000)
a1.print_balance()

a1.credit(1000)
a1.print_balance()
a1.debit(1000)
a1.print_balance()