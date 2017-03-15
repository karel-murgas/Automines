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


##########################
# Global initializations #
##########################

DIFFICULTY = {
    'beginner': (8, 8, 10),
    'intermediate': (16, 16, 40),
    'expert':  (24, 24, 99)
}

CELLSIZE = 20

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