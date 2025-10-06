name="Abdullah Fayyaz"
age=22
speed=19.23
Software_Engineer=True
#data types
##string, integer, float, boolean, None
#Python is case sensitive language
print("My name is",name,"and my age is",age)
print("My speed is",speed,"km/h")
print("I am a Software Engineer:",Software_Engineer)
print(type(name))
print(type(age))
print(type(speed))
print(type(Software_Engineer))


a=10
b=500
sum=a+b
print("The sum of a and b is:",sum)


#operators in python
##Arithmetic (+-/*%**)
a=10
b=500
sum=a+b
dif=a-b
mul=a*b
div=b/a
mod=b%a
print("a+b",sum)
print("a-b",dif)
print("a*b",mul)
print("b/a",div)
print("b%a",mod)
print("b^a",b**a)

##Comparison (==,!=,<,>,<=,>=)
print(a==b)
print(a!=b)
print(a<b)
print(a>b)
print(a<=b)
print(a>=b)

##Assignment (=,+=,-=,*=,)
num=10
print(num)
num+=10
print(num)
num-=1
print(num)
num*=10
print(num)
num/=2
print(num)
num**=2
print(num)
num%=2
print(num)


##Logical Operator(And,Or,Not)

val1=True
val2=False

print(val1 and val2)
print(val1 or val2)
print(not val1)


#Type Converstion

a=int("2")
b=1
c=str(b)
d="ok"
sum=a+b
print(sum)
print(c+d)

#Input 

# name=input("Enter yout name : ")
# age=int(input("Enter yout age :"))
# weight=float(input("Enter your weight :"))
# print(name,age,weight)


##Control Structure(Loops)
#While->
count =100
while count >=1:
    print(count)
    count-=1

i=1
while i<=10:
    print("3 x ",i," = ",3*i)
    i+=1

arr=[1,2,3,4,5,6,7,8,9,10]
length=len(arr)
i=0
while i<length:
    print(arr[i])
    i+=1

x=5
i=0
while arr[i]!=x:
    i+=1

print("x is on the ",i," th index of the list.")

###Break is used to terminate a loop .
###Conutine only terminates the current cycle of the loop and continue from next one.

i=0
while i<=5:
    if(i == 3):
        i+=1
        continue
    print(i)
    i+=1
print("---------------------------------")
i=0
while i<=5:
    if(i == 3):
        i+=1
        break
    print(i)
    i+=1
print("---------------------------------")
##For loops
arr=[1,2,3,4,5,6,7,8,9,10]

for num in arr:
    print(num)
print("---------------------------------")
tup =(1,2,3,4,5)

for num in tup:
    print(num)


# # List example
# fruits = ["apple", "banana", "cherry"]
# fruits.append("orange")  # Works fine
# Slower because of mutability (requires more memory and processing).
# Lists are not hahable
# print(fruits)  # ['apple', 'banana', 'cherry', 'orange']

# # Tuple example
# colors = ("red", "green", "blue")
# colors.append("yellow")  # ❌ AttributeError
# Faster due to immutability and smaller memory footprint.
# tuples are ot hahable
# print(colors)  # ('red', 'green', 'blue')


print("---------------------------------")

str="Enemy"

for char in str:
    print(char)

##Else with for loop
print("---------------------------------")
for char in str:
    if(char == "e"):
        break
    else :
        print(char)
else:
    print("End")

print("---------------------------------")
for char in str:
    if(char == "e"):
        break
    else :
        print(char)

print("End")
print("---------------------------------")
tup =(1,2,3,4,5)
x=3

for ele in tup:
    if(x==ele):
        print("x found")
        break
    else:
        print("finding")

## Range function returns a sequence of numbers , starting from 0 by default and increment by 1 by default and stops before a specific number
### range(start?,stop,step?)
print("---------------------------------")
for el in range(5):
    print(el)
print("---------------------------------")
for el in range(1,7):
    print(el)
print("---------------------------------")
for el in range(0,11,2):
    print(el)

##Pass statement is a null statement that does nothing.its just a placeholder for future code

for i in range(5):
    pass 

print("Some useful work")