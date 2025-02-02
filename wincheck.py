import variables as v


def gameOverX():
    
    if v.row1[0]==v.row1[1]==v.row1[2]=='X':
        return True
    elif v.row2[0]==v.row2[1]==v.row2[2]=='X':
        return True
    elif v.row3[0]==v.row3[1]==v.row3[2]=='X':
        return True
    elif v.row1[0]==v.row2[0]==v.row3[0]=='X':
        return True
    elif v.row1[1]==v.row2[1]==v.row3[1]=='X':
        return True
    elif v.row1[2]==v.row2[2]==v.row3[2]=='X':
        return True
    elif v.row1[0]==v.row2[1]==v.row3[2]=='X':
        return True
    elif v.row1[2]==v.row2[1]==v.row3[0]=='X':
        return True
    else:
        return False
    

def gameOverO():
    
    if v.row1[0]==v.row1[1]==v.row1[2]=='O':
        return True
    elif v.row2[0]==v.row2[1]==v.row2[2]=='O':
        return True
    elif v.row3[0]==v.row3[1]==v.row3[2]=='O':
        return True
    elif v.row1[0]==v.row2[0]==v.row3[0]=='O':
        return True
    elif v.row1[1]==v.row2[1]==v.row3[1]=='O':
        return True
    elif v.row1[2]==v.row2[2]==v.row3[2]=='O':
        return True
    elif v.row1[0]==v.row2[1]==v.row3[2]=='O':
        return True
    elif v.row1[2]==v.row2[1]==v.row3[0]=='O':
        return True
    else:
        return False