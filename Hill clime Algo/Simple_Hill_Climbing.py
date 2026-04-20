import random

def f(x):
    return -x**2 + 5

def simple_hill_climbing(start, step, max_iter):
    current = start

    for _ in range(max_iter):
        neighbors = [current - step, current + step]

        moved = False
        for n in neighbors:
            if f(n) > f(current):
                current = n
                moved = True
                break

        if not moved:
            break

    return current, f(current)


# Input
start = int(input("Enter starting value: "))
step = int(input("Enter step size: "))
max_iter = int(input("Enter max iterations: "))

# Run
result = simple_hill_climbing(start, step, max_iter)

print("Simple Hill Climbing Result:")
print("Best State:", result[0])
print("Best Value:", result[1])