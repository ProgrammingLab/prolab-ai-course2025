import numpy as np
import matplotlib.pyplot as plt

class Vector2D:
    def __init__(self, start, end, color='r', label=None):
        """
        start: np.array([x0, y0])
        end:   np.array([x1, y1])
        color: 矢印の色
        label: ラベル文字列
        """
        self.start = np.array(start)
        self.end = np.array(end)
        self.color = color
        self.label = label

    @property
    def vec(self):
        return self.end - self.start  # ベクトルの成分

def plot_vectors(vectors):
    plt.figure(figsize=(6,6))
    
    all_points = []
    
    for v in vectors:
        plt.quiver(*v.start, *v.vec, angles='xy', scale_units='xy', scale=1, color=v.color, label=v.label)
        all_points.append(v.start)
        all_points.append(v.end)
    
    # グラフ範囲
    all_points = np.array(all_points)
    max_val = np.max(np.abs(all_points)) + 1
    plt.xlim(-max_val, max_val)
    plt.ylim(-max_val, max_val)
    
    plt.xticks(np.arange(-max_val, max_val+1, 1))
    plt.yticks(np.arange(-max_val, max_val+1, 1))
    plt.grid(True)
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.gca().set_aspect('equal')
    
    # ラベル表示
    if any(v.label for v in vectors):
        plt.legend()
    
    plt.title("2D Vector Visualization (Start → End)")
    plt.show()


# 使い方
v1 = Vector2D(start=[1, 3], end=[2, 0], color='r', label='v1')   # 左下から上
v2 = Vector2D(start=[0, 0], end=[1, 3], color='g', label='v1')   # 左下から上
v3 = Vector2D(start=[0, 0], end=[2, 0], color='b', label='v2')    # 右下から右上


plot_vectors([v1, v2, v3])
