def removeSmallest(arr):
  if len(arr) == 0:
    return 'YES'

  arr.sort()
  prev = arr[0]
  current = 0
  
  for i in range(1, len(arr)):
    current = arr[i]
    if abs(current - prev) > 1:
      return 'NO'
    prev = current
  return 'YES'


if __name__ == "__main__":
  t = int(input().strip())
  n = 0
  arr = []
  for i in range(t):
    n = input().strip()
    arr = list(map(int, input().strip().split(' ')))
    print(removeSmallest(arr))