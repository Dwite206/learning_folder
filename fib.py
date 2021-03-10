def fib(number):
    num1 = 0
    num2 = 1
    result = []
    for i in range(number):
        result.append(num1)
        temp = num1
        num1 = num2
        num2 = temp + num2
    return result


print(fib(21))
