class Container:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[0] * width for _ in range(height)]  # Create an empty grid

    def fits(self, shape, row, col):
        """
        Check if the given shape can fit in the container at the specified row and column.
        """
        shape_height = len(shape)
        shape_width = len(shape[0])
        if row + shape_height > self.height or col + shape_width > self.width:
            return False  # Shape doesn't fit within the container bounds

        for r in range(shape_height):
            for c in range(shape_width):
                if shape[r][c] == 1 and self.grid[row + r][col + c] == 1:
                    return False  # Shape overlaps with an occupied cell

        return True

    def place(self, shape, row, col):
        """
        Place the given shape into the container at the specified row and column.
        """
        shape_height = len(shape)
        shape_width = len(shape[0])
        for r in range(shape_height):
            for c in range(shape_width):
                if shape[r][c] == 1:
                    self.grid[row + r][col + c] = 1

    def fit_shapes(self, shapes):
        """
        Fit a list of shapes into the container.
        """
        row = self.height - 1  # Start from the bottom row
        col = 0

        for shape in shapes:
            shape_height = len(shape)
            shape_width = len(shape[0])

            while col + shape_width <= self.width:
                if self.fits(shape, row, col):
                    self.place(shape, row, col)
                    col += shape_width
                else:
                    row -= 1  # Move to the row above
                    if row < 0:
                        break
                    col = 0  # Move back to the leftmost column

            if row < 0:
                break

# Define the main function
def main():
    container = Container(4, 4)
    shapes = [[[1, 1, 0], [1, 1, 1]],
              [[1, 1], [1, 1]],
              [[1, 1, 1]]]

    container.fit_shapes(shapes)

    for row in container.grid:
        print(row)

if __name__ == "__main__":
    main()
