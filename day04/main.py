
def part1(data: str):
	# going to assume we can eagerly convert lines to list
	lines = [line for line in data.split()]
	# marked = [[c for c in line] for line in lines]

	# for line in lines:
	# 	print(line)
	m = len(lines)
	n = len(lines[0])

	accessible = 0
	for j in range(m):
		for i in range(n):
			if lines[i][j] == '@':
				# count surrounding rolls
				rolls = 0
				for k in range(i - 1, i + 2):
					for l in range(j - 1, j + 2):
						if k < 0 or l < 0 or k >= m or l >= n or (k == i and l == j):
							continue
						if lines[k][l] == '@':
							rolls += 1
				if rolls < 4:
					accessible += 1
					# marked[i][j] = 'x'

	# for line in marked:
	# 	print(''.join(line))
	return accessible


def part2(data: str):
	# going to assume we can eagerly convert lines to list
	lines = [[c for c in line] for line in data.split()]

	m = len(lines)
	n = len(lines[0])

	total_removed = 0
	accessible = -1

	# do until no more accessible
	while accessible != 0:

		# count and mark for removal
		accessible = 0
		for j in range(m):
			for i in range(n):
				if lines[i][j] == '@':
					# count surrounding rolls
					rolls = 0
					for k in range(i - 1, i + 2):
						for l in range(j - 1, j + 2):
							if k < 0 or l < 0 or k >= m or l >= n or (k == i and l == j):
								continue
							if lines[k][l] == '@':
								rolls += 1
					if rolls < 4:
						accessible += 1
						lines[i][j] = 'x'

		total_removed += accessible

		# remove marked
		for j in range(m):
			for i in range(n):
				if lines[i][j] == 'x':
					lines[i][j] = '.'

	return total_removed


tc = '''
..@@.@@@@.
@@@.@.@.@@
@@@@@.@.@@
@.@@@@..@.
@@.@@@@.@@
.@@@@@@@.@
.@.@.@.@@@
@.@@@.@@@@
.@@@@@@@@.
@.@.@@@.@.
'''

def test_part1():
	assert part1(tc) == 13

def test_part2():
	assert part2(tc) == 43

if __name__ == "__main__":
	with open("input.txt") as f:
		data = f.read().strip()

	print("Part 1:", part1(data))
	print("Part 2:", part2(data))

