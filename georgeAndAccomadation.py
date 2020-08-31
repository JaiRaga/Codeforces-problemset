if __name__ == "__main__":
    t = int(input().strip())
    count = 0
    for i in range(t):
        p, q = map(int, input().strip().split(" "))
        if q - p >= 2:
            count += 1
    print(count)
