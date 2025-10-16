# input from user
inches = float(input("Enter measurement in inches: "))

# Calculate and store converted values
foot = inches / 12
yard = inches / 36
centimetre = inches * 2.54
meter = inches / 39.37

# Print results
print("\n----- Conversion Results -----")
print("Measurement in Inches:", inches)
print("In Foot:", foot)
print("In Yard:", yard)
print("In Centimetres:", centimetre)
print("In Meters:", meter)
