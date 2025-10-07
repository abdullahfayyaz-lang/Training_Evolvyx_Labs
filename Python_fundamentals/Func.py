#Function -> Block of statements to perform a specific task.

def cal_sum(a,b):
    return a+b

sum=cal_sum(10,2382)
print(sum)

def print_list(arr):
    for ele in arr:
        print(ele,end=" ")


arr=[1,2,3,4,5]
print_list(arr)


def fac(n):
    fact=1
    for i in range(1,n+1):
        fact=fact*i  
    print(fact)



fac(10)
fac(10)