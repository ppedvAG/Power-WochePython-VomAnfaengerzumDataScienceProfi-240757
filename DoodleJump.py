import random
import tkinter as tk

class DoodleJumpGame:
	def __init__(self):
		self.gameSpeed = 10
		self.nextDirection = 0
		self.stepDistance = 5
		self.platforms = []
		self.highestPlatform = 0

		self.playerDimensions = (30, 50)
		self.playerPosX = 400
		self.playerPosY = 0
		self.currentHeight = 0
		self.highestHeight = 0
		self.jumpTicks = 0
		self.death = False

		self.windowWidth = 800
		self.windowHeight = 600

		self.createNewPlatforms()


	def step(self):
		if self.currentHeight < self.highestHeight - self.windowHeight and self.jumpTicks <= 0:
			self.death = True

		# Move Screen
		for platform in self.platforms:
			platform[1] += 3 if self.jumpTicks <= 0 else -3

		# Update Backend Variables
		self.currentHeight += 3 if self.jumpTicks > 0 else -3
		self.highestHeight += 3 if self.jumpTicks > 0 and self.highestHeight < self.currentHeight else 0
		self.jumpTicks -= 1
		if self.nextDirection == 0 and self.playerPosX >= self.stepDistance:
			self.playerPosX -= self.stepDistance
		elif self.nextDirection == 1 and self.playerPosX <= self.windowWidth - self.playerDimensions[0] - self.stepDistance:
			self.playerPosX += self.stepDistance

		# Check Collisions
		for platform in self.platforms:
			if  self.windowHeight - platform[1] <= self.playerPosY + self.playerDimensions[1] <= self.windowHeight - platform[1] + 5 and \
				self.playerPosX <= platform[0] + platform[2] and self.playerPosX + self.playerDimensions[0] >= platform[0]:
				self.jumpTicks = 120
				break  # Player can only hit one Platform at a time, skip all other collision checks

		self.updatePlatforms()

		if hasattr(self, "window"):
			self.updateUI()


	def updatePlatforms(self):
		# Remove Platforms that are too low
		toRemove = []
		for p in self.platforms:
			if p[1] < -100:
				toRemove.append(p)

		for r in toRemove:
			self.platforms.remove(r)

		self.createNewPlatforms()


	def createNewPlatforms(self):
		# newAmount = 7 - self.highestHeight // 2000
		# if newAmount < len(self.platforms):
		# 	return

		for i in range(7 - len(self.platforms)):
			newWidth = (100 - self.highestHeight // 200) + random.randint(0, 20)
			if newWidth < 10:
				newWidth = 10

			newX = random.randint(0, self.windowWidth - newWidth)
			newY = self.highestPlatform + self.windowHeight / 7
			newY = int(newY)
			self.highestPlatform = newY
			self.platforms.append([newX, newY - self.highestHeight, newWidth])


	def listenKeys(self, event):
		key = event.keysym
		stepDistance = 5
		if key == "Left" and self.playerPosX >= stepDistance:
			self.playerPosX -= stepDistance
		if key == "Right" and self.playerPosX <= self.windowWidth - self.playerDimensions[0] - stepDistance:
			self.playerPosX += stepDistance


	def updateUI(self):
		if self.death:
			try:
				self.window.destroy()
				return
			except:
				return

		# Draw Player + Highest Marker + Update Title
		self.window.wm_title(f"Score: {self.highestHeight}, JumpTicks: {self.jumpTicks}")
		self.uiPlayer.place(x=self.playerPosX, y=self.playerPosY)
		markerHeight = self.windowHeight / 2 - (self.highestHeight - self.currentHeight - self.playerDimensions[1])
		self.heightMarker.place(x=0, y=markerHeight if markerHeight > 0 else 0)

		# Redraw Platforms
		for p in self.uiPlatforms:
			p.destroy()
		self.uiPlatforms.clear()

		for x, y, width in self.platforms:
			if y > self.highestHeight + self.windowHeight + 100:  # Skip out of Screen Platforms
				continue
			platform = tk.Label(bg="lightblue")
			platform.place(x=x, y=self.windowHeight + 5 - y, width=width, height=5)
			self.uiPlatforms.append(platform)

		if __name__ == "__main__":
			self.window.after(self.gameSpeed, self.step)


	def initUI(self):
		self.window = tk.Tk()
		self.window.geometry(f"{self.windowWidth}x{self.windowHeight}")
		self.window.resizable(False, False)
		self.window.config(bg="white")

		# Init Player
		self.playerPosY = self.windowHeight / 2
		self.uiPlayer = tk.Label(bg="lightgreen")
		self.uiPlayer.place(width=self.playerDimensions[0], height=self.playerDimensions[1], x=self.playerPosX, y=self.playerPosY)
		self.heightMarker = tk.Label(bg="Red")
		self.heightMarker.place(width=20, height=5, x=0, y=self.highestHeight)

		# Init Platforms
		self.uiPlatforms = []
		self.platforms.append([0, 0, self.windowWidth])
		platform = tk.Label(bg="lightblue")
		platform.place(x=0, y=self.windowHeight - 5, width=self.windowWidth, height=5)
		self.uiPlatforms.append(platform)


	def startUILoop(self):
		self.initUI()
		self.window.bind("<KeyPress>", self.listenKeys)
		self.window.after(self.gameSpeed, self.step)
		self.window.mainloop()


	def setupUI(self):  # UI für Model
		if not hasattr(self, "window"):
			self.initUI()


if __name__ == '__main__':
	game = DoodleJumpGame()
	game.startUILoop()