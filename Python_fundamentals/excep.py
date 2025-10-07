#Exception handling
try:
    a=int(input("enter a number : "))
    for i in range(1,11):
        print(int(a),"x",i,"=",int(a)*i)
except ValueError:
    print("Input is not an integer")


print("done")
print("ok")