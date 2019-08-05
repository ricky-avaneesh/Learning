# Creating threads by extending the thread class
"""

When extending the tread class one can only over-write run and init method
other than these two functions no function can be over-written by the child class

"""
import threading
from threading import current_thread
class A( threading.Thread ):
	def run(self):
		for x in range(6):
			print("Child = ", current_thread().getName())

obj= A()
obj.start()
obj.join()
print("Control returned to", current_thread().getName())