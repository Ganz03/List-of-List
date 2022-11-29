import ast
X = ast.literal_eval(input())

def IsPrima(n,i = 2) :
    if n < 2 :
        return False
    elif n == 2 :
        return True
    elif n % i == 0 :
        return False
    elif i * i > n :
        return True 
    else :
        return IsPrima(n,i+1)

def IsOneElm(S) :
    if len(S) == 1 :
        return True
    else :
        return False
        
def IsAtom(e) :
    return type(e) != list

def PrimaPlus(X) :
    if X == [] :
        return 0
    else :
        if IsAtom(X[0]) :
            if IsPrima(X[0],i = 2) :
                return X[0] + PrimaPlus(X[1:])
            else :
                return PrimaPlus(X[1:])
        else :
            if X[0] == [] :
                return PrimaPlus(X[1:])
            else :
                return PrimaPlus(X[0]) + PrimaPlus(X[1:])

print(PrimaPlus(X))