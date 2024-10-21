import math

n = int(input())

point = [tuple(map(float, input().split())) for _ in range(n)]

dis = [[0] * n for _ in range(n)] #ｎ行列に変換

# ユークリッド距離を計算
for i in range(n):
    for j in range(n):
        if i != j:#距離０
            dx = point[i][0] - point[j][0]
            dy = point[i][1] - point[j][1]
            dis[i][j] = math.sqrt(dx**2 + dy**2)


for row in dis:
    print(" ".join(f"{d:.4f}" for d in row)) #.4f->小数点以下４桁まで
