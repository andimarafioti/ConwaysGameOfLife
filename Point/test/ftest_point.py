# coding: utf-8
from unittest import TestCase

from Point.point import Point

__author__ = 'Andres'


class testPoint(TestCase):
	def testAPointHasEightNeighbors(self):
		aPoint = Point(2, 3)

		neighbors = aPoint.eightNeighbors()

		self.assertTrue(len(neighbors) == 8)
