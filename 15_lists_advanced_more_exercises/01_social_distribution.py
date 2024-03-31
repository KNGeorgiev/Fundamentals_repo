population = [int(i) for i in input().split(', ')]
minimum_wealth = int(input())

if sum(population) / len(population) < minimum_wealth:
    print('No equal distribution possible')
    exit()

while any(person < minimum_wealth for person in population):
    richest, poorest = max(population), min(population)
    index_richest, index_poorest = population.index(richest), population.index(poorest)
    difference = minimum_wealth - poorest
    population[index_richest] -= difference
    population[index_poorest] += difference

print(population)
