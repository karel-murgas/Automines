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

import random as rnd
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
        """Create empty minefield"""

        return [[Cell(r, c) for c in range(self.cols)] for r in range(self.rows)]

    def populate(self, r0, c0):
        """Populate minefield with mines"""

        def place_mine(pot_rows, pot_cols):
            """Place mine in one of available cells"""

            row = rnd.choice(pot_rows)
            col = rnd.choice(pot_cols[row])
            self.map[row][col].mined = True
            return mark_as_full(pot_rows, pot_cols, row, col)

        def mark_as_full(pot_rows, pot_cols, row, col):
            """Eliminate cell form pool of minable cells"""

            pot_cols[row].remove(col)
            if not pot_cols[row]:
                pot_rows.remove(row)
            return pot_rows, pot_cols

        pot_rows = [r for r in range(self.rows)]
        pot_cols = [[c for c in range(self.cols)] for r in pot_rows]

        pot_rows, pot_cols = mark_as_full(pot_rows, pot_cols, r0, c0)

        for m in range(self.mines):
            pot_rows, pot_cols = place_mine(pot_rows, pot_cols)


class Cell(pyg.sprite.Sprite):
    """One cell (field) on the map"""

    def __init__(self, row, col, mined=False, status='neutral', size=CELLSIZE):
        pyg.sprite.Sprite.__init__(self)
        self.row = row
        self.col = col
        self.status = status
        self.rect = pyg.Rect(row*size, col*size, size, size)
        self.image = pyg.Surface((size, size))
        self.load_image(status)
        self.mined = mined

    def load_image(self, status):
        """Gets required image"""

        img = pyg.image.load(GRAPHICS['folder'] + GRAPHICS['cell'][status])
        self.image.blit(img, (0, 0))
