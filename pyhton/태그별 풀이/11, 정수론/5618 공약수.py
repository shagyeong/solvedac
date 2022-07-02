def divisor(numbers:list):
    minimum = min(numbers)
    divisors = []

    for i in range(1, minimum + 1):
        result = 1
        for n in numbers:
            if n // i == 0:
                result = 1
            else:
                result = 0
        if result == 1:
            divisors.append(i)
            divisors.append(minimum // i)

    divisors.sort()
    divisors = set(divisors)
    divisors = list(divisors)
    return divisors

print(divisor([75, 125]))