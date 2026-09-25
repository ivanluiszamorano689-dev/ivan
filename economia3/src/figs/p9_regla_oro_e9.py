import sys; sys.path.insert(0, "../lib")
from econ_style import *

alpha = 0.4
dn = 0.08  # delta + n

s = np.linspace(0.01, 0.95, 400)
kstar = (s / dn) ** (1 / (1 - alpha))
cstar = kstar ** alpha - dn * kstar

s_oro = alpha
k_oro = (alpha / dn) ** (1 / (1 - alpha))
c_oro = k_oro ** alpha - dn * k_oro

s_e8 = 0.25
k_e8 = (s_e8 / dn) ** (1 / (1 - alpha))
c_e8 = k_e8 ** alpha - dn * k_e8

fig, ax = new_fig(6.3, 3.9)
ax.plot(s, cstar, color=C["blue"], lw=LW)
econ_axes(ax, r"$s$", r"$c^*$", xlim=(0, 1.05), ylim=(0, 2.05))
label_curve(ax, 0.66, 1.66, r"$c^*(s)=k^{*\,0,4}-0{,}08\,k^*$", C["blue"], dx=0, dy=10)
vguide(ax, s_oro, c_oro, label=r"$s_{oro}{=}\alpha{=}0{,}40$")
point(ax, s_oro, c_oro, color=C["blue"], dx=8, dy=6, label=r"$c_{oro}{=}1{,}75$")
point(ax, s_e8, c_e8, color=C["orange"], dx=8, dy=-16, label=r"$c^*_{E8}{=}1{,}60$")
save(fig, "p9_regla_oro_e9")
