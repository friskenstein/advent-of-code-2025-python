
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

def max_k_digit_subsequence(s: str, k: int) -> int:
    n = len(s)
	# assuming string valid and long enough

    drop = n - k
    stack: list[str] = []

    for ch in s:
        while drop and stack and stack[-1] < ch:
            stack.pop()
            drop -= 1
        stack.append(ch)

    return int(''.join(stack[:k]))

def part1(data: str):
	return sum(max_two_digit_subsequence(line) for line in data.split())


def part2(data: str):
	return sum(max_k_digit_subsequence(line, 12) for line in data.split())


tc = '987654321111111\n811111111111119\n234234234234278\n818181911112111'

def test_part1():
	assert part1(tc) == 357

def test_part2():
	assert part2(tc) == 3121910778619

if __name__ == "__main__":
	with open("input.txt") as f:
		data = f.read().strip()

	print("Part 1:", part1(data))
	print("Part 2:", part2(data))

