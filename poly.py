class Complex:
    def __init__(self,real,img):
        self.real=real
        self.img=img

    def showNumber(self):
        print(self.real,"i +",self.img,"j")
    ##opertaor overloading
    ###Dunder Functions
    def __add__(self,num2):
        newReal=self.real + num2.real
        newImg=self.img + num2.img
        return Complex(newReal,newImg)
    def __sub__ (self,num2):
        newReal=self.real - num2.real
        newImg=self.img - num2.img
        return Complex(newReal,newImg)

    def __mul__ (self,num2):
        newReal=self.real * num2.real
        newImg=self.img * num2.img
        return Complex(newReal,newImg)


num1=Complex(1,3)
num2=Complex(4,6)

num1.showNumber()
num2.showNumber()

num3=num1 + num2
num4=num1 - num2
num5=num1 * num2
num3.showNumber()
num4.showNumber()
num5.showNumber()


class Circle:
    def __init__(self,radius):
        self.radius=radius

    def area(self):
        return (22/7)*self.radius**2
    
    def perimeter(self):
        return 2*(22/7)*self.radius


c1=Circle(21)
print(c1.area())
print(c1.perimeter())


class Employee:
    def __init__(self,role,dept,salary):
        self.role=role
        self.dept=dept
        self.salary=salary
    
    def showDetails(self):
        print("Role :",self.role)
        print("Department :",self.dept)
        print("Salary :",self.salary)

class Engineer(Employee):
    def __init__(self,name,age,role,dept,salary):
        super().__init__(role,dept,salary)
        self.name=name
        self.age=age

        
    def showDetails(self):
        print("Name :",self.name)
        print("Age :",self.age)
        super().showDetails()

emp1=Employee("ASE","Engineering",5000000000000000000000000000000000)
##emp1.showDetails()
eng1=Engineer("Abdullah Fayyaz",22,"ASE","Spftware Development","5000000000000000000000000")
eng1.showDetails()