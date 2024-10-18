import math

x1, y1 = map(float, input().split())
x2, y2 = map(float, input().split())

dis = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)

# 小数点以下1桁以上表示
print(f"{dis:.1f}")
