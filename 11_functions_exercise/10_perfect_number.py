def perfect_number(n):
    perfect_container = 0

    for i in range(1, n):
        if n % i == 0:
            perfect_container += i

    if perfect_container == n:
        print("We have a perfect number!")
    else:
        print("It's not so perfect.")


number = int(input())

perfect_number(number)
