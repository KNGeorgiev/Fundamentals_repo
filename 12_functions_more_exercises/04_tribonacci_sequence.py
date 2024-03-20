def tribonacci_sequence(n):

    counter = 0

    a1 = 0
    a2 = 0
    a3 = 1

    while counter < n:
        print(a3, end=" ")
        result = a1 + a2 +a3
        a1 = a2
        a2 = a3
        a3 = result
        counter += 1


number = int(input())
tribonacci_sequence(number)
