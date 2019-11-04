def width(h, arr):
    w = 0
    for i in arr:
        if i > h:
            w += 2
        else:
            w += 1
    return w


if __name__ == "__main__":
    n, h = map(int, input().strip().split(' '))
    arr = list(map(int, input().strip().split(' ')))
    print(width(h, arr))