import sys

n1 = int(input())
n2 = int(input())
n3 = int(input())

largest = 0

if n2 > n1 and n2 > n3:
    largest = n2

if n3 > n1 and n3 > n2:
    largest = n3

if n1 > n2 and n1 > n3:
    largest = n1

print(largest)
