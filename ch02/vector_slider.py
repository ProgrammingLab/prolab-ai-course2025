import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation

# 初期値
vx, vy = 1.0, 0.8

# =========================
# 🎨 スタイル設定
# =========================
plt.rcParams.update({
    "axes.facecolor": "#f8f9fb",  # 背景淡いグレー
    "axes.edgecolor": "#d0d0d0",
    "grid.color": "#cccccc",
    "font.size": 11,
    "figure.facecolor": "#fafafa"
})

# =========================
# 📐 図と軸設定
# =========================
fig, ax = plt.subplots(figsize=(6, 6))
plt.subplots_adjust(left=0.12, bottom=0.28)
ax.set_aspect("equal", "box")
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.grid(True, linestyle="--", alpha=0.6)
ax.axhline(0, color="#888888", lw=0.8)
ax.axvline(0, color="#888888", lw=0.8)
ax.plot(0, 0, "o", color="#333333", ms=5)

# =========================
# 🏹 矢印要素
# =========================
arrow = None
proj_x_line, = ax.plot([], [], color="#4a90e2", lw=2, alpha=0.5)
proj_y_line, = ax.plot([], [], color="#4a90e2", lw=2, alpha=0.5)
tip_marker, = ax.plot([], [], "o", color="#e24a6b", markersize=7)
info_text = ax.text(-0.3, 1.15, "", transform=ax.transAxes,
                    va="top", fontsize=11,
                    bbox=dict(boxstyle="round,pad=0.4",
                              fc="white", ec="#cccccc", alpha=0.9))

# =========================
# 🎚️ スライダー作成
# =========================
ax_vx = plt.axes([0.15, 0.16, 0.7, 0.03], facecolor="#efefef")
ax_vy = plt.axes([0.15, 0.10, 0.7, 0.03], facecolor="#efefef")

s_vx = Slider(ax_vx, "vx", -5.0, 5.0, valinit=vx, valstep=0.01)
s_vy = Slider(ax_vy, "vy", -5.0, 5.0, valinit=vy, valstep=0.01)

# =========================
# 🔄 更新関数
# =========================
def update_plot(vx, vy):
    global arrow
    # 既存矢印を削除して再描画
    if arrow is not None:
        arrow.remove()

    # メインベクトル矢印
    arrow = ax.arrow(0, 0, vx, vy,
                     head_width=0.18, head_length=0.25,
                     fc="#e24a6b", ec="#e24a6b", lw=2.2,
                     length_includes_head=True,
                     alpha=0.9)

    # 成分線（投影）
    proj_x_line.set_data([0, vx], [0, 0])
    proj_y_line.set_data([vx, vx], [0, vy])
    tip_marker.set_data([vx], [vy])

    # テキスト
    mag = np.hypot(vx, vy)
    ang = np.degrees(np.arctan2(vy, vx))
    info_text.set_text(f"v = ({vx:.2f}, {vy:.2f})\n"
                       f"|v| = {mag:.2f}\n"
                       f"angle = {ang:.1f}°")

# =========================
# 🌀 アニメーションで常時監視
# =========================
def animate(frame):
    vx, vy = s_vx.val, s_vy.val
    update_plot(vx, vy)
    return []

ani = FuncAnimation(fig, animate, interval=30, blit=False)

# =========================
# 🚀 実行
# =========================
plt.show()
