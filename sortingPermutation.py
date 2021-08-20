def permutatuin(s):
    s = list(s)
    cp = s.copy()
    cp.sort()

    c = 0
    for i in range(0, len(s)):
        if s[i] != cp[i]:
            c += 1

    return c


if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        l = int(input().strip())
        s = input().strip()
        print(permutatuin(s))