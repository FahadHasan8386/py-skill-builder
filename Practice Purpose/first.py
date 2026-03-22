1️⃣ Program to Check Whether a Given Number is Even or Odd
num = int(input("Enter a number: "))

if num % 2 == 0:
    print("Even Number")
else:
    print("Odd Number")
________________________________________
2️⃣ Program to Find the Sum of Even and Odd Numbers
n = int(input("Enter limit: "))

even_sum = 0
odd_sum = 0

for i in range(1, n+1):
    if i % 2 == 0:
        even_sum += i
    else:
        odd_sum += i

print("Sum of Even Numbers:", even_sum)
print("Sum of Odd Numbers:", odd_sum)
________________________________________
3️⃣ Program to Check Whether a Number is Positive or Negative
num = int(input("Enter a number: "))

if num > 0:
    print("Positive Number")
elif num < 0:
    print("Negative Number")
else:
    print("Zero")
________________________________________
4️⃣ Program to Find the Largest Number Among Three Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

largest = max(a, b, c)

print("Largest number is:", largest)
________________________________________
5️⃣ Program to Swap Two Numbers
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

a, b = b, a

print("After swap:")
print("a =", a)
print("b =", b)
________________________________________
6️⃣ Program to Find the Number of Integers Divisible by 5
count = 0

for i in range(1, 101):
    if i % 5 == 0:
        count += 1

print("Numbers divisible by 5:", count)
________________________________________
7️⃣ Program to Check if Two Numbers are Equal
a = int(input("Enter first number: "))
b = int(input("Enter second number: "))

if a == b:
    print("Numbers are equal")
else:
    print("Numbers are not equal")
________________________________________
8️⃣ Program to Find Sum of Digits of a Number
num = int(input("Enter a number: "))
sum = 0

while num > 0:
    digit = num % 10
    sum += digit
    num = num // 10

print("Sum of digits:", sum)
________________________________________
9️⃣ Program to Find Prime Numbers in a Given Range
start = int(input("Enter start: "))
end = int(input("Enter end: "))

for num in range(start, end+1):
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            print(num)
________________________________________
🔟 Program to Check Whether a Number is Prime
num = int(input("Enter a number: "))

if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not Prime")
            break
    else:
        print("Prime Number")
else:
    print("Not Prime")
________________________________________
1️⃣1️⃣ Program to Find Sum of First N Natural Numbers
n = int(input("Enter a number: "))

sum = 0

for i in range(1, n+1):
    sum += i

print("Sum =", sum)
________________________________________
1️⃣2️⃣ Program to Find the Factorial of a Number
n = int(input("Enter a number: "))

fact = 1

for i in range(1, n+1):
    fact *= i

print("Factorial =", fact)
________________________________________
1️⃣3️⃣ Program to Find All Roots of a Quadratic Equation
import cmath

a = float(input("Enter a: "))
b = float(input("Enter b: "))
c = float(input("Enter c: "))

d = (b**2) - (4*a*c)

root1 = (-b + cmath.sqrt(d)) / (2*a)
root2 = (-b - cmath.sqrt(d)) / (2*a)

print("Root 1 =", root1)
print("Root 2 =", root2)

