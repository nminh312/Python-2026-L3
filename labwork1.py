#ex1
r = float(input("Enter circle radius: "))
area = 3.14 * r * r
print("Circle area = ", area)
#ex2
celsius = (float(input("Enter temperature in Celsius: ")))
fahrenheit = (celsius * 9/5) + 32
print(f"{celsius} (C) = {fahrenheit} (F)")
#ex3
n = (int(input("Enter a number: ")))
if n<=1:
    print(f"{n} is not prime number")
else:
    for i in range(2, n):
        if n % i == 0:
            print(f"{n} is not prime number")
            break
    else:
        print(f"{n} is prime number")
#ex4
n = (int(input("Enter a number: ")))
if n<=1:
    print(f"{n} is not perfect number")
else:
    sum = 0
    for i in range(1, n):
        if n % i == 0:
            sum += i
    if sum == n:
        print(f"{n} is perfect number")
    else:
        print(f"{n} is not perfect number")
#ex5
colors= ["Red", "Green", "Blue", "Yellow", "Purple"]
ask = input("What is your favorite color? ")
if ask in colors:
    index = colors.index(ask)
    print(f"Your color is at index {index} in my list")
else:
    print ("Sorry, I could not find your color")
#ex6
range1 = range(0, 7)
range2 = range (1, 11, 3)
range3 = range(5, 0, -1)
range4 = range(6, -3, -2)
print(list(range1))
print(list(range2))
print(list(range3))
print(list(range4))
#ex7
def remove_dollar_sign(s):
    return s.replace("$", "")
text = input("Something with $: ")
result = remove_dollar_sign(text)
print(result)
#ex8
def extract_even(l):
    l = [1, 4, 5, -1, 10]
    result = []
    for i in l:
        if i%2 ==0:
            result.append(i)
    return result
print(extract_even)
#ex9
def factorial(n):

    result = 1
    for i in range(1, n + 1):
        result = result * i
    return result
n = (int(input("Enter a number: ")))
print(factorial(n))
#ex10
def divisor(n):
    result = []
    for i in range(1, n + 1):
        if n % i ==0:
            result.append(i)
    return result
n = (int(input("Enter a number: ")))
print(divisor(n))
#ex11
import math
def distance(x1, y1, x2, y2):
    d = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)
    return d
x1 = (float(input("x1: ")))
y1 = (float(input("y1: ")))
x2 = (float(input("x2: ")))
y2 = (float(input("y2: ")))

print("Distance", distance(x1, y1, x2, y2))
#ex12
def rectangle(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m-1 or j == 0 or j == n-1:
                print("*", end = " ")
            else:
                print(" ", end=" ")
        print()
m = (int(input("Columns: ")))
n = (int(input("Rows: ")))
print(rectangle(m, n))
