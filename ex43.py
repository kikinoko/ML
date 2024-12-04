import numpy as np

def gini_coefficient(values):
    
    values = np.array(values)
    if np.any(values < 0):
        raise ValueError("値には負の数はない。")
    
    n = len(values)
    if n == 0:
        return 0  # 要素がない場合はジニ係数を0とする

    # 値を昇順にソート
    sorted_values = np.sort(values)
    
    # 累積値の総和
    cumulative_values = np.cumsum(sorted_values)
    
    # ジニ係数の計算
    numerator = 2 * np.sum((np.arange(1, n + 1) * sorted_values))  # Σ(i * x_i)
    denominator = n * np.sum(sorted_values)  # n * Σ(x_i)
    gini = (numerator / denominator) - ((n + 1) / n)
    
    return gini

income = [40, 30, 20, 10]  # 所得の例
gini = gini_coefficient(income)
print(f"ジニ係数: {gini:.4f}")
