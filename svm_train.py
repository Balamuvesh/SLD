import pandas as pd  
import numpy as np  
import matplotlib.pyplot as plt  
#%matplotlib inline
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.metrics import classification_report, confusion_matrix
import pickle


def train(X,y):
	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.33)
	svclassifier = SVC(kernel='linear',C=2**-5,gamma=1)  
	svclassifier.fit(X_train, y_train)
	y_pred = svclassifier.predict(X_test)
	 
 	#print(confusion_matrix(y_test,y_pred))  
	print(classification_report(y_test,y_pred)) 
	#print(len(y_pred))
	return(svclassifier)

def dysgraphia():	
	dysgraphiadata = pd.read_csv("Dysgraphia.csv") 
	dysgraphiadata.shape 
	dysgraphiadata.head()
	X = dysgraphiadata.drop(dysgraphiadata.columns[-1], axis=1)  
	y = dysgraphiadata[dysgraphiadata.columns[-1]]
	print("\t\tDysgraphia classification report\n")
	dysgraphia_classifier=train(X,y)
	f = open('dysgraphia_classifier.pickle', 'wb')
	pickle.dump(dysgraphia_classifier,f)
	f.close()
def apd():
	apd_data = pd.read_csv("APD.csv") 
	apd_data.shape 
	apd_data.head()
	X = apd_data.drop(apd_data.columns[-1], axis=1)
	print("\t\tAPD classification report\n")
	y = apd_data[apd_data.columns[-1]]
	apd_classifier=train(X,y)
	f = open('apd_classifier.pickle', 'wb')
	pickle.dump(apd_classifier,f)
	f.close()

def gad():
	gad_data = pd.read_csv("APD.csv") 
	gad_data.shape 
	gad_data.head()
	X = gad_data.drop(gad_data.columns[-1], axis=1)  
	y = gad_data[gad_data.columns[-1]]
	print("\t\tGAD classification report\n")
	gad_classifier=train(X,y)
	f = open('gad_classifier.pickle', 'wb')
	pickle.dump(gad_classifier,f)
	f.close()



def main():
	while(True):
		n=input("Which classifier needs to be retrained?\n\t1.Dysgraphia\n\t2.Auditory Processing Disorder\n\t3.Generalized Anxiety Disorder\n\t4.Exit\nInput:")
		if(n=='1'):
			dysgraphia()
		elif(n=='2'):
			apd()
		elif(n=='3'):
			gad()
		elif(n=='4'):
			print("Exiting training program")
			break;
main()





