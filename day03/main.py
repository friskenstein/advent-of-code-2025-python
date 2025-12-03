
def max_two_digit_subsequence(s: str) -> int:
    best_second = int(s[-1])
    best_value = -1

    for i in range(len(s) - 2, -1, -1):
        d1 = int(s[i])
        candidate = 10 * d1 + best_second
        if candidate > best_value:
            best_value = candidate
        if d1 > best_second:
            best_second = d1

    return best_value


def part1(data: str):
	return sum(max_two_digit_subsequence(line) for line in data.split())


def part2(data: str):
	...


tc = '987654321111111\n811111111111119\n234234234234278\n818181911112111'

def test_part1():
	assert part1(tc) == 357


if __name__ == "__main__":
	with open("input.txt") as f:
		data = f.read().strip()

	print("Part 1:", part1(data))
	print("Part 2:", part2(data))

