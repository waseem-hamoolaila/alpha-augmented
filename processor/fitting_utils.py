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

    test = True
    test_matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    def __init__(self, rows, cols, rtl=False):
        """
        Construct the main Box with initial values.

        Args:
            - rows (int): number of rows in the box
            - cols (int): number of cols in the box
        """
        self.rows = rows
        self.cols = cols
        self.matrix = [[0] * cols for _ in range(rows)] if not self.test else self.test_matrix
        self.rtl = rtl

    def _can_fit(self, package, row_index, col_index):
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

        for package_row in range(package.rows):
            for package_col in range(package.cols):
                if col_index + package_col >= self.cols:
                    # If we reached the far right of the box... we will reject it to go up one step
                    return False

                try:
                    if self.rtl:
                        box_cell = self.matrix[row_index - package_row][col_index - package_col]
                        package_cell = package.structure[package_row][package_col]
                    else:
                        box_cell = self.matrix[row_index - package_row][col_index + package_col]
                        package_cell = package.structure[package_row][package_col]

                    if box_cell == 1 and package_cell == 1:
                        return False

                except IndexError:
                    return False

        return True

    def _fit_Package_into_the_box(self, package, row_index, col_index):
        """
        Actually fit the Package into the box

        Args:
            - Package (Package): the Package that passed the test and can be fitted.
            - row_index (int): row index where we will start fitting.
            - col_index (int): col index where we will start fitting.

        Returns:
            - bool: fitted successfully, and now the Package is occupying space in the box, False otherwise.
        """
        for package_row in range(package.rows):
            for package_col in range(package.cols):
                try:
                    if package.structure[package_row][package_col] == 1:
                        self.matrix[row_index - package_row][col_index + package_col] = 1
                except IndexError:
                    return False
        return True

    def scan_and_place(self, package):
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

                if self._can_fit(package=package, row_index=current_row_index, col_index=current_col_index):
                    self._fit_Package_into_the_box(
                        package=package, row_index=current_row_index, col_index=current_col_index
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
    box = Box(5, 10, rtl=True)

    # box.show()
    s2 = Package([[1, 1, 1]])
    box.scan_and_place(s2)
    box.console_print()


if __name__ == "__main__":
    main()
