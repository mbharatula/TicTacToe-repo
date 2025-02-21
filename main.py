import game as g
import initialise as i
import positions as p
import variables as v
import lpos as l
import wincheck as w

print("WELCOME TO TIC-TAC-TOE....")
print("AS RULES STATE X STARTS FIRST...")
#INTIALISING
i.intialise()
print("For Convinience Let Us Assign Numbers as Follows..")
i.intialise1()

gameover=False
userChoice=input("Enter The Symbol You Want To Choose..\"X\" or \"O\"\n").lower()
while len(v.matrix)>1:
    if userChoice=='x':
        p.userPosition()
        if p.upos in  v.matrix:
            v.matrix.remove(p.upos)
            p.compPosition()
            v.matrix.remove(p.cpos)
            print(f"I Choose {p.cpos}")
            g.gameX(m=p.upos,n=p.cpos)
            if w.gameOverX():
                print("You Won The Game!!")
                gameover=True
                break
            if w.gameOverO():
                print("It is my Day Try Again Later!")
                gameover=True
                break

        elif p.upos not in v.matrix:
            print("Oops! You Entered A Wrong Position Try Again")
            print("The Positions left are...")
            for i in v.matrix:
                print(i,end=' ')
        print()

    if userChoice=='o':
        p.compPosition()
        print(f"I Choose Position {p.cpos}")
        p.userPosition()
        if p.upos in v.matrix:
            v.matrix.remove(p.upos)
            v.matrix.remove(p.cpos)
            g.gameX(m=p.cpos,n=p.upos)
            if w.gameOverO():
                print("You Won The Game!!")
                gameover=True
                break
            if w.gameOverX():
                print("It is my Day Try Again Later!")
                gameover=True
                break

        elif p.upos not in v.matrix:
            
            print("Oops! You Entered A Wrong Position Try Again")
            print("The Positions left are...")
            for i in v.matrix:
                print(i,end=' ')
            print()
            print("SO,LET ME MARK IT AGAIN")

if (len(v.matrix)==1):
    if(not gameover):
        if(userChoice=='x'):
            print(f"The Only Position Left For You is {v.matrix[0]}\n Let Me Mark it")
            l.lpos()
            if w.gameOverX():
                print("You Won The Game!!")
            if w.gameOverO():
                print("It is my Day Try Again Later!")
              
        if(userChoice=='o'):
            print(f"The Only Position Left For Me is {v.matrix[0]}\n Let Me Mark it")
            l.lpos()
            if w.gameOverO():
                print("You Won The Game!!")
            if w.gameOverX():
                print("It is my Day Try Again Later!")
    
