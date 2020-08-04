seq_lens = [0 for i in range(1000000)]


def collatz(num):
    col_len = 0
    count = 1
    temp = num
    while num != 1:
        if num %2 == 0:
            num = num/2
        else:
            num = num * 3 + 1
        count += 1
        if num < 1000000:
            if seq_lens[int(num)] != 0:
                count += seq_lens[int(num)]
                break
    seq_lens[temp] = count


def main():
    ans = 0
    big_collatz = 0
    for i in range(1, 1000000):
        collatz(i)
        if big_collatz < seq_lens[i]:
            big_collatz = seq_lens[i]
            ans = i
    print(ans)


if __name__ == "__main__":
    main()
