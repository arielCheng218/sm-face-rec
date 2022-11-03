#
# 	This program identifies and tags faces from the St. Mark's students and staff directory. 
# 	Built for the internal use of the St. Mark's marketing & communications department to auto-tag photos on SmugMug.
#
#		Author: Ariel Cheng, Class of '25
# 	Date: 10/25/2022
#

# TODO use multiple photos as training data see wiki here https://github.com/ageitgey/face_recognition/wiki/Face-Recognition-Accuracy-Problems#question-face-recognition-works-well-with-european-individuals-but-overall-accuracy-is-lower-with-asian-individuals
# TODO cross-reference no media list
# TODO test accuracy of model and refine
# TODO make some form of UI

# FIXME duplicate name problem??

import os
import shutil
import face_recognition

# clean data
PATH = "./data/train/"

# constants
TOLERANCE = 0.45

name_to_count = {}

for directory in os.listdir(PATH):
	for file_name in os.listdir(f"{PATH}{directory}/"):
		# Isolate person_name
		person_name = file_name
		if "2020" in file_name:
			first_ind_of_2 = file_name.find("2")
			person_name = file_name[:first_ind_of_2]
			if person_name[-1] == "." or person_name[-1] == "_":
				person_name = person_name[:-1]
		if "JPG" in file_name:
			first_ind_of_JPG = person_name.find(".JPG")
			person_name = person_name[:first_ind_of_JPG]
		# Make directory for them, if it does not exist
		if os.path.exists(f"{PATH}{person_name}"):
			print(f"Path for {person_name} exists.")
			name_to_count[person_name] += 1
		else:
			print(f"Path for {person_name} does not exist. Adding new directory.")
			os.mkdir(f"{PATH}/{person_name}")
			name_to_count[person_name] = 1
		# Rename image
		old_file_path = f"{PATH}{directory}/{file_name}"
		new_image_name = f"{PATH}{directory}/" + person_name + str(name_to_count[person_name]) + ".JPG"
		os.rename(old_file_path, new_image_name)
		# Move renamed image into directory
		destination_path = f"{PATH}/{person_name}"
		shutil.move(new_image_name, destination_path)