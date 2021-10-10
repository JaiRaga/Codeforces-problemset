def coolness(arr):
  l = 0
  h = 0
  total = 0
  for i in range(len(arr)):
    if i == 0:
      l = arr[i]
      h = arr[i]
    else:
      if arr[i] < l:
        l = arr[i]
        total += 1
      elif arr[i] > h:
        h = arr[i]
        total += 1
  return total


if __name__ == "__main__":
  n = int(input().strip())
  arr = list(map(int, input().strip().split()))
  print(coolness(arr))