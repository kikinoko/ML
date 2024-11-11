import matplotlib.pyplot as plt
import numpy as np

# サンプル数
num_samples = 100

# 平均0、標準偏差2の正規分布からランダムにサンプルを生成
samples = np.random.normal(loc=0, scale=2, size=num_samples)

# ヒストグラムを作成
plt.hist(samples)
plt.grid(axis='y', alpha=0.75)
plt.show()
