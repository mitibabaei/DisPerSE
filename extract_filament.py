#!/usr/bin/python
# This is a script to post process DisPerSE
# output fits skeleton.
# It extracts the filaments.

##################################
# import #########################
##################################

import sys 
import pyfits 
import numpy as np
import matplotlib.pyplot as plt
import os
import math

postProcess = True

#################################
# find a filament ###############
#################################

def findFilament( array, current_number ):
  "This function builds up a filament"
  lst2 = []
  for s in enumerate(array):
    k = s[0]
    x = array[k,0]
    y = array[k,1]
    #velo = array[k,2]
    filament_number = array[k,2] 
    if filament_number == current_number:
      lst2.extend((x,y,filament_number))#,velo))
  new_filament = np.array(lst2).reshape(-1,3)
  return new_filament

#################################
# read the data #################
# from fits     #################
#################################

#file_f		= sys.argv[1]	
# skeleton file is given by the user in the command line as the first argument
fitsfile	= pyfits.open('HCN_spw11_imsmooth_subimage_peak.fits_c0.15.up.NDskl.BRK.S008.TRIM.ASMB.fits')
data		= fitsfile[0].data
print data.shape

################################
# variables I use in the next ##
# 	      loop            ##
################################
i,j,k		= 0,0,0
# i -> x, j -> y, k -> z
i_limit, j_limit = data.shape[1], data.shape[0]#, data.shape[0]
lst 		= []

################################
# get the filaments ############
################################
print "Extracting Skeletons"
#while k < k_limit:
while j < j_limit:
  while i < i_limit:
    filament_no	= data[j,i]    
    if filament_no != 0:
      lst.extend((i, j, filament_no))
    i += 1  
  i = 0
  j += 1
j = 0 
#  k +=1
#  print k
filament_array	= np.array(lst).reshape(-1,3)
#filament_array = np.array(lst).reshape(-1,3)
#filament_array = data
print "Array shape: " + str(filament_array.shape)

if postProcess is True:
	################################
	# variables I use in the next ##
	# 	      loop            ##
	################################
	l 		= 0
	lst2		= []
	lst3 		= []
	new_list 	= []
	################################
	# number of filaments ##########
	################################
	number_of_filaments = 25  # k #filament_array.max(axis=0)[3] #k
	print "Number of extracted filaments: " + str(number_of_filaments)

	################################
	# post process filaments #######
	################################

	while l <= number_of_filaments:
	  print l
	  new_filament = findFilament(array=filament_array, current_number=l)
	  length,columns = new_filament.shape 
	  if length >= 0.0:      # 5 times the herschel beam at 250
	    print new_filament.size, str(l) + '/' + str(number_of_filaments)
	    new_list.extend((new_filament))
	    filament = np.array(new_list).reshape(-1,3) 
            #save_file = open('/home/suri/projects/carmaorion/analysis/disperse/0.1kms_resolution/OMC4/P3/filaments/filament' + str(l) + '.txt', 'w')
	    save_file = open('/scratch/aaghabab/disperse/hcn/filaments3/filament' + str(l) + '.txt', 'w')
	    np.savetxt(save_file,filament,fmt='%.4e')	  
	  new_list = []
	  lst2 = []
	  l += 1
	  
