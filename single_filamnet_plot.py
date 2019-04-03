
import aplpy
import matplotlib.pyplot as plt
import numpy as np


totalFilamentNumber = 5

for ii in range(totalFilamentNumber):
	print (ii)
	try:
		fig = plt.figure()
		f = aplpy.FITSFigure('/scratch/aaghabab/disperse/hcn/HCN_spw11_imsmooth_subimage_moment0.fits', figure=fig)
		#f.add_label(351.45, 1.1,'Moment 0')
		f.show_colorscale(cmap = 'gray_r', vmax = 150) 
		#f.set_nan_color('#DCDCDC')
		filData = np.loadtxt('/scratch/aaghabab/disperse/hcn/filaments/filament' + str(ii) + '.txt')
		x,y = filData[:,0],filData[:,1]
		plt.plot(x,y, '.', markersize=0.6)
		f.ticks.show()
		f.ticks.set_color('black')
		f.tick_labels.show()
		#f.set_xaxis_coord_type('scalar')
		#f.set_yaxis_coord_type('latitude')
		f.tick_labels.set_font(size='small', weight='medium', stretch='normal', family='serif', style='normal', variant='normal')
		f.tick_labels.set_xformat('ddd.dd')
		f.tick_labels.set_yformat('d.dd')
		#f.tick_labels.set_xformat('hh:mm:ss')
		#f.tick_labels.set_yformat('dd:mm:ss')
		#f.ticks.set_xspacing(0.04) 
		#f.ticks.set_yspacing(0.03)
		f.ticks.set_length(5)
		#f.add_colorbar()
		#f.colorbar.show()
		#f.colorbar.set_axis_label_text('km/s')
		#f.colorbar.set_width(0.1)
		#f.colorbar.set_font(size='small', weight='medium', stretch='normal', family='sans-serif', style='normal', variant='normal')+
		#plt.savefig('/home/beck/projects/NGC6334/disperse/Filaments/Filament' + str(ii) + '.png', dpi = 300)
		plt.show()
	except (IOError,IndexError):
		pass
