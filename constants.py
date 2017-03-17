"""Initializes global variables and settings for Automines"""
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
import math


##########################
# Global initializations #
##########################


pyg.font.init()
pyg.init()


#########
# Fixed #
#########


CELLSIZE = 20

DIFFICULTY = {  # Columns, Rows, Mines
    'beginner': (8, 8, 10),
    'intermediate': (16, 16, 40),
    'expert':  (24, 24, 99),
    'test': (10, 1, 3)
}

COLORS = {  # Colors for different danger levels
    '1': (0, 0, 255),  # Intense Blue
    '2': (0, 64, 0),  # Dark Green
    '3': (204, 0, 0),  # Intense Red
    '4': (0, 0, 102),  # Dark Blue
    '5': (153, 76, 0),  # Dark Brown
    '6': (102, 255, 255),  # Light Blue
    '7': (0, 0, 0),  # Black
    '8': (128, 128, 128)  # Gray
}

DANGER_LEVEL_FONT = pyg.font.SysFont('arial', math.floor(CELLSIZE*0.9))
#pyg.font.get_default_font()
GRAPHICS = {
    'folder': 'graphics/',
    'cell': {
        'neutral': 'neutral.png',
        'clear': 'clear.png',
        'maybe': 'maybe.png',
        'danger': 'danger.png',
        'mine': 'mine.png'
    }
}