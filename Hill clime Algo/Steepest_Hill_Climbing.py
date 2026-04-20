def f(x):
    return -x**2 + 5

def steepest_hill_climbing(start, step, max_iter):
    current = start

    for _ in range(max_iter):
        neighbors = [current - step, current + step]

        best = current
        for n in neighbors:
            if f(n) > f(best):
                best = n

        if best == current:
            break

        current = best

    return current, f(current)


# Input
start = int(input("Enter starting value: "))
step = int(input("Enter step size: "))
max_iter = int(input("Enter max iterations: "))

# Run
result = steepest_hill_climbing(start, step, max_iter)

print("Steepest-Ascent Hill Climbing Result:")
print("Best State:", result[0])
print("Best Value:", result[1])