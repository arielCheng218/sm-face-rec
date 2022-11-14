import numpy as np
from PIL import Image
import os

# constants
PATH = "./data/train/"

def is_same(image1, image2):
	image1_arr = Image.open(image1)
	image2_arr = Image.open(image2)
	return image1_arr.size == image2_arr.size and not(np.bitwise_xor(image1_arr, image2_arr).any())

# remove duplicates in data
for person in os.listdir(PATH):
	full_path = f"{PATH}{person}/"
	image_names = [filename for filename in os.listdir(full_path)]
	images_to_delete = []
	for i in range(len(image_names) - 1):
		image1 = full_path + image_names[i]
		image2 = full_path + image_names[i+1]
		if is_same(image1, image2):
			images_to_delete.append(image1)
	for image in images_to_delete:
			os.remove(image)
			print("Removed " + image1 + ".")