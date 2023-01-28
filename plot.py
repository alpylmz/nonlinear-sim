import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anim
import logging as log

# initialize a special logger
logger = log.getLogger('nonlinear_plot')
logger.setLevel(level=log.DEBUG)

fig = plt.figure()
ax = fig.add_subplot(111)
last_initial_point = [0, 0]

def onclick(event):
    global last_initial_point
    last_initial_point[0] = event.xdata
    last_initial_point[1] = event.ydata
    logger.error("clicked: x: %s, y: %s", event.xdata, event.ydata)
    pass

cid = fig.canvas.mpl_connect('button_press_event', onclick)

def update_plot(i):
    ax.clear()
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    ax.plot(
        [last_initial_point[0], 
        last_initial_point[0] + 1,
        last_initial_point[0] + 2,
        last_initial_point[0] + 3,], 
        [last_initial_point[1], 
        last_initial_point[1] + 1,
        last_initial_point[1] + 2,
        last_initial_point[1] + 3,])
           
a = anim.FuncAnimation(fig, update_plot, frames = 60)

plt.show()
