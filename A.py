def a(s):
    count = s.count('a')
    if count > (len(s) // 2):
        return len(s)
    else:
        return count + (count - 1)



if __name__ == "__main__":
    s = input().strip()
    print(a(s))