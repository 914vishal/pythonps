#    1 
#   1 2 
#  1 2 3 
# 1 2 3 4 
#  1 2 3 
#   1 2 
#    1   
rows=4
for i in range(1,2*rows):
    res=""
    spaces=rows-i if i<=rows else i-rows 
    cols=i if i<=rows else 2*rows-i 
    for sp in range(1,spaces+1):
        res+=" "
    for j in range(1,cols+1):
        res+=str(j)+" "
    print(res)


#########################------------------------------


# 1 2 3 4 5 
#  1 2 3 4 
#   1 2 3 
#    1 2 
#     1 
#    1 2 
#   1 2 3 
#  1 2 3 4 
# 1 2 3 4 5 

rows=5
for i in range(1,2*rows):
    res=""
    spaces=i-1  if i<=rows else 2*rows-i-1
    cols=rows-i+1 if i<=rows else i-rows+1
    for sp in range(1,spaces+1):
        res+=" "
    for j in range(1,cols+1):
        res+=str(j)+" "
    print(res)