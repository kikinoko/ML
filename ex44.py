import numpy as np
import pandas as pd

def gini_impurity(y):

    prob = np.bincount(y) / len(y)
    return 1 - np.sum(prob ** 2)

def gini_split(data, feature, target):
  
    unique_values = data[feature].sort_values().unique()
    best_split = None
    min_gini = float('inf')

    for value in unique_values:
        left = data[data[feature] <= value][target]
        right = data[data[feature] > value][target]
        
        if len(left) == 0 or len(right) == 0:
            continue
        
        # Calculate weighted Gini impurity
        gini = (len(left) / len(data)) * gini_impurity(left) + \
               (len(right) / len(data)) * gini_impurity(right)
        
        if gini < min_gini:
            min_gini = gini
            best_split = value
    
    return best_split, min_gini

def find_best_split(data, features, target):
   
    best_feature = None
    best_split = None
    min_gini = float('inf')

    for feature in features:
        split, gini = gini_split(data, feature, target)
        if gini < min_gini:
            min_gini = gini
            best_feature = feature
            best_split = split
    
    return best_feature, best_split, min_gini

# サンプルデータ
data = pd.DataFrame({
    'Feature1': [2, 3, 10, 19, 25],
    'Feature2': [1, 5, 7, 14, 20],
    'Target': [0, 0, 1, 1, 0]
})

# 対象の特徴量とターゲット
features = ['Feature1', 'Feature2']
target = 'Target'

# ベストな分割を探す
best_feature, best_split, min_gini = find_best_split(data, features, target)


print(f"最小ジニ係数: {min_gini}")

