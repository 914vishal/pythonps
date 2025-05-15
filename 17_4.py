# Write a program to print the count of   number of Fibonacci numbers in between 0 to 500 ?
a = 0
b = 1
count = 0
while a <= 500:
    count += 1
    a = b
    b = a + b
print("Count of Fibonacci numbers between 0 and 500:", count)