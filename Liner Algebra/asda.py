import sys
import argparse
import numpy as np
from matplotlib import animation
from matplotlib import pyplot as plt

# Get LaTeX to work
plt.rc('text', usetex=True)
plt.rc('text.latex', preamble=r'\usepackage{braket}')

# Command line parser
parser = argparse.ArgumentParser()
parser.add_argument('-f', type=str, default=None, metavar='FILE',
                    help='Input file. Cols: time |1><1| |1><2| |2><1| |2><2|')
parser.add_argument('-m', choices=['bw', 'color'], default='bw',
                    help='Black & white or color mode')
args = parser.parse_args()

# Input file handling
try:
    dat = np.genfromtxt(args.f)
except TypeError:
    time = np.arange(1000)*0.01
    oodat = (1 + np.cos(time))/2
    oddat = np.ones_like(oodat)*0.1
    ttdat = (1 + -np.cos(time))/2
    dat = np.column_stack((time, oodat, oddat, oddat, ttdat))
except IOError:
    print(f"Could not find input file {args.f}")
    sys.exit()
              
# Element fills, cahnge RGB values to desired values for color mode
if args.m == 'bw':
    otcol = str(dat[0, 1])
    oocol = str(dat[0, 2])
    tocol = str(dat[0, 3])
    ttcol = str(dat[0, 4])
else:
    otcol = (1., 0., 0., dat[0, 1])
    oocol = (1., 1., 0., dat[0, 2])
    tocol = (0., 1., 1., dat[0, 3])
    ttcol = (0., 0., 1., dat[0, 4])

# Shift, side length and border width
s = 10
b = 0.1
l = s - 2*b

# Element artists
oo = plt.Rectangle((0+b, s+b), l, l, fc=oocol)     # |1><1|
ot = plt.Rectangle((s+b,s+b), l, l, fc=otcol)      # |1><2|
to = plt.Rectangle((0+b, 0+b), l, l, fc=tocol)     # |2><1|
tt = plt.Rectangle((s+b, 0+b), l, l, fc=ttcol)     # |2><2|

# PLT figure
fig, ax = plt.subplots(dpi=100)
ax.set_xlim([-1, 21])
ax.set_ylim([-1, 21])
plt.axis("off")

# Element label color
if args.m == 'bw':
    lc = 'r'  # For B&W: red
else:
    lc = 'k'  # For color: black

# Animation functions
def init():
    for a in [oo, ot, to, tt]:
        ax.add_artist(a)
    ool = plt.text(s/2, s*3/2, r"$\ket{1}\!\bra{1}$",
                   color=lc, fontsize='x-large', ha='center', va='center')
    otl = plt.text(s*3/2, s*3/2, r"$\ket{1}\!\bra{2}$",
                   color=lc, fontsize='x-large', ha='center', va='center')
    tol = plt.text(s/2, s/2, r"$\ket{2}\!\bra{1}$",
                   color=lc, fontsize='x-large', ha='center', va='center')
    ttl = plt.text(s*3/2, s/2, r"$\ket{2}\!\bra{2}$",
                   color=lc, fontsize='x-large', ha='center', va='center')
    return oo, ot, to, tt, ool, otl, tol, ttl,

def animate(frame):
    if args.m == "bw":
        oo.set_facecolor(str(dat[frame, 1]))
        ot.set_facecolor(str(dat[frame, 2]))
        to.set_facecolor(str(dat[frame, 3]))
        tt.set_facecolor(str(dat[frame, 4]))
    else:
        oo.set_facecolor((1., 0., 0., dat[frame, 1]))
        ot.set_facecolor((1., 1., 0., dat[frame, 2]))
        to.set_facecolor((0., 1., 1., dat[frame, 3]))
        tt.set_facecolor((0., 0., 1., dat[frame, 4]))
    ool = plt.text(s/2, s*3/2, r"$\ket{1}\!\bra{1}$",
                   color=lc, fontsize='x-large', ha='center', va='center')
    otl = plt.text(s*3/2, s*3/2, r"$\ket{1}\!\bra{2}$",
                   color=lc, fontsize='x-large', ha='center', va='center')
    tol = plt.text(s/2, s/2, r"$\ket{2}\!\bra{1}$",
                   color=lc, fontsize='x-large', ha='center', va='center')
    ttl = plt.text(s*3/2, s/2, r"$\ket{2}\!\bra{2}$",
                   color=lc, fontsize='x-large', ha='center', va='center')
    return oo, ot, to, tt, oo, ot, to, tt, ool, otl, tol, ttl,

anim = animation.FuncAnimation(fig, animate, init_func=init,
                               frames=len(dat), interval=len(dat)//30,
                               blit=True)

# anim.save('animation.gif', fps=60, writer='pillow')

plt.show()