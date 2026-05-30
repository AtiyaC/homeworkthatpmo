num = int(input("Enter a number: "))
count = 0

# Use absolute value to handle negative numbers
n = abs(num)

if n == 0:
    count = 1
else:
    while n > 0:
        n //= 10  # Integer division
        count += 1

print(f"Total digits: {count}")
