
def parse_ranges(line: str):
	parts = [p for p in line.strip().split(",") if p]
	ranges = []
	for part in parts:
		a_str, b_str = part.split("-")
		ranges.append((int(a_str), int(b_str)))
	return ranges


def invalid_nums_repeat_twice(mx, max_digits):
	invalid_nums = []

	for k in range(1, max_digits // 2 + 1):
		base = 10 ** (k - 1)
		limit = 10 ** k
		factor = 10 ** k + 1  # N = X * (10^k + 1)

		# if the smallest X gives N > mx, no reason to try bigger k
		if base * factor > mx:
			break

		for x in range(base, limit):
			n = x * factor
			if n > mx:
				break
			invalid_nums.append(n)

	invalid_nums.sort()
	return invalid_nums

def invalid_nums_repeat_3plus(mx, max_digits):
	invalid_set = set()

	# block_len = length of the repeating pattern (L)
	for block_len in range(1, max_digits):
		base = 10 ** (block_len - 1)  # smallest L-digit number (no leading zero)
		limit = 10 ** block_len  # one past largest L-digit number

		# reps = repetition count r >= 2
		max_reps = max_digits // block_len
		for reps in range(2, max_reps + 1):
			# factor = (10^(L*r) - 1) / (10^L - 1)
			ten_L = 10 ** block_len
			factor = (10 ** (block_len * reps) - 1) // (ten_L - 1)

			# if the smallest X gives N > mx, no reason to try bigger k
			if base * factor > mx:
				break

			for x in range(base, limit):
				n = x * factor
				if n > mx:
					break
				invalid_set.add(n)

	return sorted(invalid_set)


def sum_invalid_ids(ranges, repeats):
	ranges = sorted(ranges)

	merged = []
	for start, end in ranges:
		if not merged or start > merged[-1][1] + 1:
			merged.append([start, end])
		else:
			merged[-1][1] = max(merged[-1][1], end)
	ranges = [(a, b) for a, b in merged]

	mx = max(b for _, b in ranges)
	max_digits = len(str(mx))


	algorithm = {
		'twice': invalid_nums_repeat_twice,
		'three_plus': invalid_nums_repeat_3plus,
	}[repeats]
	invalid_nums = algorithm(mx, max_digits)


	total = 0
	i = 0
	for n in invalid_nums:
		while i < len(ranges) and ranges[i][1] < n:
			i += 1
		if i >= len(ranges):
			break
		if ranges[i][0] <= n <= ranges[i][1]:
			total += n

	return total


def part1(data: str):
	ranges = parse_ranges(data)
	return sum_invalid_ids(ranges, 'twice')

def part2(data: str):
	ranges = parse_ranges(data)
	return sum_invalid_ids(ranges, 'three_plus')


tc = '11-22,95-115,998-1012,1188511880-1188511890,222220-222224,1698522-1698528,446443-446449,38593856-38593862,565653-565659,824824821-824824827,2121212118-2121212124'

def test_part1():
	assert part1(tc) == 1227775554

def test_part2():
	assert part2(tc) == 4174379265

if __name__ == "__main__":
	with open("input.txt") as f:
		data = f.read().strip()

	print("Part 1:", part1(data))
	print("Part 2:", part2(data))

