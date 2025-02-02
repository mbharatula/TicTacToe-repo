import variables as v



for i in range (0,3):
        v.row1.append('_')
for i in range (0,3):
        v.row2.append('_')
for i in range (0,3):
        v.row3.append('_')
        
def intialise():
    print(v.row1)
    print(v.row2)
    print(v.row2)

for i in range (0,3):
        v.row1_n.append('_')
for i in range (0,3):
        v.row2_n.append('_')
for i in range (0,3):
        v.row3_n.append('_')

for i in range (0,3):#0,1,2
    v.row1_n[i]=11+i
for i in range (0,3):
    v.row2_n[i]=21+i
for i in range (0,3):
    v.row3_n[i]=31+i

def intialise1():
    print(v.row1_n)
    print(v.row2_n)
    print(v.row3_n)
