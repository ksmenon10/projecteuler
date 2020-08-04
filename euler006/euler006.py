from math import pow

def squaresums(n):
    total = 0
    for i in range(1, n+1):
         total += i
    return pow(total, 2)


def sumsquares(n):
    total = 0
    for i in range(1, n+1):
        total += pow(i,2)
    return total


def main():
    n=100
    print(int(squaresums(n) - sumsquares(n)))


if __name__ == "__main__":
    main()
