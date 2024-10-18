import bisect

n = int(input())


arr = list(map(int, input().split()))

target = int(input())


index = bisect.bisect_left(arr, target)


if index < len(arr) and arr[index] == target:
    print("YES")
else:
    print("NO")
