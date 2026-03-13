import random

POP_SIZE = 6
GENERATIONS = 15
MUTATION_RATE = 0.1

def fitness(x):
    return x*x + 2*x

def binary_to_decimal(b):
    return int(b, 2)

def random_chromosome():
    return format(random.randint(0,31),'05b')

population = [random_chromosome() for _ in range(POP_SIZE)]
for gen in range(GENERATIONS):
    print("\nGeneration", gen)
    population = sorted(population,
                        key=lambda c: fitness(binary_to_decimal(c)),
                        reverse=True)

    print("Population:", population)
    parents = population[:2]
    cut = random.randint(1,4)
    child1 = parents[0][:cut] + parents[1][cut:]
    child2 = parents[1][:cut] + parents[0][cut:]

    def mutate(chrom):
        if random.random() < MUTATION_RATE:
            pos = random.randint(0,4)
            chrom = list(chrom)
            chrom[pos] = '1' if chrom[pos]=='0' else '0'
            chrom = ''.join(chrom)
        return chrom

    child1 = mutate(child1)
    child2 = mutate(child2)

    population[-1] = child1
    population[-2] = child2

best = max(population, key=lambda c: fitness(binary_to_decimal(c)))

print("\nBest Chromosome:", best)
print("Best x:", binary_to_decimal(best))
print("Best fitness:", fitness(binary_to_decimal(best)))
