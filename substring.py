def substring(s):
    l = ''
    for i in range(0, len(s), 2):
        if i == 0:
            l += s[i:i + 2]
            # print(l)
        else:
            l += s[i + 1:i + 2]
            # print(l)
    return l


if __name__ == "__main__":
    t = int(input().strip())
    for i in range(t):
        s = input().strip()
        print(substring(s))