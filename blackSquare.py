if __name__ == "__main__":
    strips = list(map(int, input().strip().split()))
    squ = input().strip()
    cal = 0
    for i in squ:
        i = int(i)
        cal += strips[i-1]
    print(cal)
