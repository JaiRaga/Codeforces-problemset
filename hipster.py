if __name__ == "__main__":
    socks = list(map(int, input().strip().split()))
    hip = min(socks)
    maximum = max(socks)
    maximum -= hip
    maximum //= 2
    print(hip, maximum)
