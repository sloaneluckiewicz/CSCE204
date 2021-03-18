def factorial(num):
    answer = 1

    for i in range(1, num+1):
        answer *= i 

    return answer 

result = factorial(7)
print(f"7! = {result}")