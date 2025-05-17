# # 1. find the smallest palindromic substring in a string

string="malayali"
smallest=""
for i in range(len(string)):
    temp=""
    for j in range(i,len(string)):
        temp+=string[j]
        if temp==temp[::-1] and len(temp)>=2:
            if smallest=="" or len(temp)<len(smallest):
                smallest=temp 
print(smallest)
