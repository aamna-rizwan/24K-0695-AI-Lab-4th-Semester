import random
def f(x):
    return -x**2 + 6*x

x = random.randint(0, 6)
print("Initial x:", x)
print("Initial f(x):", f(x))

while True:
    neighbors = []
    if x - 1 >= 0:
        neighbors.append(x - 1)
    if x + 1 <= 6:
        neighbors.append(x + 1)

    best_neighbor = x
    best_value = f(x)
    for n in neighbors:
        if f(n) > best_value:
            best_neighbor = n
            best_value = f(n)

    if best_neighbor == x:
        break

    x = best_neighbor
    print("Move to x =", x, " f(x) =", f(x))

print("\nFinal Optimal x:", x)
print("Maximum value f(x):", f(x))
