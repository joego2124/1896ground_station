#!/usr/bin/env python3
'''Animates distances and measurment quality'''
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.animation as animation

PORT_NAME = '/dev/ttyUSB0'
DMAX = 4000
IMIN = 0
IMAX = 50

def update_line(num, arr, line):
    scan = arr[0]
    offsets = np.array([(np.radians(meas[1]), meas[2]) for meas in scan])
    line.set_offsets(offsets)
    intens = np.array([meas[0] for meas in scan])
    line.set_array(intens)
    return line,

def run():
    fig = plt.figure()
    ax = plt.subplot(111, projection='polar')
    line = ax.scatter([0, 0], [0, 0], s=5, c=[IMIN, IMAX],
                           cmap=plt.cm.Greys_r, lw=0)
    ax.set_rmax(DMAX)
    ax.grid(True)

    arr = np.load("temp.npy", allow_pickle=True)

    print(arr[0])

    ani = animation.FuncAnimation(fig, update_line,
        fargs=(arr, line), interval=50)

    plt.show()

if __name__ == '__main__':
    run()