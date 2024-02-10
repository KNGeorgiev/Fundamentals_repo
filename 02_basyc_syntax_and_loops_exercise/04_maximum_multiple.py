divisor = int(input())
boundary = int(input())
largest = 0

for x in range(divisor, boundary + 1):
    if x > 0 and x % divisor == 0:
        largest = x

print(largest)
