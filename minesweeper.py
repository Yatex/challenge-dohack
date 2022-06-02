from xml.etree.ElementTree import tostring


def check_bomb(isit):
    if(isit == '*'):
        return 1
    else:
        return 0 

def checkborders():
    return check_bomb(solution[rows-1][columns-1]) + check_bomb(solution[rows-1][columns]) + check_bomb(solution[rows-1][columns+1]) + check_bomb(solution[rows][columns-1]) + check_bomb(solution[rows][columns+1]) + check_bomb(solution[rows+1][columns-1]) + check_bomb(solution[rows+1][columns]) + check_bomb(solution[rows+1][columns+1])

map = [["+","-","-","-","-","-","-","-","-","+"],["|","*"," "," "," ","*"," ","*","*","|"],["|","*","*","*"," ","*"," ","*","*","|"],["|"," "," "," "," ","*","*"," ","*","|"],["|","*"," ","*","*","*","*"," "," ","|"],["|"," ","*"," "," "," "," ","*"," ","|"],["|"," ","*","*","*"," "," "," ","*","|"],["|"," "," ","*","*"," "," "," "," ","|"],["|"," "," ","*"," ","*","*"," "," ","|"],["+","-","-","-","-","-","-","-","-","+"]] # recieve map
solution = map

rows = 0
columns = 0

for line in solution:
    columns = 0
    for block in line:
        if(block != '|' and block != '-' and block != '+' and block != '*'):
            solution[rows][columns] = str(checkborders())
        columns += 1
    rows += 1

for line in solution:
    print(line)