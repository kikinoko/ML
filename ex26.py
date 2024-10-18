def transA(x, A):

    result = []
    for row in A:

        transformed_value = sum(row[i] * x[i] for i in range(len(x)))
        result.append(transformed_value)
    return result

# 標準入力の処理
d, m = map(int, input().split())  # d: ベクトルの次元, m: 変換後の次元

x = list(map(int, input().split()))

A = [list(map(int, input().split())) for _ in range(m)]

y = transA(x, A)

print(" ".join(map(str, y)))
