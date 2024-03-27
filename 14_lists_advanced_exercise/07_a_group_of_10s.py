sequence = list(map(int, input().split(', ')))
max_value = 10

while len(sequence) != 0:
    removed = list(filter(lambda x: x <= max_value, sequence))
    print(f"Group of {max_value}'s: {removed}")
    sequence = [n for n in sequence if n not in removed]
    max_value += 10
    
