from mpl_toolkits.basemap import Basemap
import matplotlib.pyplot as plt
import numpy as np


def generate_wind_fild_to_north():
    return


def main():
    plt.figure()

    b = Basemap(projection="npstere", lon_0=340, boundinglat=55)
    b.drawcoastlines()

    # get the pole coords in the projected coords
    xpole, ypole = b(0, 90)


    nx, ny = 600, 600
    x1d = np.linspace(xpole - 0.95 * abs(xpole),  xpole + 0.95 * abs(xpole), nx)
    y1d = np.linspace(ypole - 0.95 * abs(ypole),  ypole + 0.95 * abs(ypole), ny)

    yy, xx = np.meshgrid(y1d, x1d)

    # b.scatter(xx, yy)

    b.scatter(*b(0, 90), c="r")

    ue, ve = np.zeros_like(xx), np.ones_like(xx) * 0.005

    # ue[:, :] = 1
    # ve[:, :] = 0

    urot, vrot = b.rotate_vector(ue, ve, *b(xx, yy, inverse=True))

    stride = 20
    b.quiver(xx[::stride, ::stride], yy[::stride, ::stride], urot[::stride, ::stride], vrot[::stride, ::stride], scale=0.2, width=0.003)


    plt.show()

if __name__ == '__main__':
    main()