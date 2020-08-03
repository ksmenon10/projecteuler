from math import sqrt


def main():
    lim = 600851475143
    n = int(sqrt(lim))
    prime = [True for i in range(2, n + 1)]
    p = 2
    num = 3

    while p * p <= n - 1:
        if prime[p]:
            num = p * p
            for i in range(num, n - 1, p):
                prime[i] = False
        p += 1

    for i in range((n - 2), 2, -1):
        if prime[i]:
            if lim % i == 0:
                print(i)
                break


if __name__ == "__main__":
    main()
