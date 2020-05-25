#For calculating values from segmented grayscale data

from PIL import Image
import os
import csv
import numpy as np

patient_id = np.load('Patient_ID_List.npy')
c1 = []
c2 = []
c4 = []
s_n = []
s_e = []
s_et = []


for ii in range(len(patient_id)):
    indir = 'results_array_post-processed_10000/'+str(patient_id[ii])
    
    class1=0
    class2=0
    class4=0
    s_1=0
    s_2=0
    s_4=0
    
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            #print(f)
            img = Image.open(indir+'/'+f).convert('L')  # convert image to 8-bit grayscale
            WIDTH, HEIGHT = img.size
            
            cl1=0
            cl2=0
            cl4=0
    
            data = list(img.getdata()) # convert image data to a list of integers
            # convert that to 2D list (list of lists of integers)
            data = [data[offset:offset+WIDTH] for offset in range(0, WIDTH*HEIGHT, WIDTH)]
           
            for i in range(WIDTH):
            	for j in range(HEIGHT):
            		if data[i][j]==1:
            			cl1+=1
            		elif data[i][j]==2:
            			cl2+=1
            		elif data[i][j]==4:
            			cl4+=1
            
    
            class1+=cl1
            class2+=cl2
            class4+=cl4
            if cl1!=0:
                s_1+=1
            if cl2!=0:
                s_2+=1
            if cl4!=0:
                s_4+=1
    
    print('\nPatient ID: '+str(patient_id[ii]))
    c1.append(str(class1))
    c2.append(str(class2))
    c4.append(str(class4))    
    s_n.append(str(s_1))
    s_e.append(str(s_2))
    s_et.append(str(s_4))

    
with open('Temp.csv', 'w') as csvfile:
    fieldnames = ['ID','Nec','Edema','ET','Slices_1','Slices_2','Slices_4']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
    for a in range(len(patient_id)):
        writer.writerow({'ID': str(patient_id[a]),'Nec':str(c1[a]),'Edema':str(c2[a]), 'ET': str(c4[a]), 'Slices_1': str(s_n[a]) , 'Slices_2':str(s_e[a]), 'Slices_4':str(s_et[a])})

            
    
"""  
#For calculating values from segmented colored data

from PIL import Image
import os
import csv
import numpy as np

patient_id = np.load('Patient_ID_List.npy')
c1 = []
c2 = []
c4 = []
s_n = []
s_e = []
s_et = []


for ii in range(len(patient_id)):
    indir = 'Test_Data/'+str(patient_id[ii])
    
    class1=0
    class2=0
    class4=0
    s_1=0
    s_2=0
    s_4=0
    
    for root, dirs, filenames in os.walk(indir):
        for f in filenames:
            #print(f)
            img = Image.open(indir+'/'+f)
            
            cl1=0
            cl2=0
            cl4=0
               
            for pixel in img.getdata():
                if pixel == (255,51,51): 
                    cl1 += 1
                elif pixel == (89,191,64): 
                    cl2 += 1
                elif pixel == (255,255,64): 
                    cl4 += 1
            
    
            class1+=cl1
            class2+=cl2
            class4+=cl4
            if cl1!=0:
                s_1+=1
            if cl2!=0:
                s_2+=1
            if cl4!=0:
                s_4+=1
    
    print('\nPatient ID: '+str(patient_id[ii]))
    c1.append(str(class1))
    c2.append(str(class2))
    c4.append(str(class4))    
    s_n.append(str(s_1))
    s_e.append(str(s_2))
    s_et.append(str(s_4))

    
with open('Temp.csv', 'w') as csvfile:
    fieldnames = ['ID','Nec','Edema','ET','Slices_1','Slices_2','Slices_4']
    writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
 
    writer.writeheader()
    for a in range(len(patient_id)):
        writer.writerow({'ID': str(patient_id[a]),'Nec':str(c1[a]),'Edema':str(c2[a]), 'ET': str(c4[a]), 'Slices_1': str(s_n[a]) , 'Slices_2':str(s_e[a]), 'Slices_4':str(s_et[a])})

            
"""
