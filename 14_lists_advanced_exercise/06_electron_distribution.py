electron_number = int(input())

final_list = []

for x in range(1, electron_number + 1):
    electrons_per_shell = 2 * (x ** 2)
    if sum(final_list) + electrons_per_shell < electron_number:
        final_list.append(electrons_per_shell)
    else:
        final_list.append(electron_number - sum(final_list))
        break

print(final_list)
