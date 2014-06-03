import random


class Puzzle:
    def __init__(self, word_list, width=15, height=15, empty_char='-'):
        self.empty_char = empty_char
        self.width = width
        self.height = height
        self.word_list = word_list
        self.grid = [empty_char * width] * height
        self.taken = []

    def randomize_items(self):
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
            direction = random.randint(0, 2)
            backwards = random.randint(0, 1)
            grid = self.grid
            # region Direction Handling
            if direction == 0:
                # region Horizontal word handling
                y = random.randint(0, self.height - 1)
                x = random.randint(0, self.width - len(word))
                to_be_taken = [[y, temp] for temp in range(x, x + len(word))]
                # endregion
            elif direction == 1:
                # region Vertical word handling
                y = random.randint(0, (self.height - 1) - len(word))
                x = random.randint(0, self.width - 1)
                to_be_taken = [[temp, x] for temp in range(y, y + len(word))]
                # endregion
            elif direction == 2:
                diagonal_direction = random.randint(0, 1)
                if diagonal_direction:
                    # Upwards diagonal word handling
                    y = random.randint(len(word), (self.height - 1))
                    x = random.randint(0, self.width - len(word))
                    to_be_taken = [[y - num, temp] for num, temp in enumerate(range(x, x + len(word)))]

                else:
                    # Downwards diagonal word handling
                    y = random.randint(0, (self.height - 1) - len(word))
                    x = random.randint(0, self.width - len(word))
                    to_be_taken = [[y + num, temp] for num, temp in enumerate(range(x, x + len(word)))]
            for taken_temp in self.taken:
                if taken_temp in to_be_taken:
                    self.place_item(word, __recursion_level + 1)
                    return
            if backwards:
                word = word[::-1]
            for num, (y, x) in enumerate(to_be_taken):
                grid[y] = grid[y][:x] + word[num] + grid[y][x + 1:]
            self.taken += to_be_taken
        else:
            return

    def __str__(self):
        return self.format_puzzle()


puzzle = Puzzle(
    ['John', 'Dog', 'chair', 'car', 'tree', 'fish', 'phone', 'pirate', 'bat', 'ball', 'desk', 'wallet', 'spoon',
     'washing', 'microwave', 'shed', 'motherboard'], width=20, height=20)

for i in puzzle.word_list:
    puzzle.place_item(i.lower())

puzzle.randomize_items()

print puzzle

