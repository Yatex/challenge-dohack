from xml.etree.ElementTree import tostring
from apicalls import minesweeper

def check_bomb(isit):
    if(isit == '*'):
        return 1
    else:
        return 0 

def resolver():
    map = minesweeper()
    solution = map

    rows = 0
    columns = 0

    for line in solution:
        columns = 0
        for block in line:
            if(block != '|' and block != '-' and block != '+' and block != '*'):
                solution[rows][columns] = str(check_bomb(solution[rows-1][columns-1]) + check_bomb(solution[rows-1][columns]) + check_bomb(solution[rows-1][columns+1]) + check_bomb(solution[rows][columns-1]) + check_bomb(solution[rows][columns+1]) + check_bomb(solution[rows+1][columns-1]) + check_bomb(solution[rows+1][columns]) + check_bomb(solution[rows+1][columns+1]))
            columns += 1
        rows += 1
    
    return map, solution