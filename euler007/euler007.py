def main():
    primes = [2]
    count = 1
    lastprime = 2
    num = 3
    while count <10001:
        isprime = True
        for i in range(0, len(primes)):
            if num % primes[i] == 0:
                isprime = False
                break
        if isprime:
            lastprime = num
            primes.append(num)
            count += 1
        num += 1
    print(lastprime)


if __name__ == "__main__":
    main()