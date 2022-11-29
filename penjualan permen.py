import ast
inp = ast.literal_eval(input())

def IsOneElm(S) :
    if len(S) == 1 :
        return True
    else :
        return False

def IsAtom(e) :
    return type(e) != list

def penjualan(inp) :
    if inp == [] :
        return 0
    else :
        if IsAtom(inp[0]) :
            if inp[0] % 2 != 0 :
                return inp[0] * 3000 + penjualan(inp[1:])
            else :
                return inp[0] * 4000 + penjualan(inp[1:])
        else :
            n = 0
            for x in inp[0] :
                n += x
            if inp[0] == [] :
                return penjualan(inp[1:])
            else :
                if n % 2 != 0 :
                    return n * 1000 + penjualan(inp[1:])
                else :
                    return n * 2000 + penjualan(inp[1:])

print(penjualan(inp))