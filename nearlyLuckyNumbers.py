if __name__ == "__main__":
    n = input().strip()
    num = 0
    num += n.count('4')
    num += n.count('7')
    if num == 4 or num == 7:
        print("YES")
    else:
        print("NO")
