from math import floor


def checkPalindrome(n):
    size = len(n) - 1
    for i in range(0, floor((len(n)) / 2)):
        if n[i] != n[size - i]:
            return False
    return True


if __name__ == '__main__':
    maxAns = 0
    for i in range(500, 1000):
        for j in range(500, 1000):
            if checkPalindrome(str(i * j)):
                if maxAns < i * j:
                    maxAns = i * j
    print(maxAns)
