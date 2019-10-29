def jokeProgramming(s):
    if s.count('H') > 0:
        return 'YES'
    elif s.count('Q') > 0:
        return 'YES'
    elif s.count('9') > 0:
        return 'YES'
    elif s.count('+') > 0:
        return 'NO'
    return 'NO'



if __name__ == "__main__":
    s = input().strip()
    print(jokeProgramming(s))