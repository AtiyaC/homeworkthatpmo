# Initial values
a = 10
b = 20
c = 30

print(f"Before swapping: a = {a}, b = {b}, c = {c}")

# Swapping logic (a -> b, b -> c, c -> a)
temp = a
a = c
c = b
b = temp

print(f"After swapping:  a = {a}, b = {b}, c = {c}")
