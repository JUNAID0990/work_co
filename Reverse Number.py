# Read number of test cases
N = int(input("Enter number"))

results = []

for _ in range(N):
    # Read the numbers as integers (input contains space)
    line = input()
    space_index = line.find(' ')
    a = int(line[:space_index])
    b = int(line[space_index+1:])
    
    # Reverse a mathematically
    rev_a = 0
    temp = a
    while temp > 0:
        rev_a = rev_a * 10 + temp % 10
        temp = temp // 10
    
    # Reverse b mathematically
    rev_b = 0
    temp = b
    while temp > 0:
        rev_b = rev_b * 10 + temp % 10
        temp = temp // 10
    
    # Add reversed numbers
    total = rev_a + rev_b
    
    # Reverse the sum mathematically
    rev_sum = 0
    temp = total
    while temp > 0:
        rev_sum = rev_sum * 10 + temp % 10
        temp = temp // 10
    
    results.append(str(rev_sum))

    # print(rev_sum)
    # print(rev_a)  
print("\n OUTPUT ".join(results))
print(rev_a)
print(rev_b)
print(total)
print(rev_sum)
print(temp)