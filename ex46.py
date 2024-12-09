import random
from collections import Counter

# ヘルパー関数
def test_split(index, value, dataset):

    left, right = [], []
    for row in dataset:
        if row[index] < value:
            left.append(row)
        else:
            right.append(row)
    return left, right

def gini_index(groups, classes):

    n_instances = float(sum(len(group) for group in groups))
    gini = 0.0
    for group in groups:
        size = float(len(group))
        if size == 0:
            continue
        score = 0.0
        for class_val in classes:
            p = [row[-1] for row in group].count(class_val) / size
            score += p * p
        gini += (1.0 - score) * (size / n_instances)
    return gini

def to_terminal(group):
   
    outcomes = [row[-1] for row in group]
    return Counter(outcomes).most_common(1)[0][0]

def split(node, max_depth, min_size, depth, features, get_best_split_with_features):
   
    left, right = node['groups']
    del node['groups']
    if not left or not right:
        node['left'] = node['right'] = to_terminal(left + right)
        return
    if depth >= max_depth:
        node['left'], node['right'] = to_terminal(left), to_terminal(right)
        return
    if len(left) <= min_size:
        node['left'] = to_terminal(left)
    else:
        node['left'] = get_best_split_with_features(left, features)
        split(node['left'], max_depth, min_size, depth + 1, features, get_best_split_with_features)
    if len(right) <= min_size:
        node['right'] = to_terminal(right)
    else:
        node['right'] = get_best_split_with_features(right, features)
        split(node['right'], max_depth, min_size, depth + 1, features, get_best_split_with_features)

def predict(node, row):
   
    if row[node['index']] < node['value']:
        if isinstance(node['left'], dict):
            return predict(node['left'], row)
        else:
            return node['left']
    else:
        if isinstance(node['right'], dict):
            return predict(node['right'], row)
        else:
            return node['right']

# ランダムフォレストクラス
class my_RandomForestClassifier:
    def __init__(self, n_trees=10, max_depth=5, min_size=1, sample_size=0.8, n_features=None):
        self.n_trees = n_trees
        self.max_depth = max_depth
        self.min_size = min_size
        self.sample_size = sample_size
        self.n_features = n_features
        self.trees = []

    def _subsample(self, dataset):
    
        sample = []
        n_sample = round(len(dataset) * self.sample_size)
        while len(sample) < n_sample:
            index = random.randint(0, len(dataset) - 1)
            sample.append(dataset[index])
        return sample

    def _random_features(self, dataset):
       
        n_features = self.n_features or len(dataset[0]) - 1
        return random.sample(range(len(dataset[0]) - 1), n_features)

    def _build_tree_with_random_features(self, dataset, features):
       
        def get_best_split_with_features(dataset, features):
            class_values = list(set(row[-1] for row in dataset))
            best_index, best_value, best_score, best_groups = None, None, float('inf'), None
            for index in features:
                for row in dataset:
                    groups = test_split(index, row[index], dataset)
                    gini = gini_index(groups, class_values)
                    if gini < best_score:
                        best_index, best_value, best_score, best_groups = index, row[index], gini, groups
            return {'index': best_index, 'value': best_value, 'groups': best_groups}

        root = get_best_split_with_features(dataset, features)
        split(root, self.max_depth, self.min_size, 1, features, get_best_split_with_features)
        return root

    def fit(self, dataset):
        
        for _ in range(self.n_trees):
            sample = self._subsample(dataset)
            features = self._random_features(dataset)
            tree = self._build_tree_with_random_features(sample, features)
            self.trees.append(tree)

    def predict_row(self, row):

        predictions = [predict(tree, row) for tree in self.trees]
        return Counter(predictions).most_common(1)[0][0]

    def predict(self, dataset):
       
        return [self.predict_row(row) for row in dataset]

# テストデータ
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

# ランダムフォレストの学習と予測
rf = my_RandomForestClassifier(n_trees=5, max_depth=3, min_size=1, sample_size=0.8, n_features=2)
rf.fit(dataset)
predictions = rf.predict(dataset)

# 結果表示
for i, row in enumerate(dataset):
    print(f"Expected: {row[-1]}, Predicted: {predictions[i]}")
