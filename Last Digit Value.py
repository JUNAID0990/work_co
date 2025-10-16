'''Start with current = a_last.

Multiply current * a_last and take % 10 to get the next last digit.

Stop when a last digit repeats (cycle found).

Use b % cycle_length to pick the correct last digit.'''


# Read number of test cases
N = int(input("Enter number of test cases: "))

# Step 2: Store all test cases in a list
test_cases = []
for _ in range(N):
    # map use for input into integers
    a, b = map(int, input().split())  # Split input into integers
    test_cases.append((a, b))

#  Process each test case
for a, b in test_cases:
    a_last = a % 10  # Only last digit matters
    cycle = []
    seen = set()
    
    current = a_last
    while current not in seen:
        cycle.append(current)
        seen.add(current)
        current = (current * a_last) % 10  # next last digit
    
    cycle_len = len(cycle)
    
    # Find the correct index in the cycle
    index = b % cycle_len
    if index == 0:
        index = cycle_len
    
    print("output",cycle[index-1])


