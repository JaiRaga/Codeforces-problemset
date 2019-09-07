def hulk(n):
    n = int(n)
    one = "I hate"
    two = "I love"
    conn = " that "
    end = " it"

    sen = ''

    for i in range(1,n+1):
        if (i == 1 or i % 2 != 0) and i != n:
            sen += one + conn
        elif (i == 2 or i % 2 == 0) and i != n:
            sen += two + conn
        elif (i == 1 or i % 2 != 0):
            sen += one + end
        elif (i == 2 or i % 2 == 0):
            sen += two + end
        # elif i == n:
        #     str += end
    return sen

if __name__ == "__main__":
    n = input().strip()
    print(hulk(n))