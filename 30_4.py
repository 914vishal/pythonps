# task-1
#               row    cols
# 1 1 1 1 1       1       5
# 2 2 2 2 2       2       5       
# 3 3 3 3 3       3       5
# 4 4 4 4 4       4       5
# 5 5 5 5 5       5       5

rows=5
for row in range(rows):
    s=""
    for col in range(rows):
        s+= str(row+1)+" "
    print(s)
    
# output:-

# 1 1 1 1 1 
# 2 2 2 2 2
# 3 3 3 3 3
# 4 4 4 4 4
# 5 5 5 5 5
    
######--------------------------------------

# task-2

#               row    cols
# 1               1       5
# 2 2              2       5       
# 3 3 3            3       5
# 4 4 4 4           4       5
# 5 5 5 5 5       5       5

rows=5
for row in range(1,rows+1):
    s=" "
    for col in range(1,row+1):
        s+= str(row)+ " " 
    print(s)
    
# output:-
#  1
#  2 2
#  3 3 3
#  4 4 4 4
#  5 5 5 5 5