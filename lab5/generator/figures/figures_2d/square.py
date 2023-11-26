from generator.figures.figure import Figure
from generator.colors.colors import paintText


class Square(Figure):
    def __init__(self):
        super().__init__()

    def generateSquare(self):
        n = self.size
        line = ''
        if n > 1:
            line += n * 2 * '_'
        else:
            line += '_'

        top_line = ' ' + line
        bottom_line = '|' + line + '|' + '\n'

        inner_spaces = n * 2 * ' '
        inner_fill = '|' + inner_spaces + '|'
        content = ''

        i = 1
        while (i < n):
            content += inner_fill + '\n'
            i += 1

        square = top_line + '\n' + content + bottom_line
        return square

    def generateFigure(self):
        generated = self.generateSquare()
        colored = paintText(generated, self.color)
        return colored
