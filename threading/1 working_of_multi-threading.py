
# This Code is to check how multitreading works
from threading import *
def new():
	for x in range(6):
		print("Statement being executed by child thread : ", current_thread().getName())
		

if __name__ == '__main__':
	t = Thread(target = new)
	print("Hello from : ", current_thread().getName())
	t.start()
	t.join()
	print("Bye from : ", current_thread().getName())
