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

        self._validate_structure(structure)

        self.structure = structure
        self.rows = len(structure)
        self.cols = len(structure[0])
        self.color = color

    def _validate_structure(self, structure):
        structure_type_message = "Package structure must be a nested list."

        if not isinstance(structure, list):
            raise TypeError(structure_type_message)

        if not any(isinstance(row, list) for row in structure):
            raise TypeError(structure_type_message)


class Box:
    """
    The main container, that will hold the Packages.
    """

    test = False
    test_matrix = [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0],
    ]

    def __init__(self, rows, cols, rtl=False, vertical=False):
        """
        Construct the main Box with initial values.

        Args:
            - rows (int): number of rows in the box
            - cols (int): number of cols in the box
            - rtl (bool): packing the packages right to left, left to right by default
            - vertical (bool): vertical point of view, horizontal by default.
        """
        self.rows = rows
        self.cols = cols
        self.matrix = [[0] * cols for _ in range(rows)] if not self.test else self.test_matrix
        self.rtl = rtl
        self.vertical = vertical

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
                if col_index + package_col >= self.cols and not self.rtl:
                    return False

                if col_index - package_col < 0 and self.rtl:
                    return False

                if self.vertical and self.matrix[row_index - 1][col_index] == 1:
                    return False

                try:
                    if self.rtl:
                        box_cell = self.matrix[row_index - package_row][col_index - package_col]
                        package_cell = package.structure[package_row][package.cols - package_col - 1]
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
                    if self.rtl:
                        if package.structure[package_row][package_col] == 1:
                            self.matrix[row_index - package_row][col_index - package_col] = 1
                    else:
                        if package.structure[package_row][package_col] == 1:
                            self.matrix[row_index - package_row][col_index + package_col] = 1
                except IndexError:
                    return False
        return True

    def place(self, package):
        """
        Try to fit an Package into the box.

        Args:
            - Package (Package): the Package that I want to fit in to the box

        Returns:
            - bool: True in case the Package fitted successfully, False otherwise
        """

        for box_row in range(self.rows):
            for box_col in range(self.cols):
                if self.rtl:
                    current_col_index = self.cols - box_col - 1
                else:
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
        String representation of the current box.
        """
        for row in self.matrix:
            row_str = " ".join(str(cell) for cell in row)
            print(row_str)


def main():
    box = Box(5, 6, rtl=True, vertical=True)

    # box.show()
    s2 = Package([[1, 0, 1, 1, 1], [1, 1, 0, 1, 1]])
    s3 = Package([[1]])
    s3 = Package([[1], [1]])
    box.place(s2)
    box.place(s3)
    box.place(s3)
    box.place(s3)
    box.place(s3)
    box.place(s3)
    box.console_print()

    # print(box._can_fit(s2, 2, 2))


if __name__ == "__main__":
    main()
