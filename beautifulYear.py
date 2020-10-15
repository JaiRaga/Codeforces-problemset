if __name__ == "__main__":
    y = int(input().strip())
    n = y

    while True:
        c = 0
        n = n + 1
        s = str(n)
        # print(s)
        for i in s:
            if s.count(i) != 1:
                # print("No")
                break
            c += 1
        if c == 4:
            print(int(n))
            break
