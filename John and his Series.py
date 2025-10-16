# a = first term
# d = common difference
# n = number of terms

# Input values
a = float(input("Enter the first term (a): "))
d = float(input("Enter the common difference (d): "))
n = int(input("Enter the number of terms (n): "))

# Calculate nth term Tn​=a+(n−1)×d
nth_term = a + (n - 1) * d

# Calculate sum of n terms Sn​=2/n ​×(2a+(n−1)×d)
sum = (n / 2) * (2 * a + (n - 1) * d)

# results
print("The nth term (Tn) is:", nth_term)
print("The sum of first n terms (Sn) is:", sum)
