import numpy as np
import matplotlib.pyplot as plt

def plot_vectors(vectors, colors=None, labels=None):
    origin = np.zeros(2)
    
    plt.figure(figsize=(6,6))
    
    if colors is None:
        colors = ['r'] * len(vectors)
    if labels is None:
        labels = [''] * len(vectors)
    
    for vec, color, label in zip(vectors, colors, labels):
        plt.quiver(*origin, *vec, angles='xy', scale_units='xy', scale=1, color=color, label=label)
    
    # グラフの範囲
    all_coords = np.array(vectors)
    max_val = np.max(np.abs(all_coords)) + 1
    plt.xlim(-max_val, max_val)
    plt.ylim(-max_val, max_val)
    
    # 目盛りを1刻みに設定
    plt.xticks(np.arange(-max_val, max_val+1, 1))
    plt.yticks(np.arange(-max_val, max_val+1, 1))
    
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.gca().set_aspect('equal')
    
    if any(labels):
        plt.legend()
    plt.title("2D Vector Visualization")
    plt.show()


# 使用例
v1 = np.array([3, 4])
v2 = np.array([-2, 5])
v3 = np.array([4, -3])

plot_vectors([v1, v2, v3], colors=['r','g','b'], labels=['v1','v2','v3'])
