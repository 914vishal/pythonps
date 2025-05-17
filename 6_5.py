# task -1

# 5 5 5 5 5
# 4 4 4 4
# 3 3 3
# 2 2
# 1

rows=5
for i in range(rows,0,-1):
    res=""
    for j in range(i,0,-1):
        res+=str(i)+" "
    print(res)
    
##################################################

# task -2

#* * * * *
# * * * *
#  * * *
#   * *
#    *

rows=5
for i in range(1,rows+1):
    res=""
    for sp in range(i):
        res+=" "
    for j in range(1,rows-i+2):
        res+="*"+" "
    print(res)
    
##################################################

# task -3

# *       *
# *       *
# * * * * *
# *       *
# *       *

rows=5
mid=rows//2 +1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if j==1 or j==rows or i==mid:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)  