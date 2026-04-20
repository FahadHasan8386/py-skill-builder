import random

def f(x):
    return -x**2 + 5

def stochastic_hill_climbing(start, step, max_iter):
    current = start

    for _ in range(max_iter):
        neighbors = [current - step, current + step]
        next_state = random.choice(neighbors)

        if f(next_state) > f(current):
            current = next_state

    return current, f(current)


# Input
start = int(input("Enter starting value: "))
step = int(input("Enter step size: "))
max_iter = int(input("Enter max iterations: "))

# Run
result = stochastic_hill_climbing(start, step, max_iter)

print("Stochastic Hill Climbing Result:")
print("Best State:", result[0])
print("Best Value:", result[1])