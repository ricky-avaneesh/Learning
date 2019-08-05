# Creating threads without extending the thread class
"""



"""
from  threading import Thread

class ex:
	def B(self):
		lst = [2,1,'w',8.7,'abc']
		for x in lst:
			print("Child thread printing ", x)

obj = ex()
t1 = Thread(target = obj.B)
t1.start()
t1.join()
print("Done")