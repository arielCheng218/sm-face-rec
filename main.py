"""
	This program identifies and tags faces from the St. Mark's students and staff directory. 
	Built for the internal use of the St. Mark's marketing & communications department to auto-tag photos on SmugMug.

	Author: Ariel Cheng, Class of '25
	Date: 10/25/2022

"""

# TODO figure out a way to quantify accuracy
# FIXME ACCURACY ISSUES - identifies people as known when they are supposed to be unknown.

# TODO make a function called every year so this code can be re-used
# FIXME duplicate name problem?? what if future people have same names.
# TODO make some form of UI


import face_recognition
import knn

# constants
pred = knn.predict("./data/test/naina-horning-1.jpeg", model_path="./model/knn")
print(pred)