import matplotlib.pyplot as plt
import numpy as np

# ランダムな座標を生成
x = np.random.uniform(-3, 3, 10)
y = np.random.uniform(-3, 3, 10)#np.random.uniform(low, high, size)


# 散布図を作成
plt.scatter(x, y)

# 軸の範囲を設定
plt.xlim(-3, 3)
plt.ylim(-3, 3)


# グリッドを追加
plt.grid()
# プロットを表示
plt.show()
