##print numbers from 1 to 100 without using loop

def PrintNum(num):
    if num>0:
        PrintNum(num-1)
        print(num,end=" ")
PrintNum(100)
##print(r)
##r=PrintNum(100)
#  change done by subham
# for github
