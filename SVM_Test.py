from sklearn import utils
import pandas as pd
import pickle
import math

filename = 'SVM_Trained_Model_RBF_5Features.sav'
#filename = 'SVM_Trained_Model_RBF_8Features.sav'
#filename = 'SVM_Trained_Model_Poly.sav'
#filename = 'SVM_Trained_Model_Linear.sav'
#filename = 'SVM_Trained_Model_LinearKernel.sav'
loaded_model = pickle.load(open(filename, 'rb'))

#X = pd.read_excel('Data_SVM_Test.xlsx')
X = pd.read_excel('Data_SVM_Test_PP_10000.xlsx')
x = X.values
x_test = x[:51,1:6]
#x_test = x[:51,1:9]

Y = pd.read_excel('Data_Y_Test.xlsx')
y = Y.values
y_test = y[:51,1:]

y_test = utils.column_or_1d(y_test.ravel(), warn=True)


Correct = 0
Incorrect = 0
C0=0
C1=0
C2=0

print('\n\nTesting:\n')

for i in range(len(x_test)):
    print('\nActual class:'+str(y_test[i])+' Predicted Class: ' + str(loaded_model.predict([x_test[i]])))
    if str(y_test[i]) in str(loaded_model.predict([x_test[i]])):
        Correct+=1
        if '0' in str(y_test[i]):
            C0+=1
        if '1' in str(y_test[i]):
            C1+=1
        if '2' in str(y_test[i]):
            C2+=1       
    else:
        Incorrect+=1

acc = math.floor((Correct*100)/51)

print('\nCorrect Predictions: '+str(Correct)+'\nIncorrect Predictions: '+str(Incorrect))
print('Class 0 Correct: '+str(C0)+'\nClass 1 Correct: '+str(C1)+'\nClass 2 Correct: '+str(C2))
print('Accuracy: '+ str(acc)+'%')
