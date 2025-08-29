# Try saving a shorter version to avoid timeout during export
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation, PillowWriter

np.random.seed(12)
N_total = 120
box = (0.0, 1.0, 0.0, 1.0)
sep_x = 0.5
frames = 120      # shorter animation for saving
dt = 0.02
speed = 0.25
ball_size = 110

N_per_class = N_total // 2
epsilon = 0.01
X_blue = np.random.uniform(sep_x - 0.30, sep_x - epsilon, N_per_class)
X_red  = np.random.uniform(sep_x + epsilon, sep_x + 0.30, N_per_class)
Y_blue = np.random.uniform(box[2] + 0.03, box[3] - 0.03, N_per_class)
Y_red  = np.random.uniform(box[2] + 0.03, box[3] - 0.03, N_per_class)
X = np.concatenate([X_blue, X_red]).astype(float)
Y = np.concatenate([Y_blue, Y_red]).astype(float)
labels = np.array([0]*N_per_class + [1]*N_per_class)

angles = np.random.uniform(0, 2*np.pi, N_total)
VX = speed * np.cos(angles)
VY = speed * np.sin(angles)

def reflect_on_walls(X, Y, VX, VY, xmin, xmax, ymin, ymax, radius=0.0):
    X_next = X + VX*dt
    Y_next = Y + VY*dt
    hit_left  = X_next < xmin + radius
    hit_right = X_next > xmax - radius
    VX[hit_left | hit_right] *= -1.0
    X_next = np.clip(X + VX*dt, xmin + radius, xmax - radius)
    hit_bottom = Y_next < ymin + radius
    hit_top    = Y_next > ymax - radius
    VY[hit_bottom | hit_top] *= -1.0
    Y_next = np.clip(Y + VY*dt, ymin + radius, ymax - radius)
    return X_next, Y_next, VX, VY

def shannon_entropy(counts):
    total = np.sum(counts)
    if total == 0:
        return 0.0
    p = counts / total
    p = p[p > 0]
    return float(-(p * np.log2(p)).sum())

def entropies(X, labels, sep):
    left_mask = X < sep
    right_mask = ~left_mask
    left_counts = np.array([np.sum((labels==0) & left_mask),
                            np.sum((labels==1) & left_mask)], dtype=float)
    right_counts = np.array([np.sum((labels==0) & right_mask),
                             np.sum((labels==1) & right_mask)], dtype=float)
    H_left = shannon_entropy(left_counts)
    H_right = shannon_entropy(right_counts)
    H_sum = H_left + H_right
    return H_left, H_right, H_sum, left_counts, right_counts

fig, (ax_box, ax_plot) = plt.subplots(1, 2, figsize=(11.5, 5.8))
plt.subplots_adjust(wspace=0.25)
ax_box.set_xlim(box[0], box[1])
ax_box.set_ylim(box[2], box[3])
ax_box.set_aspect('equal', adjustable='box')
ax_box.set_xticks([]); ax_box.set_yticks([])
sep_line = ax_box.axvline(sep_x, linestyle='--', linewidth=1, color="black")
scat = ax_box.scatter([], [], s=ball_size, edgecolor="k")
txt_box = ax_box.text(0.02, 0.98, "", transform=ax_box.transAxes, va='top', fontsize=9)

ax_plot.set_xlim(0, frames)
ax_plot.set_ylim(0, 2.05)
ax_plot.set_xlabel("Frame")
ax_plot.set_ylabel("Entropy (bits)")
line_left,   = ax_plot.plot([], [], label="H_left")
line_right,  = ax_plot.plot([], [], label="H_right")
line_sum,    = ax_plot.plot([], [], label="H_sum (left+right)")
ax_plot.legend(loc="lower right", fontsize=9)

H_left_hist, H_right_hist, H_sum_hist, H_global_hist = [], [], [], []

def init():
    scat.set_offsets(np.c_[[], []])
    for ln in (line_left, line_right, line_sum):
        ln.set_data([], [])
    txt_box.set_text("")
    ax_box.set_title("Balls mixing (free motion, wall bounces)")
    ax_plot.set_title("Entropy over time")
    return scat, sep_line, line_left, line_right, line_sum, txt_box

def update(frame):
    global X, Y, VX, VY
    X[:], Y[:], VX[:], VY[:] = reflect_on_walls(X, Y, VX, VY, *box)
    colors = np.where(labels==0, "blue", "red")
    scat.set_offsets(np.c_[X, Y])
    scat.set_facecolors(colors)
    scat.set_edgecolors("black")

    H_left, H_right, H_sum, left_counts, right_counts = entropies(X, labels, sep_x)
    H_left_hist.append(H_left)
    H_right_hist.append(H_right)
    H_sum_hist.append(H_sum)

    t = np.arange(1, len(H_left_hist) + 1)
    line_left.set_data(t, H_left_hist)
    line_right.set_data(t, H_right_hist)
    line_sum.set_data(t, H_sum_hist)

    txt_box.set_text(
        f"Left [blue, red]: {left_counts.astype(int)} | H_left={H_left:.2f}\n"
        f"Right [blue, red]: {right_counts.astype(int)} | H_right={H_right:.2f}\n"
        f"H_sum={H_sum:.2f} | frame {frame+1}/{frames}"
    )
    return scat, sep_line, line_left, line_right, line_sum, txt_box

anim = FuncAnimation(fig, update, init_func=init, frames=frames, interval=60, blit=True)

gif_path = "entropia.gif"
try:
    anim.save(gif_path, writer=PillowWriter(fps=12))
    saved_msg = f"Saved GIF to {gif_path}"
except Exception as e:
    saved_msg = f"Could not save GIF: {e}"

saved_msg
