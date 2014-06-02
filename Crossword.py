import random

words = ["john", "blue", "pancakes", "eggs"]


class Puzzle:
    def __init__(self, width, height, word_list, empty_char='-'):
        self.empty_char = empty_char
        self.width = width
        self.height = height
        self.word_list = word_list
        self.grid = [empty_char * width] * height
        self.taken = []

    def randomize_list(self):
        for row_number, row in enumerate(self.grid):
            for letter_number, letter in enumerate(row):
                if letter == self.empty_char:
                    lst = list(self.grid[row_number])
                    lst[letter_number] = chr(random.randint(ord('a'), ord('z')))
                    self.grid[row_number] = ''.join(lst)

    def format_puzzle(self):
        formatted = ""
        for row in self.grid:
            for letter in row:
                formatted += letter + '  '
            formatted += '\n'
        return formatted

    def place_item(self, word, __recursion_level=0):
        if __recursion_level < 10:
            horizontal = 0
            grid = self.grid
            if horizontal:
                # region Word Sideways
                y = random.randint(0, len(grid) - 1)
                x = random.randint(0, self.width - len(word))
                to_be_taken = range(x, x + len(word))
                for row, taken_column in self.taken:
                    if row == y:
                        conflicting = [grid_letter for grid_letter in taken_column if
                                       any([new_letter for new_letter in to_be_taken if grid_letter == new_letter])]
                        if any(conflicting):
                            self.place_item(word, __recursion_level + 1)
                            return
                grid[y] = grid[y][:x] + word + grid[y][x + len(word):]
                #endregion
            else:
                # region Word Vertical
                y = random.randint(0, (len(grid) - 1) - len(word))
                x = random.randint(0, self.width-1)
                to_be_taken = range(xrange(y,y+len(word)), x)
                for row in xrange(y, y + len(word)):
                    grid[row] = grid[row][:x] + word[row-y] + grid[row][x+1:]

                #endregion
            self.taken.append([y, to_be_taken])

        else:
            return

    def __str__(self):
        return self.format_puzzle()


p = Puzzle(20, 20, ['John', 'Dog', 'Cat', 'Mouse', 'Hat', 'Shoe', 'Rabbit'])

for i in p.word_list:
    p.place_item(i.lower())

print p
