if __name__ == "__main__":
    n = input().split()
    juice = list(map(int, input().strip().split()))
    sum = 0
    for i in juice:
        sum += i
    sum /= len(juice)
    print(sum)
