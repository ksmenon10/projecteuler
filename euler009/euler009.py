from math import pow, sqrt


def is_square(z):
    if pow(int(sqrt(z)), 2) == z:
        return True
    else:
        return False


def main():
    for a in range(1, 1000):
        for b in range(1, 1000):
            c = pow(a, 2) + pow(b,2)
            if is_square(c):
                z = sqrt(c);
                if a+b+z == 1000:
                    print(int(a*b*z))
                    return


if __name__ == "__main__":
    main()
