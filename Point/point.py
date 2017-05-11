# coding: utf-8
from PySide.QtCore import QPoint

__author__ = 'Andres'


class Point(QPoint):
	def eightNeighbors(self):
		leftNeighbors = [Point(self.x()-1, y) for y in range(self.y()-1, self.y()+2)]
		rightNeighbors = [Point(self.x()+1, y) for y in range(self.y()-1, self.y()+2)]
		topNeighbor = [Point(self.x(), self.y()+1)]
		bottomNeighbor = [Point(self.x(), self.y()-1)]

		return leftNeighbors + rightNeighbors + topNeighbor + bottomNeighbor
