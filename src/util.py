
if __name__ == "__main__":
	exit(1)


from .typ import Tile, CHAR_TO_TILE_TABLE


"""
Reads the given input file, then parse the data ready for the cleaner.
@param fName: str
@param path_prefix: str="./"
@return list[list[chr]]
"""
def readFile(fName: str, path_prefix: str="./") -> list[list[chr]]:
	# create the variables used in the function
	r: list[list[chr]] = []
	data: str = ""

	# opens the file specified by the user as fp
	with open(f"{path_prefix}/{fName}") as fp:
		# reads all line in fp, but skips the lines
		# where there is only blank spaces.
		for line in fp.readlines():
			if line in " \t\n":
				continue
			data += line

	# makes sure that some data was read, else raise the
	# "AssertionError"
	assert data, "No data in file"
	tmp: list[chr] = []
	
	# Formes the data into a useable form
	# this is an MxN matrix of letters or
	# blank spaces
	for c in data:
		# appends the line as a list to the
		# r var for return
		if c == "\n":
			r.append(tmp.copy())
			tmp = []
			continue

		tmp.append(c)

	# Makes sure all data is in the r var
	# this for when the user does not leave
	# a newline at the eof
	if tmp:
		r.append(tmp.copy())

	# returns the r var to the prog
	return r


"""
Made to clean the table for the program, to make sure only valid chr's are used
it will look up valid tiles from the typ.CHAR_TO_TILE_TABLE in "typ.py"
@param li2d: list[list[chr]]; A two dimensional list
@return list[list[Tile]]
"""
def cleaner(li2d: list[list[chr]]) -> list[list[Tile]]:
	# init the vars used in the program
	r: list[list[chr]] = []

	# starts a loop over the li2d var
	for li in li2d:
		tmp: list[chr] = []

		# loops over the chr's in the li iterrator
		for c in li:

			# tries to get the tile corresponding to the char
			# it will then append it to the list to be returned
			# if this failes the prog throws a "ValueError"
			if r:=CHAR_TO_TILE_TABLE.get(c, None):
				tmp.append(r)
			else:
				raise ValueError

		# if this is not the first run the program will try
		# to check whether the rows are of equal length
		# if found not to be it throws an "AssertionError"
		if r:
			assert len(tmp)+2 == len(r[0]), "The dimensions of all nested lists must be equal"

		# makes sure the new list has a Closed tile
		# at each end
		tmp.insert(0, Tile.Closed)
		tmp.append(Tile.Closed)

		# copy makes sure the list is not by reference
		# else this is going to be a nightmare
		r.append(tmp.copy())
		tmp = []

	# Caps off the list with closed tiles at the top and bottom
	i: int = len(r[0])
	r.insert(0, [Tile.Closed]*i)
	r.append([Tile.Closed]*i)

	# returns the r var
	return r

