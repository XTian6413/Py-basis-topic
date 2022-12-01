

def sum_of_square(n):
    result = 0
    for i in range(1, n+1):
        result += i * i
    return result

print(sum_of_square(3))