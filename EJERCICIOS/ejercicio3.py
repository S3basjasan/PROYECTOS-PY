# Fibonacci
fibonacci = []
def calcualarFibonacci(num):
    if num == 0:
        fibonacci.append(0)
        return 0
    elif num == 1:
        fibonacci.append(1)
        return 1
    return calcualarFibonacci(num - 2) + calcualarFibonacci(num - 1)

print(f"El fibonacci es: {calcualarFibonacci(5)}")
print(fibonacci)

