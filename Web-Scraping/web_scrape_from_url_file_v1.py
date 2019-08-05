from bs4 import BeautifulSoup
import urllib
import glob
##############################################################################################
# Required Variables For the Code                                                            #
##############################################################################################
# Directory Path
dir_path = "/home/avi/Desktop/Learning/Web-Scraping/images/drone/"		# path to directoy where images will be saved
image_name = "drone"	# Name of the Image to be saved
url_dir_path = "/home/avi/Downloads/"	# path where url files exist
file_name = "urls3.txt"
##############################################################################################
def image_lister():
	c = 0

	list_images = glob.glob("%s/*.jpg"%(dir_path))
	num_images = len(list_images)
		
	# Get the image no. of last image in the directory
	for i in range(num_images):
		a, b = list_images[i].rsplit('_')
		a, b = b.rsplit('.')
		if(c < int(a)):
	 		c = int(a)

	print(f"Number of images present in the directory : {num_images}")
	return(c, num_images)

def image_downloader( images_src, c, c_initial ):
	i = 1
	L = len(images_src)	# L stores no. of images that are available for downloading
	print(f"Number of new images that may be added : {L}")
	for src in images_src :
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

if __name__ == '__main__':
	
	index, num = image_lister()

	url_file = open((url_dir_path + file_name), "r")
	read_lines = url_file.readlines()

	image_downloader(read_lines, index, num)

	url_file.close()