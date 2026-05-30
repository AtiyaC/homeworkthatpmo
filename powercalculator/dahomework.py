# Function to calculate power
def calculate_power(base, exponent):
    return base ** exponent

# User input
try:
    num = float(input("Enter the base number: "))
    pwr = float(input("Enter the power: "))
    
    result = calculate_power(num, pwr)
    print(f"{num} raised to the power of {pwr} is: {result}")
except ValueError:
    print("Please enter valid numbers.")
