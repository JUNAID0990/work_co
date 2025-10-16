'''First, it checks if a is greater than both b and c.
If true -> a is maximum.
Otherwise -> it compares b and c to find the maximum.
True and True → True False and True → False False and False → False True and False → False'''


# Given three numbers
a = 10
b = 25
c = 15

# ternary operator
max_num = a if (a > b and a > c) else (b if b > c else c)

print("Maximum number is:", max_num)
