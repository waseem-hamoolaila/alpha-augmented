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

    def __init__(self, rows, cols):
        """
        Construct the main Box with initial values.

        Args:
            - rows (int): number of rows in the box
            - cols (int): number of cols in the box
        """
        self.rows = rows
        self.cols = cols
        self.matrix = [[0] * cols for _ in range(rows)] if not self.dummy else self.test_matrix

    def can_fit(self, item, row_index, col_index):
        """
        Check if I can place a specific Item in the a given coordinate.

        Args:
            - item (Item): The item that I want to place into the box.
            - row_index (int): row index where I want to start placing.
            - col_index (int): col index where I want to start placing.


        Returns:
            - True: in case the item will be fit starting from the given coordinates
            - False: otherwise
        """

        if row_index >= self.rows or col_index >= self.cols:
            return False

        for item_row in range(item.rows):
            for item_col in range(item.cols):
                # Here I need to see if the main matrix along the rows / cols of the item is available
                # since we are working our way from the bottom up... the box cell direction will be up
                # for that the operation is the row_index - the item row

                if col_index + item_col >= self.cols:
                    # If we reached the far right of the box... we will reject it to go up one step
                    return False

                box_cell = self.matrix[row_index - item_row][col_index + item_col]
                shape_cell = item.representation[item_row][item_col]
                if box_cell == 1 and shape_cell == 1:
                    return False

        return True

    def scan_and_fit(self, item):
        """
        Try to fit an item into the box.

        Args:
            - item (Item): the item that I want to fit in to the box

        Returns:
            - True: in case the item fitted successfully
            - False: otherwise
        """

        for box_row in range(self.rows):
            for box_col in range(self.cols):
                current_x_coordinate = box_col
                current_y_coordinate = self.rows - box_row - 1

                if self.can_fit(item=item, row_index=current_y_coordinate, col_index=current_x_coordinate):
                    self.fit_item_into_the_box(
                        item=item, y_coordinate=current_y_coordinate, x_coordinate=current_x_coordinate
                    )
                    return True

        return False  # the item cannot be fitted.

    def fit_item_into_the_box(self, item, y_coordinate, x_coordinate):
        """
        Actually fit the item into the box

        Args:
            - item (Item): the item that passed the test and can be fitted.
            - y_coordinate (int): row index where we will start fitting.
            - x_coordinate (int): col index where we will start fitting.

        Returns:
            - True: fitted successfully, and now the item is occupying space in the box.
            - False: otherwise.
        """
        for item_row in range(item.rows):
            for item_col in range(item.cols):
                if item.representation[item_row][item_col] == 1:
                    self.matrix[y_coordinate - item_row][x_coordinate + item_col] = 1

        return True

    def bulk_insertion(self, list_of_items):
        """
        Insert bulk of items at once to the box

        Args:
            - list_of_items (Item): list of items that will be inserted (ordered)

        Returns:
            - True: inserted successfully.
            - False: otherwise
        """

        for item in list_of_items:
            result = self.scan_and_fit(item)
            if not result:
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
    s3 = Item([[1, 1], [1, 1]])
    s4 = Item([[1, 1]])

    # print(box.can_fit(s2, 0, 2))

    box.scan_and_fit(s)
    box.scan_and_fit(s3)
    box.scan_and_fit(s2)
    box.scan_and_fit(s2)
    box.scan_and_fit(s2)
    box.scan_and_fit(s3)
    box.scan_and_fit(s2)  # should not be added
    box.scan_and_fit(s3)  # should not be added
    box.scan_and_fit(s4)  # should be fitted in the last two boxes
    box.show()


if __name__ == "__main__":
    main()
