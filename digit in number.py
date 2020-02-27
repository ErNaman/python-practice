def count(num):
    count=0
    while num>0:
        num=num//10
        count=count+1
    print("number of digits in number is/are:- ",count)
x=int(input(print("enter the number:- ")))
count(x)
