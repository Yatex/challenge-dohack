from apicalls import minesweeper
import numpy as np
import json

def check_bomb(isit):
    if(isit == '*'):
        return 1
    else:
        return 0 

def resolver():
    problem = np.array(json.loads(minesweeper().content))
    solution = problem.copy()

    rows = 0

    for line in solution:
        columns = 0
        for block in line:
            if(block == ' '):
                solution[rows][columns] = str(check_bomb(solution[rows-1][columns-1]) + check_bomb(solution[rows-1][columns]) + check_bomb(solution[rows-1][columns+1]) + check_bomb(solution[rows][columns-1]) + check_bomb(solution[rows][columns+1]) + check_bomb(solution[rows+1][columns-1]) + check_bomb(solution[rows+1][columns]) + check_bomb(solution[rows+1][columns+1]))
            columns += 1
        rows += 1
    
    package = {'problem': problem.tolist(), 'solution': solution.tolist()}
    return package