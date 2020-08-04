from math import pow


def main():
    primes = [2]
    for i in range(3, 21):
        isPrime = True
        for j in range(0, len(primes)):
            if i % primes[j] == 0:
                isPrime = False
                break
        if isPrime:
            primes.append(i)

    gcd = [0 for i in range(0, len(primes))]

    for i in range(2, 21):
        num = i
        tempgcd = [0 for i in range(0, len(primes))]
        for j in range(0, len(primes)):
            if primes[j] > i or i == 1:
                break
            while num % primes[j] == 0:
                num = num / primes[j]
                tempgcd[j] += 1
        for k in range(0, len(primes)):
            if gcd[k] < tempgcd[k]:
                gcd[k] = tempgcd[k]

    product = 1
    for i in range(0, len(primes)):
        product *= int(pow(primes[i], gcd[i]))

    print(product)


if __name__ == "__main__":
    main()
