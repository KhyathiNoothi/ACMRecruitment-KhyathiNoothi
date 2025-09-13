# Problem 1: Multiples of 3 or 5
def problem1():
    return sum(x for x in range(1000) if x % 3 == 0 or x % 5 == 0)

# Problem 2: Even Fibonacci Numbers
def problem2():
    a, b = 1, 2
    total = 0
    while b <= 4000000:
        if b % 2 == 0:
            total += b
        a, b = b, a + b
    return total

if __name__ == "__main__":
    print("Problem 1:", problem1())
    print("Problem 2:", problem2())
