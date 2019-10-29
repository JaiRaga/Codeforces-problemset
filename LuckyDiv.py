def lucky(num):
    n = str(num)
    l = n.count('4') + n.count('7')
    if l == len(n):
        return 'YES'
    elif num % 47 == 0 or num % 4 == 0 or num % 7 == 0:
        return 'YES'
    return 'NO'


if __name__ == "__main__":
    n = int(input().strip())
    print(lucky(n))