class Safe:
	def __init__(self, numbers: int, initial: int=50):
		self.numbers = numbers
		self.dial = initial
		self.count_zeros = 0
		self.count_zero_passes = 0

	def turn(self, direction: str, steps: int, /):
		if direction == 'L':
			if steps >= self.dial:
				laps = (1 + ((steps - self.dial) // self.numbers))
				if self.dial == 0:  # first 'lap' doesn't count if the dial is already at zero
					laps -= 1
				self.count_zero_passes += 1 * laps
			self.dial = (self.dial - steps) % self.numbers
		elif direction == 'R':
			if steps >= (self.numbers - self.dial):
				laps = (1 + ((steps - (self.numbers - self.dial)) // self.numbers))
				self.count_zero_passes += 1 * laps
			self.dial = (self.dial + steps) % self.numbers

		# side-effect
		if self.dial == 0:
			self.count_zeros += 1


def part1(data: str, safe: Safe | None = None) -> int:
	if safe is None:
		safe = Safe(100)

	for line in data.split():
		safe.turn(line[0], int(line[1:]))

	return safe.count_zeros


def part2(data: str, safe: Safe | None = None) -> int:
	"""password method 0x434C49434B
	"""
	
	if safe is None:
		safe = Safe(100)

	for line in data.split():
		safe.turn(line[0], int(line[1:]))

	return safe.count_zero_passes


def test_part1():

	s = Safe(100, 50)

	ops = '\n'.join([ 'L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82' ])

	assert part1(ops, s) == 3
	assert s.dial == 32

def test_part2():
	ops = '\n'.join([ 'L68', 'L30', 'R48', 'L5', 'R60', 'L55', 'L1', 'L99', 'R14', 'L82' ])

	assert part2(ops) == 6

	ops = '\n'.join([ 'R1000' ])

	assert part2(ops) == 10


if __name__ == "__main__":
	with open("input.txt") as f:
		data = f.read().strip()
	print("Part 1:", part1(data))
	print("Part 2:", part2(data))
