# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 10:11:21 2016

@author: armnkch
"""

import config

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib import gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable


nc_file = config.DATA_DIR.joinpath('iceh_inst.2003-01-02-00000.nc')
fh = Dataset(str(nc_file), mode='r')

lons = fh.variables['ULON'][:]
lats = fh.variables['ULAT'][:]
thikness = fh.variables['hi'][:].squeeze()
tmask = fh.variables['tmask'][:]
uvel = fh.variables['uvel'][:].squeeze()*100
vvel = fh.variables['vvel'][:].squeeze()*100


uvel[:, :] = 0
vvel[:, :] = 1


print(uvel.shape)
print(lons.shape)
speed = np.sqrt(uvel**2 + vvel**2)
vmin=np.min(speed); vmax=np.max(speed)

print(speed.max()) ; print(np.mean(speed)); print(np.std(speed))
#UN = uvel/speed ; VN = vvel/speed

#print fh.variables['hi'].units

#lon_0=-60.; lat_0=90.
m = Basemap(projection='npstere',boundinglat=55,lon_0=340,resolution='l', round=False)

xi, yi = m(lons, lats)

print(xi[0, :])
print(xi.min(), xi.max())

urot, vrot = m.rotate_vector(uvel, vvel, lons, lats)



#yy = np.arange(0, yi.shape[0], 10)
#xx = np.arange(0, xi.shape[1], 10)
#points = np.meshgrid(yy, xx)


plt.figure(figsize=(12,12))
ax = plt.gca()

#levs=np.arange(0.01,0.2,0.005)
cs = m.pcolor(xi,yi,urot,vmin=None, vmax=None)

stride = 10
Q = m.quiver(xi[::stride, ::stride], yi[::stride, ::stride], urot[::stride, ::stride], vrot[::stride, ::stride], scale=700)
qK = plt.quiverkey(Q, 0.1, 0.9, 10, '10 cm/s', labelpos='W')


m.drawmeridians(np.arange(-180, 190, 10))
m.drawparallels(np.arange(-90, 100, 10))

#divider = make_axes_locatable(ax)
#cax = divider.append_axes("right", size="5%", pad=0.1)
#plt.colorbar(cs, cax=cax)
m.drawcoastlines(ax=ax)
cb = m.colorbar(cs, "bottom", size="5%", pad="2%")
cb.set_label('cm/s')
plt.show()




