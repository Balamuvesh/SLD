import sys
import argparse
import pickle
import math
import numpy as np
from numpy import reshape
from numpy import array
test=[]

def dysgraphia(test):
	classifier_f = open("current_classifiers/dysgraphia_classifier.pickle", "rb")
	dclassifier = pickle.load(classifier_f)
	classifier_f.close()
	test=array(test)
	test_new= test = test.reshape(1, -1)
	predictions =dclassifier.predict(test_new)
	return predictions

def apd(test):
	classifier_f = open("current_classifiers/apd_classifier.pickle", "rb")
	dclassifier = pickle.load(classifier_f)
	classifier_f.close()
	test=array(test)
	test_new= test = test.reshape(1, -1)
	predictions =dclassifier.predict(test_new)
	return predictions
def gad(test):
	classifier_f = open("current_classifiers/gad_classifier.pickle", "rb")
	dclassifier = pickle.load(classifier_f)
	classifier_f.close()
	test=array(test)
	test_new= test = test.reshape(1, -1)
	predictions =dclassifier.predict(test_new)
	return predictions

def main(test):
	text_index=test[0]
	test=test[1:]
	if(text_index==0):
		result=dysgraphia(test)
	elif(text_index==1):
		result=apd(test)
	elif(text_index==2):
		result=gad(test)
	print(result)

