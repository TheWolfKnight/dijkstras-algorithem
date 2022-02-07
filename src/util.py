
if __name__ == "__main__":
	exit(1)


def readFile(fName: str, path_prefix: str="'/") -> list[list[chr]]:
	r: list[list[chr]] = []
	data: str = None
	with open(f"tmp.txt") as fp:
		data: str = fp.read()
	assert data, "No data in file"
	tmp: list[chr] = []
	for c in data:
		if c == "\n":
			r.append(tmp.copy())
			tmp = []
			continue

		tmp.append(c)
	if tmp:
		r.append(tmp.copy())
	return r


def cleaner(li2d: list[list[chr]]) -> list[list[chr]]:
	r: list[list[chr]] = []
	for li in li2d:
		tmp: list[chr] = []
		for c in li:
			if validChr(c):
				tmp.append(c)
			else:
				raise ValueError
		if r:
			assert len(tmp)+2 == len(r[0]), "The dimensions of all nested lists, must be equal"
		tmp.insert(0, 'X')
		tmp.append('X')
		r.append(tmp.copy())
		tmp = []
	i: int = r[0]
	r.insert(0, ['X']*len(i))
	r.append(['X']*len(i))
	return r

