def main():
    fibsum = 0
    prevnum = 1
    num = 1
    while num < 4000000:
        if num % 2 == 0:
            fibsum += num
        temp = num
        num += prevnum
        prevnum = temp
    print(fibsum)


if __name__ == "__main__":
    main()
