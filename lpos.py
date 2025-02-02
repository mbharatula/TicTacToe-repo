import variables as v

def lpos():
    x=v.matrix[0]
    if int(x[0])==1:
        for i in range (0,4):
            if i+1==int(x[1]):
                v.row1[i]='X'
    if int(x[0])==2:
        for i in range (0,4):
            if i+1==int(x[1]):
                v.row2[i]='X'
    if int(x[0])==3:
        for i in range (0,4):
            if i+1==int(x[1]):
                v.row3[i]='X'
    print(v.row1)
    print(v.row2)
    print(v.row3)