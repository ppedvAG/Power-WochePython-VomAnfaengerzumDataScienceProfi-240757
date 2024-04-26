import random
import tkinter

class SnakeGame:
	def __init__(self):
		self.gameSpeed = 500
		self.gridSize = (21, 21)
		self.grid = [[0 for _ in range(self.gridSize[0])] for _ in range(self.gridSize[1])]  # 0: Empty, 1: Food, 10: Head, 11+: Segment

		self.direction = 2  # 0: Left, 1: Up, 2: Right, 3: Down
		self.nextDirection = 2

		# Snake Startpos
		self.grid[10][10] = 10
		self.grid[10][9] = 11
		self.grid[10][8] = 12

		self.foodPos = self.placeFood()

		# Game State Variablen
		self.headPosX = 10
		self.headPosY = 10
		self.nextStepDeleteLastPiece = True
		self.death = False
		self.steps = 0
		self.score = 0

	def placeFood(self):
		while True:
			row = random.randint(0, len(self.grid) - 1)  # Calculate 2 random positions (X, Y)
			column = random.randint(0, len(self.grid[row]) - 1)
			if self.grid[row][column] == 0:  # If empty
				self.grid[row][column] = 1  # Place food
				return row, column

	def updateSegments(self):
		highest = (0, 0, 0)
		for row in range(self.gridSize[0]):
			for col in range(self.gridSize[1]):
				if row == self.headPosY and col == self.headPosX:
					continue
				if self.grid[row][col] >= 10:  # Exclude actual head but still update old head
					self.grid[row][col] += 1
					if highest[0] < self.grid[row][col]:
						highest = (self.grid[row][col], row, col)

		if self.nextStepDeleteLastPiece:
			self.grid[highest[1]][highest[2]] = 0
		else:
			self.nextStepDeleteLastPiece = True


	def step(self):
		# Check illegal directions
		if self.nextDirection - self.direction != 2 and self.direction - self.nextDirection != 2:
			self.direction = self.nextDirection

		# Change Direction
		self.headPosX += 1 if self.direction == 2 else -1 if self.direction == 0 else 0
		self.headPosY += 1 if self.direction == 3 else -1 if self.direction == 1 else 0

		# for row in self.grid:
		# 	print(row)
		# print("---------------------------------------------------------------")

		# Move Segments and Head
		try:
			if self.headPosX > self.gridSize[1] or self.headPosY > self.gridSize[0] or self.headPosX < 0 or self.headPosY < 0:  # Border collision
				self.death = True
				return
			elif self.grid[self.headPosY][self.headPosX] == 0:  # Empty space for head
				self.grid[self.headPosY][self.headPosX] = 10
			elif self.grid[self.headPosY][self.headPosX] == 1:  # Check food Collision
				self.grid[self.headPosY][self.headPosX] = 10
				self.nextStepDeleteLastPiece = False
				self.score += 1
				self.foodPos = self.placeFood()
			else:  # Segment collision
				self.death = True
			self.updateSegments()
		except IndexError:
			self.death = True

		self.steps += 1

		if hasattr(self, "window"):
			self.updateUI()


	def listenKeys(self, event):
		key = event.keysym
		self.nextDirection = 0 if key == "Left" else 1 if key == "Up" else 2 if key == "Right" else 3 if key == "Down" else self.nextDirection


	def updateUI(self):
		if self.death:
			try:
				self.window.destroy()
			except: pass
			return

		self.window.wm_title(f"Score: {self.score}")
		for row in range(self.gridSize[0]):
			for col in range(self.gridSize[1]):
				currentElement = self.grid[row][col]
				currentLabel = self.labelList[f"{row}-{col}"]
				if currentElement == 0:
					currentLabel.config(bg="#000")
				if currentElement == 1:
					currentLabel.config(bg="#FF0000")
				if currentElement == 10:
					currentLabel.config(bg="#00FF00")
				if currentElement > 10:
					currentLabel.config(bg="#006600")
		if __name__ == "__main__":
			self.window.after(self.gameSpeed, self.step)


	def startUILoop(self):
		self.window = tkinter.Tk()
		self.labelList = dict()
		self.window.geometry(f"{self.gridSize[0] * 20}x{(self.gridSize[1] + 1) * 20}")
		self.window.resizable(False, False)
		self.window.config(bg="black")
		for row in range(self.gridSize[0]):
			for col in range(self.gridSize[1]):
				label = tkinter.Label()
				label.grid(row=row, column=col, sticky="W")
				label.config(bg="#000", width=2, height=1)
				self.labelList[f"{row}-{col}"] = label
		self.window.bind("<KeyPress>", self.listenKeys)
		self.window.after(self.gameSpeed, self.step)
		self.window.mainloop()

	def setupUI(self):
		if hasattr(self, "window"):
			return

		self.window = tkinter.Tk()
		self.labelList = dict()
		self.window.geometry(f"{self.gridSize[0] * 20}x{(self.gridSize[1] + 1) * 20}")
		self.window.resizable(False, False)
		self.window.config(bg="black")
		for row in range(self.gridSize[0]):
			for col in range(self.gridSize[1]):
				label = tkinter.Label()
				label.grid(row=row, column=col, sticky="W")
				label.config(bg="#000", width=2, height=1)
				self.labelList[f"{row}-{col}"] = label


if __name__ == '__main__':
	game = SnakeGame()
	game.startUILoop()