num = int(input("Enter the number"))
binary_str = bin(num)  # Returns '0b1010'
# Remove '0b' using slicing
print(binary_str[2:])  # Output: '1010'