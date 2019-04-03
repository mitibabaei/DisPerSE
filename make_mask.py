from astropy.io import fits
import numpy as np
import aplpy
import matplotlib.pyplot as plt
from astropy.io import fits
from astropy import wcs
from astropy import coordinates
from astropy import units as u
import os

fitsfile = fits.open('HCN_spw11_imsmooth_subimage_moment0.fits', cache=True)
hdu = fitsfile[0]
print(hdu.data.shape)
data = hdu.data
header = hdu.header

w = wcs.WCS(hdu.header)

data[data==np.nan]=0
data[data>-1e18]=1
fits.writeto('mask.fits', data, header)
#png.writeto('mask_hcn.png', data, header)
plt.show()
