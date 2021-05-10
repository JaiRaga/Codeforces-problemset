def teams(k, lis):
    l = []
    times = 5 - k
    for i in lis:
        if i <= times:
            l.append(i)
    return len(l) // 3


if __name__ == "__main__":
    n, k = map(int, input().strip().split())
    lis = list(map(int, input().strip().split()))
    print(teams(k, lis))
