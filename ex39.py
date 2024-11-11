import numpy as np  
import pandas as pd 
import os  #ファイルやディレクトリ操作

class MyLinearRegression:
    def __init__(self):
        # モデルの初期化時に、係数と切片をNoneに設定
        self.coef_ = None  # 説明変数に対する係数を格納（モデルの重み）
        self.intercept_ = None  # 切片を格納（モデルのバイアス項）

    def fit(self, X, y):
        # モデルを学習するメソッド
        # 引数 X: 特徴量データ（説明変数の行列）
        # 引数 y: 目的変数データ（出力）

        # バイアス項（切片）のために、特徴量行列の最初の列に1を追加
        X_b = np.c_[np.ones((X.shape[0], 1)), X]  # 各サンプルの先頭に1を追加
        
        # 最小二乗法を用いて、最適なパラメータを計算
        # np.linalg.pinvで擬似逆行列を計算
        theta_best = np.linalg.pinv(X_b.T.dot(X_b)).dot(X_b.T).dot(y)
        

        self.intercept_ = theta_best[0]  # 最初の要素が切片
        self.coef_ = theta_best[1:]  # 残りの要素が係数

    def predict(self, X):
        # 学習済みモデルを使用して新しいデータに対する予測を行うメソッド
        # 引数 X: 特徴量
        
        # バイアス項のために、特徴量行列の最初の列に1を追加
        X_b = np.c_[np.ones((X.shape[0], 1)), X]  # 各サンプルの先頭に1を追加
        
        # 予測値を計算し、返す
        return X_b.dot(np.r_[self.intercept_, self.coef_])  # バイアスと係数を用いて予測計算


def load_and_clean_data(filename):
 
    data = pd.read_csv(filename)  
    # 数値データのみ選択（数値型の列だけを取得）
    data = data.select_dtypes(include=[np.number])  # 数値型の列を選択
    
    # 欠損値を含む行を削除し、NumPy配列に変換
    cleaned_data = data.dropna().values  # NaNを削除した後、NumPy配列として返す
    return cleaned_data  # 前処理されたデータを返す

# データの読み込みと前処理
X_train = load_and_clean_data("X_train.csv")  
y_train = load_and_clean_data("y_train.csv").ravel()  # 学習用の目的変数データを1次元配列に変換
X_test = load_and_clean_data("X_test.csv") 



if X_train.shape[0] != y_train.shape[0]:  # 学習データのサンプル数と目的変数の数が異なる場合
    # y_train の行数を X_train に合わせる
    if X_train.shape[0] < y_train.shape[0]:
        y_train = y_train[:X_train.shape[0]]  # y_trainをX_trainの行数に合わせて切り詰める
    else:
        X_train = X_train[:y_train.shape[0]]  # X_trainをy_trainの行数に合わせて切り詰める

# モデルのインスタンスを作成し、学習データでモデルを学習
model = MyLinearRegression()  # MyLinearRegressionのインスタンスを生成（インスタンスとはクラスから生成された具体的なオブジェクト）
model.fit(X_train, y_train)  # モデルを学習データで学習させる

#
y_pred = model.predict(X_test)  


output_dir = "../text/data"  # 予測結果を保存するディレクトリのパス
os.makedirs(output_dir, exist_ok=True)  # 指定したディレクトリが存在しない場合は作成する


pd.DataFrame(y_pred).to_csv(os.path.join(output_dir, "y_pred.csv"), index=False)  


