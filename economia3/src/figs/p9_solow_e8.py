import sys; sys.path.insert(0, "../lib")
from econ_style import *

alpha = 0.4
s = 0.25
dn = 0.08  # delta + n
kstar = (s / dn) ** (1 / (1 - alpha))
ystar = kstar ** alpha
inv_star = s * ystar

k = np.linspace(0.02, 13.2, 400)
f = k ** alpha
sf = s * k ** alpha
dep = dn * k

fig, ax = new_fig(6.3, 3.9)
ax.plot(k, f, color=C["blue"], lw=LW)
ax.plot(k, sf, color=C["orange"], lw=LW)
ax.plot(k, dep, color=C["aqua"], lw=LW)
econ_axes(ax, r"$k$", r"$y$", xlim=(0, 15.6), ylim=(0, 3.15))
label_curve(ax, 13.2, 13.2 ** alpha, r"$f(k)=k^{0,4}$", C["blue"], dx=6, dy=4)
label_curve(ax, 13.2, s * 13.2 ** alpha, r"$sf(k)=0{,}25\,k^{0,4}$", C["orange"], dx=6, dy=-2)
label_curve(ax, 13.2, dn * 13.2, r"$(\delta{+}n)k=0{,}08\,k$", C["aqua"], dx=6, dy=6)
vguide(ax, kstar, ystar, label=r"$k^*{=}6{,}68$")
hguide(ax, kstar, ystar, label=r"$y^*{=}2{,}14$")
point(ax, kstar, ystar, color=C["blue"])
point(ax, kstar, inv_star, color=C["orange"], dx=6, dy=-14, label=None)
save(fig, "p9_solow_e8")
