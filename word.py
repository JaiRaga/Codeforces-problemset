if __name__ == "__main__":
    s = input().strip()
    upper = 0
    lower = 0
    for i in s:
        if i.isupper():
            upper += 1
        else:
            lower += 1
    if upper > lower:
        print(s.upper())
    else:
        print(s.lower())
