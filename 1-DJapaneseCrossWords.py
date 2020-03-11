if __name__ == "__main__":
    n = int(input().strip())
    s = input().strip()
    s = s.split('W')

    def fil(lis):
        for i in lis:
            if i != "":
                return True
            else:
                return False
    s = list(filter(fil, s))

    print(len(s))
    for i in s:
        print(len(i), end=" ")
