
# from pip installs and python std
from typing import Optional
from os.path import isfile

import sys

# from locale files
from src import *


"""
A function to print a use statement
@err: list[str]
@return None
"""
def usage(err: Optional[list[str]]=None) -> None:
	print("CMD:")
	print("\tpython main.py <FLAGS> <INPUT FILE>")
	print("FLAGS:")
	print("\t-c\tUsed if the file should use the complex run type.\n\t\tHere different tile types can be used\n\t\tand find the path with the least amount of time")
	if err:
		print("ERR:")
		for e in err:
			print(f"\t{e}")
	return


"""
Takes the first element of the given list
returns the element and the rest of the list
@a: list[str]
@return tuple[str, list[str]]
"""
def chopArgv(a: list[str]) -> (str, list[str]):
	return (a[0], a[1:])


def main():
	argv = sys.argv

	# removes this files name from the argv list
	# as it will not be used
	_, argv = chopArgv(argv)

	# checks if the program was givne any CLI arguments
	# if not it will print a use statement and exit with 1
	if not argv:
		usage(["no input file was given"])
		exit(1)

	iFile, argv = chopArgv(argv)

	# makes sure the imput file is a file, and that is has the
	# correct file extension
	if not isfile(iFile) or not iFile.endswith(".json"):
		usage(["Either an invalid file was given, or it was not a text file",
			   f"The given file is: \"{iFile}\""])
		exit(1)


# safeguards against the program being run in a "wrong" way
# in all other files this will just run the "exit(1)" command
if __name__ == '__main__':
	main()
	exit(0)

