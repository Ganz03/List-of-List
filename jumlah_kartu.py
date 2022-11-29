import ast
listOfElems2D = ast.literal_eval(input())
count = 0
for x in listOfElems2D:
    count += len(x)                    
print(count)