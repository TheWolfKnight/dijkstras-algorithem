
if __name__ == "__main__":
	exit(1)


# import from pip or std python
from os.path import isfile, isdir
from json import loads


"""
Reads the given input file, and returns a dict with the data.
@param fName: str
@param path_prefix: str="./"
@return list[list[chr]]
"""
def readFile(fName: str, path_prefix: str="./") -> dict:
	# makes sure the input file is a json file
	assert fName.endswith(".json"), "The input file must be a json file!"

	# initialize the data variable for storing the the read data
	data: dict = {}

	# reads the input file and loads the json into the data variable
	with open(f"{path_prefix}/{fName}") as fp:
		# uses loads from the json module which converts a json object
		# into a python dict
		data = loads(fp.read())

	# returns the data variable
	return	data

