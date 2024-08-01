def sumOfDivisors(n):
    
    if n <= 0:
        return 0
    
    sum = 0

    for i in range(1, n):
        if n % i == 0:
            sum += i

    return sum

input_number = int(input("Please enter a positive numbers: "))
result = sumOfDivisors(input_number)
print("sum of divisors: ", result)

for a in range (100, 1001):
    b = sumOfDivisors(a)
    if a < b and sumOfDivisors(b) == a:
        print(a, b, sep= ',' , end = '--')


