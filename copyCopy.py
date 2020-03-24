if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        n = int(input().strip())
        arr = list(map(int, input().strip().split()))
        arr.sort()
        arr = list(set(arr))

        print(len(arr))
