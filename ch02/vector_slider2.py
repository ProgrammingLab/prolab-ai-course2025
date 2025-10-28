import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

# 初期値
a = np.array([1.0, 0.5])
b = np.array([0.5, 1.0])

# 描画設定
fig, ax = plt.subplots(figsize=(6, 6))
plt.subplots_adjust(left=0.1, bottom=0.25)
ax.set_xlim(-3, 3)
ax.set_ylim(-3, 3)
ax.set_aspect('equal')
ax.grid(True, linestyle='--', alpha=0.6)
ax.set_title("ベクトルの和の可視化", fontsize=16, fontweight='bold')

# 矢印を描画（a, b, a+b）
arrow_a = ax.arrow(0, 0, a[0], a[1], head_width=0.15, color="#1f77b4", length_includes_head=True)
arrow_b = ax.arrow(0, 0, b[0], b[1], head_width=0.15, color="#2ca02c", length_includes_head=True)
arrow_sum = ax.arrow(0, 0, *(a + b), head_width=0.15, color="#d62728", length_includes_head=True)

# 凡例のようにテキストでラベル
label_a = ax.text(a[0]*0.6, a[1]*0.6, "a", fontsize=14, color="#1f77b4", fontweight='bold')
label_b = ax.text(b[0]*0.6, b[1]*0.6, "b", fontsize=14, color="#2ca02c", fontweight='bold')
label_sum = ax.text((a[0]+b[0])*0.5, (a[1]+b[1])*0.5, "a + b", fontsize=14, color="#d62728", fontweight='bold')

# スライダー領域
axcolor = 'lightgoldenrodyellow'
ax_a_x = plt.axes([0.15, 0.15, 0.65, 0.03], facecolor=axcolor)
ax_a_y = plt.axes([0.15, 0.1, 0.65, 0.03], facecolor=axcolor)
ax_b_x = plt.axes([0.15, 0.05, 0.65, 0.03], facecolor=axcolor)
ax_b_y = plt.axes([0.15, 0.0, 0.65, 0.03], facecolor=axcolor)

slider_a_x = Slider(ax_a_x, 'a_x', -2, 2, valinit=a[0])
slider_a_y = Slider(ax_a_y, 'a_y', -2, 2, valinit=a[1])
slider_b_x = Slider(ax_b_x, 'b_x', -2, 2, valinit=b[0])
slider_b_y = Slider(ax_b_y, 'b_y', -2, 2, valinit=b[1])

def update(val):
    # 現在のスライダー値を取得
    a = np.array([slider_a_x.val, slider_a_y.val])
    b = np.array([slider_b_x.val, slider_b_y.val])
    s = a + b

    # 矢印の再描画（安定のためclearして再描画）
    ax.clear()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 3)
    ax.set_aspect('equal')
    ax.grid(True, linestyle='--', alpha=0.6)
    ax.set_title("vector add", fontsize=16, fontweight='bold')

    # 矢印の再描画
    ax.arrow(0, 0, a[0], a[1], head_width=0.15, color="#1f77b4", length_includes_head=True)
    ax.arrow(0, 0, b[0], b[1], head_width=0.15, color="#2ca02c", length_includes_head=True)
    ax.arrow(0, 0, s[0], s[1], head_width=0.15, color="#d62728", length_includes_head=True)

    # ラベル
    ax.text(a[0]*0.6, a[1]*0.6, "a", fontsize=14, color="#1f77b4", fontweight='bold')
    ax.text(b[0]*0.6, b[1]*0.6, "b", fontsize=14, color="#2ca02c", fontweight='bold')
    ax.text(s[0]*0.5, s[1]*0.5, "a + b", fontsize=14, color="#d62728", fontweight='bold')

    fig.canvas.draw_idle()

# スライダーの更新イベント
slider_a_x.on_changed(update)
slider_a_y.on_changed(update)
slider_b_x.on_changed(update)
slider_b_y.on_changed(update)

plt.show()
