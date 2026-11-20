num = int(input())
num_fact = 0

for i in range(num, 0, -1):
    num_fact = num_fact + (num-1) * i

print(num_fact)


product = 1
for i in range(1, num + 1):
    product *= i # product = product * i
print(product)