from bs4 import BeautifulSoup
import urllib
import glob


# Directory Path
dir_path = "/home/avi/Desktop/Learning/Web-Scraping/images/drone/"		# path to directoy where images will be saved
image_name = "drone"	# Name of the Image to be saved
url_dir_path = "/home/avi/Downloads/"	# path where url files exist
file_name = "urls.txt"

list_images = glob.glob("%s/*.jpg"%(dir_path))
num_images = len(list_images)
c_initial = num_images
i = 1
c = 0
# Get the image no. of last image in the directory
for i in range(num_images):
	a, b = list_images[i].rsplit('_')
	a, b = b.rsplit('.')
	if(c < int(a)):
 		c = int(a)

url_file = open((url_dir_path + file_name), "r")
images_src = url_file.readlines()
L = len(images_src)	# L stores no. of images that are available for downloading

print("Printing all the image sources")
for src in images_src:
	print(src)

print(f"Number of images present in the directory : {c}")
print(f"Number of new images that may be added : {L}")

for src in images_src:
	try:
		c = c + 1
		full_path = dir_path + image_name + '_' + str(c) + '.jpg'
		#print(urllib.request.urlretrieve(src, full_path))
		urllib.request.urlretrieve(src, full_path)
		percent_download = int((i/L)*100)
		i = i + 1
		print(f'{percent_download}% Download Complete')
	except:
		i = i + 1
		continue
c_final = len(glob.glob("%s/*.jpg"%(dir_path)))
print(f"Total number of images after running the scrip : {c_final}")
total = c_final - c_initial
print(f"Total number of Images actually downloaded : {total}")