# Take input
amount = int(input("Enter the amount: "))
denomination = int(input("Enter the largest denomination Avasthi has: "))

# Available denominations in descending order
denominations = [100, 50, 20, 10, 5, 2, 1]

# Only consider denominations <= the one Avasthi has
denominations = [d for d in denominations if d <= denomination]

# Dictionary to store number of notes
notes_count = {}

# Calculate number of notes using match-case
for d in denominations:
    match d:
        case 100 | 50 | 20 | 10 | 5 | 2 | 1:
            notes_count[d] = amount // d
            amount = amount % d

# Print the result
for d in denominations:
    print("%d rupees note: %d" % (d, notes_count[d]))

# amount = 276, denominations = [100, 50, 20, 10, 5, 2, 1]
# 100s: 276 // 100 = 2 use 2 notes of 100 remaining 276 % 100 = 76
# 50s: 76 // 50 = 1 use 1 note of 50 remaining 76 % 50 = 26
# Continue for 20s, 10s, etc.