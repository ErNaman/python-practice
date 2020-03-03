import sys
l1 = ['a', 0, 9]
for x in l1:
    try:
        print("The entry is", x)
        r = 1/int(x)
        break
    except:
        print("Oops!",sys.exc_info()[0],"occured.")
        print("Next entry.")
        print()
print("The reciprocal of",x,"is",r)
