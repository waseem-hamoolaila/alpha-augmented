class Item:
    """
    The main block that will represent certain shapes
    """

    def __init__(self, representation):
        """
        Initial the item

        Args:
        - representation (list): The desired shape for the item Ex: [[1, 1], [1, 0]]

        """
        self.representation = representation
        self.rows = len(representation)
        self.cols = len(representation[0])


class Box:
    """
    The main container, that will hold the items
    """

    test = True  # to populate the main matrix manually... this will give me more flexibility in testing
    test_matrix = [
        [1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0],
        [1, 1, 1, 1, 0],
    ]

    def __init__(self, rows, cols):
        """
        Construct the main Box with initial values.

        Args:
            - rows: number of rows in the box
            - cols: number of cols in the box
        """
        self.rows = rows
        self.cols = cols
        self.matrix = [[0] * cols for _ in range(rows)] if not self.test else self.test_matrix

    def can_fit(self, item, row_index, col_index):
        """
        Check if I can place a specific Item in the a given coordinate.

        Args:
            - item (Item): The item that I want to place into the box.
            - row_index (int): row index where I want to start placing.
            - col_index (int): col index where I want to start placing.
        """

        if row_index >= self.rows or col_index >= self.cols:
            return False

        for item_row in range(item.rows):
            for item_col in range(item.cols):
                # Here I need to see if the main matrix along the rows / cols of the item is available
                # since we are working our way from the bottom up... the box cell direction will be up
                # for that the operation is the row_index - the item row
                box_cell = self.matrix[row_index - item_row][col_index + item_col]
                shape_cell = item.representation[item_row][item_col]
                if box_cell == 1 and shape_cell == 1:
                    return False

        return True

    def show(self):
        """
        Used to print the current state of the box in the consol.
        """
        for row in self.matrix:
            print(row)


def main():
    box = Box(5, 5)

    # box.show()

    s = Item([[1, 1, 1], [1, 1, 1]])
    s2 = Item([[1, 1, 1]])

    print(box.can_fit(s2, 0, 2))


if __name__ == "__main__":
    main()
