
def parse_input(text: str):
	blocks = text.strip().split("\n\n")
	ranges_block, ingredients_block = blocks

	ranges = []
	for line in ranges_block.splitlines():
		line = line.strip()
		if not line:
			continue
		lo_str, hi_str = line.split("-")
		lo, hi = int(lo_str), int(hi_str)
		if lo > hi:
			lo, hi = hi, lo  # just in case
		ranges.append((lo, hi))

	ingredients = []
	for line in ingredients_block.splitlines():
		line = line.strip()
		if not line:
			continue
		ingredients.append(int(line))

	return ranges, ingredients


def merge_ranges(ranges):
	if not ranges:
		return []

	ranges.sort(key=lambda r: r[0])

	merged = []
	cur_start, cur_end = ranges[0]

	for start, end in ranges[1:]:
		if start <= cur_end + 1:
			cur_end = max(cur_end, end)
		else:
			merged.append((cur_start, cur_end))
			cur_start, cur_end = start, end

	merged.append((cur_start, cur_end))
	return merged


def count_fresh_ids(ranges, ingredients):
	"""
	ranges must be merged (non-overlapping, sorted)
	ingredients are sorted
	"""
	merged_ranges = merge_ranges(ranges)
	ingredients_sorted = sorted(ingredients)

	fresh_count = 0
	i = 0 
	j = 0

	while i < len(ingredients_sorted) and j < len(merged_ranges):
		x = ingredients_sorted[i]
		lo, hi = merged_ranges[j]

		if x < lo:
			# ingredient before current range ⇒  spoiled
			i += 1
		elif x > hi:
			# ingredient after current range ⇒  try next range
			j += 1
		else:
			# lo <= x <= hi ⇒ fresh
			fresh_count += 1
			i += 1

	# remaining ingredients are after all ranges ⇒  spoiled
	return fresh_count


def part1(data):
	ranges, ingredients = parse_input(data)
	return count_fresh_ids(ranges, ingredients)

def part2(data):
	ranges, _ = parse_input(data)
	merged_ranges = merge_ranges(ranges)
	return sum(r[1]-r[0]+1 for r in merged_ranges)

tc = '''
3-5
10-14
16-20
12-18

1
5
8
11
17
32
'''

def test_part1():
	assert part1(tc) == 3


def test_part2():
	assert part2(tc) == 14

if __name__ == "__main__":
	with open("input.txt") as f:
		data = f.read().strip()

	print("Part 1:", part1(data))
	print("Part 2:", part2(data))

