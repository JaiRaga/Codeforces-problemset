if __name__ == "__main__":
    t = int(input().strip())

    for i in range(t):
        a, b = map(int, input().strip().split())
        diff = abs(a - b)
        if a == b:
            print(0)
        elif b - a == 1:
            print(1)
        elif a > b and diff % 2 == 0:
            print(1)
        elif a > b and diff % 2 != 0:
            print(2)
        elif a < b and diff % 2 == 0:
            print(2)
        elif a < b and diff % 2 != 0:
            print(1)
