import os
import shutil

# Data cleanup utility code
# Grouped same people together into one folder with their name.

name_to_count = {}

# Constants
PATH = "./data/train/"

for directory in os.listdir(PATH):
	for file_name in os.listdir(f"{PATH}{directory}/"):
		# Isolate person_name
		person_name = file_name
		if "2020" in file_name:
			# Remove "2020" from person's name
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