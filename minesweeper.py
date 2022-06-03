from apicalls import minesweeper
import json

def check_bomb(isit):
    if(isit == '*'):
        return 1
    else:
        return 0 

def resolver():
    problem = json.loads(minesweeper().content)
    solution = problem

    rows = 0

    for line in solution:
        columns = 0
        for block in line:
            if(block == ' '):
                solution[rows][columns] = str(check_bomb(solution[rows-1][columns-1]) + check_bomb(solution[rows-1][columns]) + check_bomb(solution[rows-1][columns+1]) + check_bomb(solution[rows][columns-1]) + check_bomb(solution[rows][columns+1]) + check_bomb(solution[rows+1][columns-1]) + check_bomb(solution[rows+1][columns]) + check_bomb(solution[rows+1][columns+1]))
            columns += 1
        rows += 1
    
    package = {'problem': problem, 'solution': solution}
    return package