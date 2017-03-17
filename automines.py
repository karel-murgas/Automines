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

# TODO input (game loop)
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


def decode_difficulty(diff):
    """Return full name of difficulty based on input"""

    if diff == 'b':
        return 'beginner'
    elif diff == 'i':
        return 'intermediate'
    elif diff == 'e':
        return 'expert'
    elif diff == 't':
        return 'test'
    else:
        return ''


def play():
    """Main game cycle (choose difficulty and start new game)"""

    difficulty = ''
    while difficulty is '':
        difficulty = decode_difficulty(input('Welcome! Please choose difficulty: Begginer / Intermediate / Expert. \n'
                                             '(b/i/e) \n'))

    game(DIFFICULTY[difficulty])


def game(difficulty):
    """Cycle for one game"""

    screen = init_screen(difficulty[0], difficulty[1])

    minefield = Minefield(*difficulty)

    [[screen.blit(cell.image, cell.rect) for cell in row] for row in minefield.map]
    pyg.display.flip()

    playing = True
    populated = False
    while playing:
        event = pyg.event.poll()

        if event.type == pyg.QUIT:  # end program
            exit()
        elif event.type == pyg.KEYDOWN:
            if event.key == pyg.K_ESCAPE:  # end program
                exit()
        elif event.type == pyg.MOUSEBUTTONDOWN:
            x, y = pyg.mouse.get_pos()
            row = math.floor(y/CELLSIZE)
            col = math.floor(x/CELLSIZE)
            if event.button == 1:
                if not populated:
                    populated = True
                    minefield.populate(row, col)
                target = minefield.map[row][col]
                target.reveal(minefield)  # TODO Change to set of fields to reveal, add while cycle and set merging
                screen.blit(target.image, target.rect)

        pyg.display.flip()





play()
