import ast
i = ast.literal_eval(input())
x = int(input())

def IsOneElm(S) :
    if len(S) == 1 :
        return True
    else :
        return False

def IsAtom(e) :
    return type(e) != list

def monster(i,x) :
    if i == [] :
        return i
    else :
        if IsAtom(i[0]) :
            print("A")
            if i[0] % x == 0 :
                return monster(i[1:],x)
            else :
                return [i[0]] + monster(i[1:],x)
        else :
            if i[0] == [] :
                return monster(i[1:],x)
            else :
                return [monster(i[0],x)] + monster(i[1:],x)

print(monster(i,x))