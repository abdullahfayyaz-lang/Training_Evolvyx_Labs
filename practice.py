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




s1=Student("Abdullah",100,98,78)

s1.print_average()