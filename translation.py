if __name__ == "__main__":
    s = input().strip()
    t = input().strip()
    rev = ''

    for i in s:
        rev = i + rev
    if rev == t:
        print("YES")
    else:
        print("NO")
