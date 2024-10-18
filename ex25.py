def transA(x):
    
    A = [[1, 3], [7, 6]]
    

    y0 = A[0][0] * x[0] + A[0][1] * x[1]
    y1 = A[1][0] * x[0] + A[1][1] * x[1]
    
    return y0, y1

x = list(map(int, input().split()))

y = transA(x)

print(f"{y[0]} {y[1]}")
