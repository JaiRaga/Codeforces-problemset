if __name__ == "__main__":
    w, h, k = map(int, input().strip().split())
    cells = 0
    for i in range(k):
        cells += (w * 2) + (h * 2) - 4
        w -= 4
        h -= 4
    print(cells)
