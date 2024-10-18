import math

def cal(numbers):
    heikin = sum(numbers) / len(numbers)
    
  
    variance = sum((x - heikin) ** 2 for x in numbers) / len(numbers)#variance->分散
    std = math.sqrt(variance) #std->standard deviation 標準偏差
    
    return heikin, std
numbers = list(map(float, input().split()))

heikin, std = cal(numbers)
print(f"平均: {heikin:.2f}, 標準偏差: {std:.2f}")
