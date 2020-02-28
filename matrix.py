def twoDlist(l1,l2):
    l3=[[0,0],[0,0]]
    for i in range(len(l1)):
        for j in range(len(l2)):
            for k in range(len(l2)):
                l3[i][j]=l3[i][j]+l1[i][j]*l3[i][j]+l2[i][j]
    print("multiplied array is:- ")
    for x in range(len(l3)):
        for y in range(len(l3)):
            print(l3[x][y],end='')
        print()
l1=[[5,6][8,9]]
l2=[[7,5],[6,7]]
