class Package:
    """
    The main block that will represent certain shapes
    """

    def __init__(self, structure, color=None):
        """
        Initial the Package

        Args:
            - structure (list): The desired shape for the Package Ex: [[1, 1], [1, 0]]
            - color (char -hexa-): Optional if you need to color the package.
        """
        self.structure = structure
        self.rows = len(structure)
        self.cols = len(structure[0])
        self.color = color


class Box:
    """
    The main container, that will hold the Packages.
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
        self.matrix = [[0] * cols for _ in range(rows)]

    def _can_fit(self, Package, row_index, col_index):
        """
        Check if I can place a specific Package in the a given coordinate.

        Args:
            - Package (Package): The Package that I want to place into the box.
            - row_index (int): row index where I want to start placing.
            - col_index (int): col index where I want to start placing.


        Returns:
            - bool: True in case the Package will be fit starting from the given coordinates, False otherwise.
        """

        if row_index >= self.rows or col_index >= self.cols:
            return False

        for Package_row in range(Package.rows):
            for Package_col in range(Package.cols):
                # Here I need to see if the main matrix along the rows / cols of the Package is available
                # since we are working our way from the bottom up... the box cell direction will be up
                # for that the operation is the row_index - the Package row

                if col_index + Package_col >= self.cols:
                    # If we reached the far right of the box... we will reject it to go up one step
                    return False

                try:
                    box_cell = self.matrix[row_index - Package_row][col_index + Package_col]
                    package_cell = Package.structure[Package_row][Package_col]
                    if box_cell == 1 and package_cell == 1:
                        return False
                except IndexError:
                    return False

        return True

    def _fit_Package_into_the_box(self, Package, row_index, col_index):
        """
        Actually fit the Package into the box

        Args:
            - Package (Package): the Package that passed the test and can be fitted.
            - row_index (int): row index where we will start fitting.
            - col_index (int): col index where we will start fitting.

        Returns:
            - bool: fitted successfully, and now the Package is occupying space in the box, False otherwise.
        """
        for Package_row in range(Package.rows):
            for Package_col in range(Package.cols):
                try:
                    if Package.structure[Package_row][Package_col] == 1:
                        self.matrix[row_index - Package_row][col_index + Package_col] = 1
                except IndexError:
                    return False
        return True

    def scan_and_place(self, Package):
        """
        Try to fit an Package into the box.

        Args:
            - Package (Package): the Package that I want to fit in to the box

        Returns:
            - bool: True in case the Package fitted successfully, False otherwise
        """

        for box_row in range(self.rows):
            for box_col in range(self.cols):
                current_col_index = box_col
                current_row_index = self.rows - box_row - 1

                if self._can_fit(Package=Package, row_index=current_row_index, col_index=current_col_index):
                    self._fit_Package_into_the_box(
                        Package=Package, row_index=current_row_index, col_index=current_col_index
                    )
                    return True

        return False  # the Package cannot be fitted.

    def bulk_insertion(self, list_of_packages):
        """
        Insert bulk of Packages at once to the box

        Args:
            - list_of_Packages (Package): list of Packages that will be inserted (ordered)

        Returns:
            - bool: True is inserted successfully, False otherwise.
        """

        for package in list_of_packages:
            result = self.scan_and_fit(package)
            if not result:
                return False

        return True

    def console_print(self):
        """
        Used to print the current state of the box in the consol.
        """
        for row in self.matrix:
            print(row)


def main():
    box = Box(5, 10)

    # box.show()

    s = Package([[1, 1, 1], [1, 1, 1]])
    s2 = Package([[1, 1, 1]])
    s3 = Package([[1, 1], [1, 1]])
    s4 = Package([[1, 1]])

    # print(box.can_fit(s2, 0, 2))

    box.scan_and_place(s)
    box.scan_and_place(s3)
    # box.scan_and_fit(s2)
    # box.scan_and_fit(s3)
    # box.scan_and_fit(s4)  # should be fitted in the last two boxes
    box.console_print()


if __name__ == "__main__":
    main()
