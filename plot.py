import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
from scipy.integrate import odeint

MU = 0.1

fig = plt.figure()
ax = fig.add_subplot(111)
clicked_point = [0, 0]

def onclick(event):
    global clicked_point
    clicked_point[0] = event.xdata
    clicked_point[1] = event.ydata
    print("clicked: x: %s, y: %s", event.xdata, event.ydata)

def van_der_pol_deriv(x, t):
    dx0 = x[1]
    dx1 = MU * (1 - x[0]**2) * x[1] - x[0]
    return np.array([dx0, dx1])

def update_plot(i):
    coords = odeint(van_der_pol_deriv, clicked_point, np.linspace(0, 100.0, 1000))
    coords = coords.tolist()
    # clear the plot
    ax.clear()
    # set the limits of the plot again
    plt.xlim(-10, 10)
    plt.ylim(-10, 10)
    ax.plot([x[0] for x in coords], [x[1] for x in coords])

cid = fig.canvas.mpl_connect('button_press_event', onclick)
a = anim.FuncAnimation(fig, update_plot, frames = 1000)

plt.show()
