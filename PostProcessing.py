import numpy as np
#import cv2
from scipy.ndimage import label
import scipy.misc
pat_id = np.load('Patient_ID_List.npy')


for x in range(len(pat_id)):
    segmentation_mask = np.load('results_array/'+str(pat_id[x])+'.npy') # This should be your 3D mask.
    
    # Let us create a binary mask.
    # It is 0 everywhere `segmentation_mask` is 0 and 1 everywhere else.
    binary_mask = segmentation_mask.copy()
    binary_mask[binary_mask != 0] = 1
    
    # Now, we perform region labelling. This way, every connected component
    # will have their own colour value.
    labelled_mask, num_labels = label(binary_mask)
    
    # Let us now remove all the too small regions.
    refined_mask = segmentation_mask.copy()
    minimum_cc_sum = 10000
    for lbl in range(num_labels):
        if np.sum(refined_mask[labelled_mask == lbl]) < minimum_cc_sum:
            refined_mask[labelled_mask == lbl] = 0
    
    array = 'results_array_post-processed_10000/' + str(pat_id[x])
    np.save(array,refined_mask)
    
    for i in range(155):
        temp = refined_mask[i,:,:]
        scipy.misc.imsave('results_array_post-processed_10000/' + str(pat_id[x])+'/'+str(pat_id[x])+'_'+str(i)+'.png', temp)
    
    print(str(pat_id[x])+' Done.')

"""

c0=0
c1=0
c2=0
c4=0
sl1 = 0
sl2 = 0
sl3 = 0
for i in range(155):
    for j in range(208):
        for k in range(208):
            if refined_mask[i][j][k]==0:
                c0+=1
            elif refined_mask[i][j][k]==1:
                c1+=1
            elif refined_mask[i][j][k]==2:
                c2+=1
            elif refined_mask[i][j][k]==4:
                c4+=1
                        

print('Details: \nC0= '+str(c0)+' C1= '+ str(c1)+' C2= '+ str(c2)+' C4= '+ str(c4))

"""
#--------------------------------------------------------------------------#

"""

#---------------Erosion-Dilation Test--------------#    

c0=0
c1=0
c2=0
c4=0

for i in range(155):
    for j in range(208):
        for k in range(208):
            if a[i][j][k]==0:
                c0+=1
            elif a[i][j][k]==1:
                c1+=1
            elif a[i][j][k]==2:
                c2+=1
            elif a[i][j][k]==4:
                c4+=1
                    

print('Details: \nC0= '+str(c0)+' C1= '+ str(c1)+' C2= '+ str(c2)+' C4= '+ str(c4))

kernel = np.ones((8,8),np.uint8)
e = cv2.erode(a,kernel,iterations = 1)
c0=0
c1=0
c2=0
c4=0
for i in range(155):
    for j in range(208):
        for k in range(208):
            if e[i][j][k]==0:
                c0+=1
            elif e[i][j][k]==1:
                c1+=1
            elif e[i][j][k]==2:
                c2+=1
            elif e[i][j][k]==4:
                c4+=1
                    

print('Details: \nC0= '+str(c0)+' C1= '+ str(c1)+' C2= '+ str(c2)+' C4= '+ str(c4))


d = cv2.dilate(e,kernel,iterations = 1)
c0=0
c1=0
c2=0
c4=0

for i in range(155):
    for j in range(208):
        for k in range(208):
            if d[i][j][k]==0:
                c0+=1
            elif d[i][j][k]==1:
                c1+=1
            elif d[i][j][k]==2:
                c2+=1
            elif d[i][j][k]==4:
                c4+=1
                    

print('Details: \nC0= '+str(c0)+' C1= '+ str(c1)+' C2= '+ str(c2)+' C4= '+ str(c4))

"""


