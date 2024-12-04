from math import inf
import numpy as np
import pandas as pd

# ノードを表すクラス
class DecisionTreeNode:
    def __init__(self, index=None, value=None, left=None, right=None, output=None):
        self.index = index
        self.value = value
        self.left = left
        self.right = right
        self.output = output

# Gini指数の計算
def gini_index(groups, class_values):
    gini = 0.0
    total_size = sum(len(group) for group in groups)
    for group in groups:
        size = len(group)
        if size == 0:
            continue
        score = 0.0
        for class_val in class_values:
            proportion = [row[-1] for row in group].count(class_val) / size
            score += proportion * proportion
        gini += (1.0 - score) * (size / total_size)
    return gini

# データを分割
def test_split(index, value, dataset):
    left, right = [], []
    for row in dataset:
        if row[index] <= value:
            left.append(row)
        else:
            right.append(row)
    return left, right

# 最良の分割を見つける
def get_best_split(dataset):
    class_values = list(set(row[-1] for row in dataset))
    best_index, best_value, best_score, best_groups = None, None, inf, None
    for index in range(len(dataset[0]) - 1):
        for row in dataset:
            groups = test_split(index, row[index], dataset)
            gini = gini_index(groups, class_values)
            if gini < best_score:
                best_index, best_value, best_score, best_groups = index, row[index], gini, groups
    if best_groups is None:
        raise ValueError("No valid split found!")
    return {'index': best_index, 'value': best_value, 'groups': best_groups}

# リーフノードの出力を生成
def to_terminal(group):
    outcomes = [row[-1] for row in group]
    return max(set(outcomes), key=outcomes.count)

# ノードを分割
def split(node, max_depth, min_size, depth):
    left, right = node['groups']
    del(node['groups'])

    # 片方が空の場合
    if not left or not right:
        node_output = to_terminal(left + right)
        return DecisionTreeNode(output=node_output)

    # 最大深度に達した場合
    if depth >= max_depth:
        left_output = to_terminal(left)
        right_output = to_terminal(right)
        return DecisionTreeNode(
            index=node['index'],
            value=node['value'],
            left=DecisionTreeNode(output=left_output),
            right=DecisionTreeNode(output=right_output),
        )

    # 最小データ数以下ならリーフノード
    if len(left) <= min_size:
        left = DecisionTreeNode(output=to_terminal(left))
    else:
        left_split = get_best_split(left)
        left = split(left_split, max_depth, min_size, depth + 1)

    if len(right) <= min_size:
        right = DecisionTreeNode(output=to_terminal(right))
    else:
        right_split = get_best_split(right)
        right = split(right_split, max_depth, min_size, depth + 1)

    return DecisionTreeNode(index=node['index'], value=node['value'], left=left, right=right)

# 決定木の構築
def build_tree(train, max_depth, min_size):
    root = get_best_split(train)
    return split(root, max_depth, min_size, 1)

# 予測
def predict(node, row):
    if node.output is not None:
        return node.output
    if row[node.index] <= node.value:
        return predict(node.left, row)
    else:
        return predict(node.right, row)

# データセット
dataset = [
    [2.771244718, 1.784783929, 0],
    [1.728571309, 1.169761413, 0],
    [3.678319846, 2.81281357, 0],
    [3.961043357, 2.61995032, 0],
    [2.999208922, 2.209014212, 0],
    [7.497545867, 3.162953546, 1],
    [9.00220326, 3.339047188, 1],
    [7.444542326, 0.476683375, 1],
    [10.12493903, 3.234550982, 1],
    [6.642287351, 3.319983761, 1]
]

# 決定木の構築
tree = build_tree(dataset, max_depth=3, min_size=1)

# テスト
for row in dataset:
    prediction = predict(tree, row)
    print(f"Expected: {row[-1]}, Predicted: {prediction}")
