def cards(s):
    s = s.lower()
    z = s.count('z')
    n = s.count('n')

    res = ''
    if n != 0:
        for i in range(n):
            res += '1 '
    if z != 0:
        for i in range(z):
            res += '0 '
    
    res.strip()
    return res


if __name__ == "__main__":
    n = input().strip()
    s = input().strip()
    print(cards(s))