
if __name__ == '__main__':
	exit(1)


from enum import Enum, auto


class Tiles(Enum):
	Start	= auto()
	Stop	= auto()
	Open 	= auto()
	Closed 	= auto()

