## performed with while loop

s = "aaabbcaaaa"  # Output should be: a3b2c1a4
i = 0
res = ""
while i < len(s):
    current_char = s[i]
    count = 0
    while i < len(s) and s[i] == current_char:
        count += 1
        i += 1
    res += current_char + str(count)
print(res)


# output:- a3b2c1a4