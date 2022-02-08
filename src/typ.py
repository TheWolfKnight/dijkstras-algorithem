
if __name__ == '__main__':
	exit(1)


from enum import Enum, auto


# This class will holde all the different types of tiles for the prog.
# This is used when there is a need to enumerate through the tiles.
class Tile(Enum):
	Start	= auto()
	Stop	= auto()
	Open 	= auto()
	Closed 	= auto()


# This table will make looking up the different tiles easy for the prog.
# To extend this simply add a new char with the corresponding tile
CHAR_TO_TILE_TABLE: dict[chr, Tile] = {
	"G": Tile.Start,
	"S": Tile.Stop,
	"O": Tile.Open,
	"X": Tile.Closed,
}

