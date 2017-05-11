# coding: utf-8
__author__ = 'Andres'


class ConwaysGameOfLife(object):
	def __init__(self, anArrayOfPointsIndicatingAliveCells):
		self._aliveCells = anArrayOfPointsIndicatingAliveCells

	def nextGeneration(self):
		aliveCells = []
		for cell in self._aliveCells:
			neighborsCount = 0
			aCellsNeighbors = cell.eightNeighbors()
			for anotherCell in self._aliveCells:
				if anotherCell in aCellsNeighbors:
					neighborsCount += 1
			if 2 <= neighborsCount <= 3:
				aliveCells.append(cell)

		self._aliveCells = aliveCells

	def isAlive(self, aPoint):
		return aPoint in self._aliveCells
