from bs4 import BeautifulSoup
import urllib
import requests
import glob

images = []
images_src = []

url = "https://unsplash.com/search/photos/drone"
request = requests.get(url) # insert link here
soup = BeautifulSoup(request.text, 'lxml')


images = soup.findAll('img') # Finds all the <img> tags
print(images)

for image in images:
	src = str(image.get('src'))	# Create a list of all image sources
	images_src.append(src)

print('\n\nPrinting all the sources', images_src)

# Directory Path
dir_path = "/home/avi/Desktop/Learning/Web-Scraping/images/drone/"		# path to directoy where images will be saved
file_name = "drone"	# Name of the Image to be saved

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
L = len(images_src)

print(f"Number of images present in the directory : {c}")
print(f"Number of new images that will be added : {L}")

for src in images_src:
	try:
		c = c + 1
		full_path = dir_path + file_name + '_' + str(c) + '.jpg'
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