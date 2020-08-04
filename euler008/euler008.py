def answer(a):
    ans = 1
    for i in range(0, 13):
        start = i
        while start + 13 < 1000:
            tempprod = 1
            for j in range(start, start + 13):
                tempprod *= int(a[j])
            ans = max(ans, tempprod)
            start += 13
    print(ans)


def main():
    eight = open("euler008.in", "r");
    f1 = eight.readlines()
    y = ""
    for x in f1:
        y += x
    y = y.replace("\n", "")
    answer(y)


if __name__ == "__main__":
    main()
