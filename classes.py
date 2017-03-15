"""Defines classes for Automines"""
#    Copyright (C) 2017  Karel "laird Odol" Murgas
#    karel.murgas@gmail.com
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.


#############
# Libraries #
#############

import pygame as pyg
from constants import *


#######################
# Classes definitions #
#######################


class Minefield():
    """Map of the minefield"""

    def __init__(self, rows, columns, mines):
        self.rows = rows
        self.cols = columns
        self.mines = mines
        self.map = self.create_empty_field()

    def create_empty_field(self):
        """Creates empty minefield"""

        return [[Cell(r, c) for c in range(self.cols)] for r in range(self.rows)]


class Cell(pyg.sprite.Sprite):
    """One cell (field) on the map"""

    def __init__(self, row, col, status='clear', size=CELLSIZE):
        pyg.sprite.Sprite.__init__(self)
        self.status = status
        self.image = pyg.Surface((size, size))
        self.load_image('neutral')
        self.row = row
        self.col = col

    def load_image(self, status):
        """Gets required image"""

        img = pyg.image.load(GRAPHICS['folder'] + GRAPHICS['cell'][status])
        self.image.blit(img, (0, 0))
