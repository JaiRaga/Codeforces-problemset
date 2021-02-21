def pangram(word):
    alpha = list('abcdefghijklmnopqrstuvwxyz')
    # l = len(alpha)

    for i in word:
        i = i.lower()
        if i in alpha:
            alpha.remove(i)

    if len(alpha) == 0:
        return 'YES'
    return 'NO'


if __name__ == "__main__":
    n = input().strip()
    word = input().strip()
    print(pangram(word))