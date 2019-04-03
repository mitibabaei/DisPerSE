
import aplpy
import matplotlib.pyplot as plt
import numpy as np


totalFilamentNumber = 25

fig = plt.figure(figsize=(15, 10))
f = aplpy.FITSFigure('/scratch/aaghabab/disperse/hcn/HCN_spw11_featherAutoMasking_peak_new.fits', figure=fig)
#f.add_label(351.45, 1.1,'Moment 0')
f.show_colorscale(cmap = 'gray_r', vmax = 1.0) 
#f.set_nan_color('#DCDCDC')

for ii in range(totalFilamentNumber):
	print (ii)
	try:
		filData = np.loadtxt('/scratch/aaghabab/disperse/hcn/filaments3/filament' + str(ii) + '.txt')
		x,y = filData[:,0],filData[:,1]
		plt.plot(x,y, '.', markersize=0.6)
	except (IOError,IndexError):
		pass

#plt.savefig('ngcFilaments.png', dpi=300)
'''
Cores1 = np.loadtxt('/home/aaghabab/Documents/scripts/disperse_filchap/Judith_beck/projects/NGC6334/Length/NGC6334-I-IN-galactic.txt')
X1 = Cores1[:,0]
Y1 = Cores1[:,1]


Cores2 = np.loadtxt('/home/aaghabab/Documents/scripts/disperse_filchap/Judith_beck/projects/NGC6334/Length/NGC6334-V-galactic.txt')
X2 = Cores2[:,0]
Y2 = Cores2[:,1]

f.show_markers(X1, Y1, s=10, facecolor='none', edgecolor='yellow')
f.show_markers(X2, Y2, s=10, facecolor='none', edgecolor='yellow')
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
'''
f.add_colorbar()
f.colorbar.show()
f.colorbar.set_axis_label_text('K[Tmb].km/s')
f.colorbar.set_width(0.1)
f.colorbar.set_font(size='small', weight='medium', stretch='normal', family='sans-serif', style='normal', variant='normal')
plt.savefig('/scratch/aaghabab/disperse/hcn/Filaments_3.png', dpi = 600)
plt.show()
