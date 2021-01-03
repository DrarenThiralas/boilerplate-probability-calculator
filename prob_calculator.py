import copy
import random
# Consider using the modules imported above.

class Hat:

	def __init__(self, **kwargs):
		self.contents = []
		for item in kwargs.items():
			color, amount = item
			self.contents += [color for i in range(amount)]

	def draw(self, amount):
		toReturn = []
		if amount >= len(self.contents):
			toReturn += self.contents
			self.contents = []
		else:
			for i in range(amount):
				toDraw = random.randint(0, len(self.contents)-1)
				toReturn += [self.contents[toDraw]]
				self.contents = self.contents[:toDraw]+self.contents[toDraw+1:]

		return toReturn


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
	random.seed()
	successes = 0

	for i in range(num_experiments):
		tempHat = copy.deepcopy(hat)
		drawnList = tempHat.draw(num_balls_drawn)
		drawnDict = {}
		for ball in drawnList:
			if ball in drawnDict:
				drawnDict[ball] += 1
			else:
				drawnDict[ball] = 1
		experimentSuccess = True
		for item in expected_balls.items():
			ball, amount = item
			if ball not in drawnDict:
				experimentSuccess = False
			else:
				if drawnDict[ball] < amount:
					experimentSuccess = False

		if experimentSuccess:
			successes += 1

	return successes/num_experiments


