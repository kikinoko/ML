def newton_method(f, f_prime, x0, tol=1e-7, max_iter=100):
   
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

#  f(x) = x^2 - 2 の解を求める
f = lambda x: x**2 - 2
f_prime = lambda x: 2 * x
x0 = 1.0  # 初期値

result = newton_method(f, f_prime, x0)
print("近似解", result)
