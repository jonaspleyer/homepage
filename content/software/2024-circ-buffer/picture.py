import numpy as np
import matplotlib.pyplot as plt
from matplotlib.patches import Circle

n_elements = 17
radius_small = 6
radius_large = 10

fig, ax = plt.subplots(figsize=(8, 8))

c1 = Circle((0, 0), radius_large, fill=True, facecolor="#abb1cf")
c2 = Circle((0, 0), radius_small, fill=True, facecolor="white")

ax.add_patch(c1)
ax.add_patch(c2)

dtheta = 2 * np.pi / n_elements
for n in range(n_elements):
    theta = np.pi / 2 - dtheta * n
    x = np.array([radius_small, radius_large]) * np.cos(theta)
    y = np.array([radius_small, radius_large]) * np.sin(theta)
    ax.plot(x, y, c="white")

    phi = theta - dtheta / 2
    if n == n_elements - 2:
        text = ".."
    elif n == n_elements - 1:
        text = "$x_n$"
    else:
        text = f"$x_{{{n}}}$"
    ax.text(
        (radius_small + radius_large) / 2 * np.cos(phi),
        (radius_small + radius_large) / 2 * np.sin(phi),
        text,
        fontsize="xx-large",
        horizontalalignment="center",
        verticalalignment="center",
    )

ax.text(
    0,
    0,
    "circ_buffer",
    fontsize="xx-large",
    horizontalalignment="center",
    verticalalignment="center",
)

ax.set_xlim((-10, 10))
ax.set_ylim((-10, 10))
ax.set_axis_off()

fig.savefig("circ-buffer-scheme.png")
plt.show()
