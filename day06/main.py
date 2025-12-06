from math import prod

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
			total += sum(gen) if ops[i] == '+' else prod(gen)

	return total	

def part2(data: str):
    lines = data.strip().split('\n')

    number_rows = lines[:-1]
    op_row = lines[-1]

    operations = [ch for ch in op_row if ch in '+*']

    total = 0
    current_numbers = []

    # walk columns from right to left
	# extra -1 step to force a final flush at i == -1
    for i in range(len(number_rows[0]) - 1, -2, -1):
        if i == -1 or all(row[i] == ' ' for row in number_rows):
            if current_numbers:
                op = operations.pop()
                if op == '+':
                    total += sum(current_numbers)
                elif op == '*':
                    total += prod(current_numbers)
                current_numbers = []
        else:
            column_chars = ''.join(row[i] for row in number_rows)
            num_str = column_chars.strip()
            if num_str:
                current_numbers.append(int(num_str))

    return total


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

def test_part2():
	assert part2(tc) == 3263827

if __name__ == "__main__":
	with open("input.txt") as f:
		data = f.read().strip()

	print("Part 1:", part1(data))
	print("Part 2:", part2(data))
