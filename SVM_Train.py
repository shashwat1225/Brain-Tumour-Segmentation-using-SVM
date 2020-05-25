from sklearn import svm    			# To fit the svm classifier
from sklearn import utils
import pandas as pd
import pickle

X = pd.read_excel('Data_SVM_Train.xlsx')
x = X.values
x_train = x[:163,1:6]          # All feature vectors assigned (5 Features)
#x_train = x[:163,1:9]          # All feature vectors assigned (8 Features)

Z = pd.read_excel('Data_Y_Train.xlsx')
z = Z.values
y_train = z[:163,1:]

y_train = utils.column_or_1d(y_train.ravel(), warn=True)

##---------------Model SVM Kernels for Features----------##
C = 10  # SVM regularization parameter

##--------------------------------------------------------------------------##
# RBF Kernel
rbf_svc = svm.SVC(kernel='rbf', gamma=10, C=C).fit(x_train, y_train)
# SVC with polynomial (degree 3) kernel
#poly_svc = svm.SVC(kernel='poly', degree=3, C=C).fit(x_train, y_train)
# SVC with linear kernel
#svc = svm.SVC(kernel='linear', C=C).fit(x_train, y_train)
# LinearSVC (linear kernel)
#lin_svc = svm.LinearSVC(C=C).fit(x_train, y_train)

print('Training SVM successful.')

###------------Saving of SVM Model-----------###

filename = 'SVM_Trained_Model_RBF_5Features.sav'
#filename = 'SVM_Trained_Model_RBF_6Features.sav'
#filename = 'SVM_Trained_Model_RBF_8Features.sav'
pickle.dump(rbf_svc, open(filename, 'wb'))

"""
filename = 'SVM_Trained_Model_Poly.sav'
pickle.dump(poly_svc, open(filename, 'wb'))
filename = 'SVM_Trained_Model_Linear.sav'
pickle.dump(svc, open(filename, 'wb'))
filename = 'SVM_Trained_Model_LinearKernel.sav'
pickle.dump(lin_svc, open(filename, 'wb'))

#loaded_model = pickle.load(open(filename, 'rb'))
#result = loaded_model.score(X_test, Y_test)
"""