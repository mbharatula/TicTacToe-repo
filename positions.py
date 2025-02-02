import variables as v
import random

upos=''
cpos=''


def userPosition():
    global upos
    upos=input("Enter where you want to mark...    ")      
     

def compPosition():
    global cpos
    cpos=random.choice(v.matrix)






