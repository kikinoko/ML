import math

def square_root(x):
    if not isinstance(x, (int, float)):  # 数値以外の入力->instance
        return None
    if x < 0:  
        return -1
    return math.sqrt(x)  
print(square_root(16)) 
