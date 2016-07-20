# -*- coding: utf-8 -*-
"""
Created on Fri Jul  8 10:11:21 2016

@author: armnkch
"""

from netCDF4 import Dataset
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap
from matplotlib import gridspec
from mpl_toolkits.axes_grid1 import make_axes_locatable


nc_file = 'iceh_inst.2003-01-02-00000.nc'
fh = Dataset(nc_file, mode='r')

lons = fh.variables['ULON'][:]
lats = fh.variables['ULAT'][:]
thikness = fh.variables['hi'][:].squeeze()
tmask = fh.variables['tmask'][:]
uvel = fh.variables['uvel'][:].squeeze()
vvel = fh.variables['vvel'][:].squeeze()

print(uvel.shape)
print(lons.shape)
speed = np.sqrt(uvel**2 + vvel**2)
vmin=np.min(speed); vmax=np.max(speed)

print(speed.max()) ; print(np.mean(speed)); print(np.std(speed))
#UN = uvel/speed ; VN = vvel/speed

#print fh.variables['hi'].units


# Plotting with cartopy
import cartopy
import cartopy.crs as ccrs

fig = plt.figure()
vector_crs = ccrs.PlateCarree()
ax = plt.axes(projection=ccrs.NorthPolarStereo(central_longitude=-40.0))

#ax.add_feature(cartopy.feature.OCEAN, zorder=0)
#ax.add_feature(cartopy.feature.LAND, zorder=0, edgecolor='black')

#ax.gridlines()
stride = 5
ax.quiver(lons[::stride, ::stride], lats[::stride, ::stride], uvel[::stride, ::stride], vvel[::stride, ::stride], transform=vector_crs, scale=50)
fig.savefig("vecplot_cartopy.png")
