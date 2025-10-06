#inheritance->one class (child) derives the properties & methods of another class(parent)
##types->
###Single
###Multi-lvl
###Multiplie
##super method is used to access methods of parent class  
# class Car:
#     @staticmethod
#     def start():
#         print("car started......")
#     @staticmethod
#     def stop():
#         print("car stoped......")

# class toyotaCar(Car):
#     def __init__(self,name):
#         self.brand=name

# class Fortuner(toyotaCar):
#     def __init__(self,_type):
#         self.type=_type

# car1=toyotaCar("Supura")
#, car2=Fortuner("Petrol")

# car1.start()
# car1.stop()
# car2.start()
# car2.stop()


class Car:
    def __init__(self,_type):
        self.type=_type
    @staticmethod
    def start():
        print("car started......")
    @staticmethod
    def stop():
        print("car stoped......")

class toyotaCar(Car):
    def __init__(self,name,_type):
        super().__init__(_type)
        self.brand=name


car1=toyotaCar("Supra","Beast")
print(car1.type)

##class method is bound to the class & receives the class as an implicit first argument.
###note - static method can't access or modifiy class state & generally for utility



class Person:
    name="anonymous"

    # def changeName(self,name):
    #     self.name=name
    @classmethod
    def changeName(cls,name):
        cls.name=name


p1=Person()
p1.changeName("Enemy")
print(p1.name)
print(Person.name)

##property decorator is used on any method in the class to use the method as a property

class Student:
    def __init__(self,phy,chem,math):
        self.phy=phy
        self.chem=chem
        self.math=math
      
      
    @property
    def percentage(self):
       return str((self.phy +self.chem+self.math)/3)+"%"


stu1=Student(98,98,98)
print(stu1.percentage)
stu1.phy=86
print(stu1.phy)
print(stu1.percentage)
