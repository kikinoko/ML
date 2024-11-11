def newton_method(f, f_prime, x0, tol=1e-7, max_iter=100):
    """
    ニュートン法で f(x) = 0 の解を求める

    Parameters:
    f (function): 関数 f(x)
    f_prime (function): 関数 f(x) の導関数 f'(x)
    x0 (float): 初期値
    tol (float): 許容誤差
    max_iter (int): 最大反復回数

    Returns:
    float: 近似解
    """
    x = x0
    for i in range(max_iter):
        fx = f(x)
        fpx = f_prime(x)
        
      
        # ニュートン法の更新式
        x_new = x - fx / fpx
        
        # 収束判定
        if abs(x_new - x) < tol:
         
            return x_new
        
        x = x_new
    
    return x

# 例: f(x) = x^2 - 2 の解を求める
f = lambda x: x**2 - 2
f_prime = lambda x: 2 * x
x0 = 1.0  # 初期値

result = newton_method(f, f_prime, x0)
print("近似解", result)
