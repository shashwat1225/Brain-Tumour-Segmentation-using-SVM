#import cv2
from PIL import Image
import numpy as np
import scipy.misc

pat_id = np.load('Patient_ID_List.npy')

for a in range(len(pat_id)):
    patient = str(pat_id[a])    
    for x in range(155):
        
        img = Image.open('results_array_post-processed_25000/' + str(patient)+'/'+str(patient)+'_'+str(x)+'.png').convert('L')  # convert image to 8-bit grayscale
        WIDTH, HEIGHT = img.size
        
        data = list(img.getdata()) # convert image data to a list of integers
        # convert that to 2D list (list of lists of integers)
        data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]
           
        for i in range(WIDTH):
        	for j in range(HEIGHT):
        		if data[i][j]==1:
        			data[i][j] = 50 
        		elif data[i][j]==2:
        			data[i][j] = 90
        		elif data[i][j]==4:
        			data[i][j] = 130
         
        scipy.misc.imsave('results_without_augmentation_post-processing_25000/'+str(patient)+'/'+str(patient)+'_'+str(x)+'.png', data)
    
    print('Patient '+str(a+1)+' Done.')
