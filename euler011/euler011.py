def right(x, i, j):
    num = 1
    for a in range(4):
        num *= x[i][j+a]
    return num


def down(x, i, j):
    num = 1
    for a in range(4):
        num *= x[i+a][j]
    return num


def rightDiag(x, i, j):
    num = 1
    for a in range(4):
        num *= x[i+a][j+a]
    return num

def leftDiag(x, i, j):
    num = 1
    for a in range(4):
        num *= x[i-a][j+a]
    return num


def answer(x):
    ans = 1
    for i in range(20):
        for j in range(20):
            if j <= 16:
                ans = max(ans, right(x,i,j))
            if i <= 16:
                ans = max(ans, down(x,i,j))
            if j <= 16 and i <= 16:
                ans = max(ans, rightDiag(x, i, j))
            if j <= 16 and i >= 3:
                ans = max(ans, leftDiag(x, i, j))
    print(ans)


def main():
    grid = [[1 for i in range(20)] for j in range(20)]

    eleven = open("euler011.txt", "r");
    f1 = eleven.readlines()

    str_grid = ""
    for i in f1:
        str_grid += i
    str_grid = str_grid.replace("\n", " ")

    num = ""
    x = 0
    y = 0
    for a in range(len(str_grid)):
        if str_grid[a] == ' ':
            grid[x][y] = int(num)
            num = ""
            y += 1
            if y == 20:
                y = 0
                x += 1
        num += str_grid[a]
    answer(grid)


if __name__ == "__main__":
    main()
