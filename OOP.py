## Object oriented programming in python
###class is a blueprint for creating an object
###Constructor all classes have a fuction __init__() which always executed when the class is being initiated

class Student:
    University_name="Fast" #Class Attribute
    ## Class COnstructor
    def __init__(self,fullname,marks):#self is the refrence to the object it self 
        self.name=fullname#object attribute
        self.marks=marks

    ##Class Mehtods
    def hello(self):
        print("Welcome ",self.name)
    
    ##Getters
    def get_name(self):
        return self.fullname 
    def get_marks(self):
        return self.marks
    ##setter
    def set_marks(self,new_marks):
        self.marks=new_marks

    def set_name(self,new_name):
        self.fullname=new_name\
    ##Static metods are the methods that don't use the self parameter(eorks at class level)
    @staticmethod #decorator allows us to wrap func in order to extend the behavior of the wrapped func ,without permanently modifiing it
    def welcome():
        print("welcome")

s0=Student("Cake",99)
s1=Student("Enemy",100)
s2=Student("Owi",89)
s3=Student("Abdullah",89)
# print(s1.name)
# print(s1.University_name)
# print(s3.name)
# print(s2.name)
# print(s0.name)
# s1.hello()
# print(s1.get_marks())
# s1.set_marks(98)
# print(s1.get_marks())
# s1.welcome()


##Abstraction :
###Example
class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("Car started....")
    

car1=Car()
car1.start()#starts only prints required info 

##Encapsulation:Wrapping dta and fuctions into a single unit
###Example

class Car:
    def __init__(self):
        self.acc=False
        self.brk=False
        self.clutch=False

    def start(self):
        self.clutch=True
        self.acc=True
        print("Car started....")