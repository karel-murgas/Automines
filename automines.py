"""Main script for Automines. Covers gameplay."""
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

from classes import *


########################
# Function definitions #
########################

# TODO Vizualizace minefieldu (pygame)
# TODO Spouštění hry, input (game loop)
# TODO Po kliknutí vygenerovat miny, generování je ready
# TODO Proces odkrývání polí

def test():
    """For testing purposes only"""

    game = Minefield(*DIFFICULTY['beginner'])
    game.populate(0, 0)
    print([['mine' for x in y if x.mined is True] for y in game.map])
    init_screen()


def init_screen(width=20, height=5):
    """Gets the screen ready and draws environment"""

    screen_ = pyg.display.set_mode((width * CELLSIZE, height * CELLSIZE))
    pyg.display.set_caption('Automines')
    pyg.display.update()
    return screen_

def play():
    """Main game cycle (choose difficulty and start new game)"""

    screen = init_screen()



test()
