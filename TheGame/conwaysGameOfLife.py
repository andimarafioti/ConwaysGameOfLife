# coding: utf-8
from Point.point import Point

__author__ = 'Andres'


class ConwaysGameOfLife(object):
	def __init__(self, anArrayOfPointsIndicatingAliveCells):
		assert isinstance(anArrayOfPointsIndicatingAliveCells, list)
		for point in anArrayOfPointsIndicatingAliveCells:
			assert isinstance(point, Point)

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
		assert isinstance(aPoint, Point)
		return aPoint in self._aliveCells
