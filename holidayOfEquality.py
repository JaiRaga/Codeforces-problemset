if __name__ == "__main__":
    n = input()
    welfare = list(map(int, input().strip().split()))
    sub = max(welfare)
    sum = 0
    for i in welfare:
        sum += sub - i
    print(sum)
