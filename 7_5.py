# *       * 
# * *     * 
# *   *   *     # print pattern 'N'
# *     * *  
# *       * 

rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==j or j==1 or j==rows:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)
print()    

#############------------------

# * * * * * 
#       *   
#     *     
#   *       
# * * * * * 

rows=5
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i==1 or i==rows or i+j==rows+1:
            res+="*"+" "
        else:
            res+=" "+" "
    print(res)
print()    

#############------------------



# * * * * * 
# *       * 
# * * * * * 
# *     *   
# *       * 

rows=5
mid=rows//2 +1
for i in range(1,rows+1):
    res=""
    for j in range(1,rows+1):
        if i<mid:
            if i==1 or j==1 or j==rows:
                res+="*"+" "
            else:
                res+=" "+" "
        elif i>=mid:
            if i==mid or j==1 or i==j:
                res+="*"+" "
            else:
                res+=" "+" "
    print(res)