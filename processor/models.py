class Shape:
    """
    Represents a shape that can be placed on the grid.
    """

    def __init__(self, pattern):
        """
        Initialize a shape with the provided pattern.

        Args:
            pattern (list): The pattern of the shape, where each sublist represents a row of the shape.
        """
        self.pattern = pattern
        self.rows = len(pattern)
        self.cols = len(pattern[0])

    def rotate(self):
        """
        Rotate the shape 90 degrees clockwise.
        """
        rotated_pattern = [[0] * self.rows for _ in range(self.cols)]
        for old_row in range(self.rows):
            for old_col in range(self.cols):
                new_row = old_col
                new_col = self.rows - 1 - old_row
                rotated_pattern[new_row][new_col] = self.pattern[old_row][old_col]
        self.pattern = rotated_pattern
        self.rows, self.cols = self.cols, self.rows


class MainArray:
    """
    Represents the main grid where shapes can be placed.
    """

    def __init__(self, num_rows, num_cols):
        """
        Initialize the main grid with the specified number of rows and columns.

        Args:
            num_rows (int): Number of rows in the grid.
            num_cols (int): Number of columns in the grid.
        """
        self.num_rows = num_rows
        self.num_cols = num_cols
        self.array = [[0] * num_cols for _ in range(num_rows)]

    def can_place(self, shape, base_row, base_col):
        """
        Check if a shape can be placed at the specified position on the grid.

        Args:
            shape (Shape): The shape to be placed.
            base_row (int): The row index to start placing the shape.
            base_col (int): The column index to start placing the shape.

        Returns:
            bool: True if the shape can be placed without overlapping, False otherwise.
        """
        for shape_row in range(shape.rows):
            for shape_col in range(shape.cols):
                shape_cell = shape.pattern[shape_row][shape_col]
                grid_cell = self.array[base_row + shape_row][base_col + shape_col]
                if shape_cell == 1 and grid_cell == 1:
                    return False
        return True

    def place_shape(self, shape):
        """
        Attempt to place a shape on the grid in different rotations.

        Args:
            shape (Shape): The shape to be placed.

        Returns:
            bool: True if the shape was successfully placed, False if no suitable position is found.
        """
        for _ in range(4):  # Rotate the shape 0, 90, 180, and 270 degrees
            for base_row in range(self.num_rows - shape.rows, -1, -1):
                for base_col in range(self.num_cols - shape.cols + 1):
                    if self.can_place(shape, base_row, base_col):
                        self._fill_shape(shape, base_row, base_col)
                        return True
            shape.rotate()  # Rotate the shape before trying again
        return False

    def _fill_shape(self, shape, base_row, base_col):
        """
        Fill the grid cells with values from the shape pattern.

        Args:
            shape (Shape): The shape to be filled.
            base_row (int): The row index to start filling the shape.
            base_col (int): The column index to start filling the shape.
        """
        for shape_row in range(shape.rows):
            for shape_col in range(shape.cols):
                if shape.pattern[shape_row][shape_col] == 1:
                    self.array[base_row + shape_row][base_col + shape_col] = 1

    def display(self):
        """
        Display the current state of the grid.
        """
        for row in self.array:
            print(" ".join(map(str, row)))


def main():
    main_grid = MainArray(10, 10)

    shape1 = Shape([[1, 1], [1, 1]])

    shape2 = Shape([[1, 1, 1], [0, 1, 0]])

    # Place the shapes on the grid
    shapes = [shape1, shape2]
    for shape in shapes:
        if main_grid.place_shape(shape):
            print("Shape placed successfully!")
        else:
            print("No available space for the shape.")

    # Display the grid after placing the shapes
    main_grid.display()

    # Add another shape
    shape3 = Shape([[1], [1], [1]])
    main_grid.place_shape(shape3)

    # Display the grid again after adding the new shape
    print("=======")
    main_grid.display()

    shape4 = Shape([[1, 1, 1]])
    main_grid.place_shape(shape4)
    
    shape5 = Shape([[1]])
    main_grid.place_shape(shape5)

    shape6 = Shape([[1]])
    main_grid.place_shape(shape6)
    
    shape6 = Shape([[1]])
    main_grid.place_shape(shape6)


    # Display the grid again after adding the new shape
    print("=======")
    main_grid.display()


if __name__ == "__main__":
    main()
