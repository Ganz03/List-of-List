import ast
inp = ast.literal_eval(input())

def max2(a,b) :
    if a > b :
        return a
    else :
        return b

def IsOneElm(S) :
    if len(S) == 1 :
        return True
    else :
        return False

def IsAtom(e) :
    return type(e) != list

def maxL(S) :
    if IsOneElm(S) :
        if IsAtom(S[0]) :
            return S[0]
        else :
            return max(S[0])
    else :
        if IsAtom(S[0]) :
            return max2(S[0],max(S[1:]))
        else :
            return max2(max(S[0]),max(S[1:]))

def merdeka(inp) :
    if inp == [] :
        return 0
    else :
        return max(inp[0]) * 1000000 + merdeka(inp[1:])

print(merdeka(inp))