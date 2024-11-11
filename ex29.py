import numpy as np

#多角形近似
def RegularPolygon(N):
    theta = np.radians(360 / N) #３６０°をN等分し、度数法から弧度法に変換
    pi = N * np.sin(theta) / 2 #正N角形の面積を計算
    return pi

#出力
print("RegularPolygon(1000000) = " + str(RegularPolygon(1000000)))
