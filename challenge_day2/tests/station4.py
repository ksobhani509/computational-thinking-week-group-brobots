num = int(input("Input Number: "))


def prime_n(x):
    if x < 2:
        return False
    for i in range(2, int(x ** 0.5) + 1):
        if x % i == 0:
            return False
    return True


print(prime_n(num))