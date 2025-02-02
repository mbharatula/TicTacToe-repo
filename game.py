import variables as v



def gameX(m,n):
    if int(m[0]) == 1:
        for i in range (0,3):
            if i+1 == int(m[1]):
                v.row1[i]='X'
            else:
                pass
    if int(m[0]) == 2:
        for i in range (0,3):
            if i+1 == int(m[1]):
                v.row2[i]='X'
            else:
                pass
    if int(m[0]) == 3:
        for i in range (0,3):
            if i+1 == int(m[1]):
                v.row3[i]='X'
            else:
                pass
    if int(n[0]) == 1:
        for i in range (0,3):
            if i+1 == int(n[1]):
                v.row1[i]='O'
            else:
                pass
    if int(n[0]) == 2:
        for i in range (0,3):
            if i+1 == int(n[1]):
                v.row2[i]='O'
            else:
                pass
    if int(n[0]) == 3:
        for i in range (0,3):
            if i+1 == int(n[1]):
                v.row3[i]='O'
            else:
                pass
    print(v.row1)
    print(v.row2)
    print(v.row3)







