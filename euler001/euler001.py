def main():
    lim = 1000
    count = 0
    for i in range(1, lim):
        if i % 5 == 0 or i % 3 == 0:
            count += 1
    print(count)


if __name__ == "__main__":
    main()

