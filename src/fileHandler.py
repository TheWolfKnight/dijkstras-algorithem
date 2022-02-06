
if __name__ == '__main__':
	exit(1)



class FileHandler(object):
	"""
	A class To handle the input file, this will be how the program gets it's data
	"""

	def __init__(self, s_pathPrefix: str="./"):
		self.s_pathPrefix = s_pathPrefix

	def readFile(self, s_fName: str) -> list[list[chr]]:
		pass
