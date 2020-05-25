from PIL import Image
import os
import numpy as np

Pat = np.load('Patient_ID_List.npy')


for i in range(len(Pat)):
    
    X_data = []
        
    for root, dirs, filenames in os.walk('results_without_augmentation/similarity/'+str(Pat[i])):
        for f in filenames:
            image = Image.open('results_without_augmentation/similarity/'+str(Pat[i]) +'/'+str(f))
            im = np.asarray(image)
            X_data.append (im)
    
    array = 'results_array/' + str(Pat[i])        
    np.save(array,X_data)       #Saves .npy array

#np.load('ImageArray.npy')       #To load the array file


#print('X_data shape:', list(X_data))
