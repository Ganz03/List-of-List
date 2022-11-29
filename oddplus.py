import ast
Y = ast.literal_eval(input())

def IsOneElm(S) :
    if len(S) == 1 :
        return True
    else :
        return False

def IsAtom(e) :
    return type(e) != list

def oddplus(Y) :
    if Y == [] :
        return 0
    else :
        if IsAtom(Y[0]) :
            if Y[0] % 2 != 0 :
                return Y[0] + oddplus(Y[1:])
            else :
                return oddplus(Y[1:])
        else :
            if Y[0] == [] :
                return oddplus(Y[1:])
            else :
                return oddplus(Y[0]) + oddplus(Y[1:])

print(oddplus(Y)) 