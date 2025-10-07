# Open,read& close file
import os
##f=open("file_name","mode")
###r open for reading
###w open for writing(this over writies)
###x create a new file and open it for writing
###a open for writing , appending at the end of exixting itmes in file
###b binary mode
###t text mode
###+ open a disk file for updating (reading & writing)
### r+ read and write no truncate
### w+ read and write  truncate
### a+ read and write  appends in the end
f=open("demo.txt","r")
data=f.readline()


# print(data)
# data=f.readline()
# print(data)
# ## read reads whole file   
# ## readline reads one line at a time.
# f=open("sample.txt","a+")

# f.write("abc")
# f.close

# with open("sample.txt","r") as f:
#     data=f.read()
#     print(data)

# with open("sample.txt","a") as f:
#     f.write("\n abcabacabaa")
#     f.close()

#deleting file 
## os module is use to delete files.
# os.remove("sample.txt")
def check_for_word(word):
    with open("sample.txt","r") as f:
        data=f.read()
        if(data.find(word) !=-1):
            print("found")
        else:
            print("not found")

def check_for_line(word):
    data=True
    line_no=1
    with open("sample.txt","r") as f:
        while data:
            data=f.readline()
            if(word in data):
                print(line_no)
            line_no+=1
    return -1

    
# with open("sample.txt","a") as f:
#     f.write("Hi everyone\nwe are learning file i/o\nusing java\ni like programing in java")
#     f.close()

# with open("sample.txt","r") as f:
#     data=f.read()
#     new_data=data.replace("java","python")

# with open("sample.txt","w") as f:
#     f.write(new_data)
#     f.close()



check_for_word("learning")
check_for_line("learning")


with open("sample.txt","r") as f:
    data=f.read()
    count=0
    nums=(data.split(","))
    for num in nums:
        if(int(num)%2==0):
            print(num)
            count+=1
        
    print(count)
    