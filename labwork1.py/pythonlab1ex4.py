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