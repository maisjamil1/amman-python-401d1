import random

for i in range(3):
    # print(int(random.random()*10))
    print(random.randint(0,10))

# Use it for rolling a dice

# Generate 5 random numbers between 1 and 6

output = []

for i in range(5):
    output.append(random.randint(1,6))

print(output)
