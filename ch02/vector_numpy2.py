import numpy as np

# --- ベクトルの定義 ---
v1 = np.array([6, 4])
v2 = np.array([3, -1])

print("ベクトル v1:", v1)
print("ベクトル v2:", v2)
print("-" * 30)

# --- ベクトルの和 ---
v_sum = v1 + v2
print("v1 + v2 =", v_sum)

# --- ベクトルの差 ---
v_diff = v1 - v2
print("v1 - v2 =", v_diff)

# --- 要素ごとの掛け算 ---
v_elem_mult = v1 * v2
print("v1 * v2 (element-wise) =", v_elem_mult)

# --- 要素ごとの割り算 ---
v_elem_div = v1 / v2
print("v1 / v2 (element-wise) =", v_elem_div)

# --- スカラー倍 ---
scalar = 2
v_scaled = scalar * v1
print(f"{scalar} * v1 =", v_scaled)