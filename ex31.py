import matplotlib.pyplot as plt
import numpy as np

x = np.random.uniform(-3, 3, 100)
y = np.random.uniform(-3, 3, 100)

# ランダムな色を生成 (RGBA形式)
colors = np.random.rand(100)  # 0から1の範囲でランダムな色の値

plt.scatter(x, y, c=colors)  

# 軸の範囲を設定
plt.xlim(-3, 3)
plt.ylim(-3, 3)


# グリッドを追加
plt.grid()
# プロットを表示
plt.show()
