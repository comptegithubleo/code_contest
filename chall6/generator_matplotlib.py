import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.path import Path
import numpy as np

x1 = np.linspace(0.0, 10.0)
x2 = np.linspace(0.0, 10.0)


verts = [
   (1., 2.),  # left, bottom
   (2., 3.),  # left, top
   (3., 1.),  # right, top
   (5., 5.),  # right, bottom
   (1., 6.),  # ignored
]

codes = [
    Path.MOVETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
    Path.LINETO,
]

path = Path(verts, codes)

fig, ax1 = plt.subplots()
fig.suptitle('A tale of 2 subplots')
patch = patches.PathPatch(path, facecolor='none', lw=2)
ax1.add_patch(patch)

#ax1.plot(x1, 'o-')
ax1.set_ylabel('Damped oscillation')
ax1.set_xlim(0, 10)
ax1.set_ylim(0, 10)
plt.show()
