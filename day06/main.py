from functools import reduce

def part1(data):
	data = preprocess(data)

	lines = data.splitlines()

	ops = lines[-1].split(' ')
	lines = lines[:-1]

	lines = zip(*(line.strip().split(' ') for line in lines if line))

	total = 0
	for i, line in enumerate(lines):
		if line:
			gen = (int(s) for s in line)
			if ops[i] == '*':
				t = reduce(lambda x, y: x * y, gen)
				total += t
			elif ops[i] == '+':
				t = sum(gen)
				total += t

	return total	

def part2(data):
	...



def preprocess(data: str):
	# dirty trick
	for _ in range(8):
		data = data.replace('  ', ' ')

	return data


tc = '''
123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +
'''


def test_part1():
	assert part1(tc) == 4277556


if __name__ == "__main__":
	with open("input.txt") as f:
		data = f.read().strip()

	print("Part 1:", part1(data))
	print("Part 2:", part2(data))
