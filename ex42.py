import numpy as np

class LogisticRegression:
    def __init__(self, learning_rate=0.01, tol=1e-7, max_iter=1000):
        self.learning_rate = learning_rate
        self.tol = tol
        self.max_iter = max_iter
        self.weights = None

    def sigmoid(self, z):
        return 1 / (1 + np.exp(-z))

    def fit(self, X, y):
        # バイアス項を含めるため、Xに1の列を追加
        X = np.c_[np.ones(X.shape[0]), X]
        self.weights = np.zeros(X.shape[1])

        for i in range(self.max_iter):
            # 線形予測値 z の計算
            z = np.dot(X, self.weights)
            predictions = self.sigmoid(z)
            
            # 勾配の計算
            gradient = np.dot(X.T, (predictions - y)) / y.size
            gradient_norm = np.linalg.norm(gradient)
            
            # パラメータの更新
            self.weights -= self.learning_rate * gradient
            
            # デバッグ用の出力
            print(f"Iteration {i+1}, Gradient norm: {gradient_norm}")

            # 収束判定
            if gradient_norm < self.tol:
                print(f"収束しました。反復回数: {i+1}")
                break
        else:
            print("最大反復回数に達しました")

    def predict_proba(self, X):
        X = np.c_[np.ones(X.shape[0]), X]  # バイアス項を追加
        return self.sigmoid(np.dot(X, self.weights))

    def predict(self, X):
        return (self.predict_proba(X) >= 0.5).astype(int)
