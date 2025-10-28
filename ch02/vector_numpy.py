import numpy as np

#配列x,yの定義
x = [3, 4] 
y = [2, -1]

#配列同士の和は連結と定義されている。
print(x + y) 

#配列をベクトルへ変換する関数np.array()
x_vec = np.array(x)
y_vec = np.array(y)

#ベクトル同士の和は成分ごとの和と定義されている。
print(x_vec + y_vec) 