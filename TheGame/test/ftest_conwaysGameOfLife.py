# coding: utf-8
from unittest import TestCase

from Point.point import Point
from TheGame.conwaysGameOfLife import ConwaysGameOfLife

__author__ = 'Andres'


class TestConwaysGameOfLife(TestCase):
	def testACellWithLessThanTwoLiveNeighboursDies(self):
		aPoint = Point(1, 2)

		aGameOfLife = ConwaysGameOfLife(anArrayOfPointsIndicatingAliveCells=[aPoint])
		aGameOfLife.nextGeneration()

		self.assertFalse(aGameOfLife.isAlive(aPoint))

	def testACellWithTwoOrThreeNeighboursLives(self):
		aPoint = Point(1, 1)
		anSquareOfPoints = [aPoint] + aPoint.eightNeighbors()
		aPointWithTwoNeighborsInTheSquare = Point(2, 3)
		aPointWithThreeNeighborsInTheSquare = Point(0, 0)

		anArrayOfPointsIndicatingAliveCells = anSquareOfPoints + [aPointWithTwoNeighborsInTheSquare]

		aGameOfLife = ConwaysGameOfLife(anArrayOfPointsIndicatingAliveCells=anArrayOfPointsIndicatingAliveCells)
		aGameOfLife.nextGeneration()

		self.assertTrue(aGameOfLife.isAlive(aPointWithTwoNeighborsInTheSquare))
		self.assertTrue(aGameOfLife.isAlive(aPointWithThreeNeighborsInTheSquare))


