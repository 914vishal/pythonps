# a
# b c 
# d   e
# g     j
# k l m n o      

rows = 5
ch = ord('a')
for i in range(1, rows + 1):
    res = ""
    for j in range(1, i + 1):
        if j == 1 or j == i or i == rows:
            res += chr(ch) + " "
        else:
            res += "  "
        ch += 1
    print(res)
