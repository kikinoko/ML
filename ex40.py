import numpy as np

def gradient_descent(f_prime, initial_x, learning_rate, max_iters):
    
    x = initial_x
    history = [x]
    
    for i in range(max_iters):
        grad = f_prime(x)
        x -= learning_rate * grad
        history.append(x)
        
        # 収束判定（勾配が非常に小さくなった場合に停止）
        if abs(grad) < 1e-6:
            break
            
    return x, history

# 二次関数 f(x) = x^2 の勾配を定義
f_prime = lambda x: 2 * x

# 初期設定
initial_x = 10.0
learning_rate = 0.1
max_iters = 100

# 最急降下法の実行
optimal_x, history = gradient_descent(f_prime, initial_x, learning_rate, max_iters)

print("最適化された x の値:", optimal_x)
