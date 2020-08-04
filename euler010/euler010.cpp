def main(n):
    prime = [True for i in range(0, n+1)]
    p = 2
    while(p *p <= n):
        if prime[p]:
            for i in range(p * 2, n+1, p):
                prime[i] = False
        p += 1
    prime[0] = False
    prime[1] = False
    ans = 0
    for p in range(n+1):
        if prime[p]:
            ans += p
    print(ans)


if __name__ == "__main__":
    n = 2000000
    main(n)
