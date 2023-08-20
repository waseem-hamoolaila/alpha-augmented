class Package:
    """
    The main block that will represent certain shapes
    """

    def __init__(
        self,
        structure,
        color=None,
        first_is_bottom=False,
        identifier=None,
    ):
        """
        Initial the Package

        Args:
            - structure (list): The desired shape for the Package Ex: [[1, 1], [1, 0]]
            - color (char): Optional if you need to color the package.
            - first_is_bottom (bool): Optional if we want to consider the structure bottom up: the first passed row is the bottom,
                                by default it is up-bottom, the first row passed will be the higher one in the package representation.
            - identifier (any): Optional, mark the package with a specific identifier and user it as needed.
        """

        self._validate_structure(structure)

        self.structure = structure
        self.rows = len(structure)
        self.cols = len(structure[0])
        self.color = color
        self.first_is_bottom = first_is_bottom
        self.identifier = identifier
        self._original_structure = structure

    def _validate_structure(self, structure):
        structure_type_message = "%s is not a valid structure, it should be two dimensional list" % structure

        if not isinstance(structure, list):
            raise ValueError(structure_type_message)

        if not any(isinstance(row, list) for row in structure):
            raise ValueError(structure_type_message)

    @property
    def _structure(self):
        """
        Used to flip the structure... in case we want to consider the first
        array as the bottom or the top
        """
        if self.first_is_bottom:
            return self.structure
        return [self.structure[row] for row in range(self.rows - 1, -1, -1)]

    def rotate(self):
        """
        Rotate the package 45 degree clock wise.
        """
        rotated = [[self.structure[row][col] for row in range(len(self.structure) - 1, -1, -1)] for col in range(len(self.structure[0]))]
        self.rows, self.cols = self.cols, self.rows  # switch cols and rows
        self.structure = rotated

    def reset(self):
        """
        Used to reset the package after rotation, bring back its original shape
        """
        self.structure = self._original_structure
        self.cols = len(self.structure[0])
        self.rows = len(self.structure)

    def console_print(self):
        """
        String representation of the current box.
        """
        for row in self._structure:
            print(row)


class Box:
    """
    The main container, that will hold the Packages.
    """

    def __init__(
        self,
        rows=5,
        cols=5,
        instance=None,
        rtl=False,
        horizontal=False,
        rotation=False,
    ):
        """
        Construct the main Box with initial values.

        Args:
            - rows (int): number of rows in the box, 5 by default
            - cols (int): number of cols in the box, 5 by default
            - instance (list): Optional, if you have any updated matrix, it will be used as it is passed.
            - rtl (bool): packing the packages right to left, left to right by default
            - horizontal (bool): horizontal point of view (deal with the box as shelves), vertical by default.
            - rotation (bool): Allow rotations for best fit.. the package will test fit in 4 positions: 45 - 90 - 145 - 180 degrees
        """
        self.rows = rows if not instance else len(instance)
        self.cols = cols if not instance else len(instance[0])
        self.matrix = [[(0, "") for _ in range(cols)] for _ in range(rows)] if not instance else instance
        self.rtl = rtl
        self.horizontal = horizontal
        self.rotation = rotation

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

                if row_index - package_row < 0:
                    return False

                # in case of vertically dropping, like in tetris board.
                if not self._clear_all_the_way_up(row_index=row_index, col_index=col_index) and not self.horizontal:
                    return False

                try:
                    if self.rtl:
                        box_cell = self.matrix[row_index - package_row][col_index - package_col]
                        package_cell = package._structure[package_row][package.cols - package_col - 1]
                    else:
                        box_cell = self.matrix[row_index - package_row][col_index + package_col]
                        package_cell = package._structure[package_row][package_col]

                    if box_cell[0] == 1 and package_cell == 1:
                        return False

                except IndexError:
                    return False

        return True

    def _clear_all_the_way_up(self, row_index, col_index):
        """
        Check if on a specific cell that it is clear till the top of the matrix

        Args:
            - row_index (int): row index from where to check
            - col_index (int): col index from where to check

        Returns:
            - bool: True if the way up is clear, False otherwise
        """

        for row in range(row_index, -1, -1):
            if self.matrix[row][col_index][0] == 1:
                return False

        return True

    def _fit_package_into_the_box(self, package, row_index, col_index):
        """
        Actually fit the Package into the box

        Args:
            - Package (Package): the Package that passed the test and can be fitted.
            - row_index (int): row index where we will start fitting.
            - col_index (int): col index where we will start fitting.

        Returns:
            - bool: fitted successfully, and now the Package is occupying space in the box, False otherwise.
        """
        for package_row in range(package.rows - 1, -1, -1):
            for package_col in range(package.cols - 1, -1, -1):
                try:
                    if self.rtl:
                        if package._structure[package_row][package.cols - package_col - 1] == 1:
                            self.matrix[row_index - package_row][col_index - package_col] = (1, package.color)
                    else:
                        if package._structure[package_row][package_col] == 1:
                            self.matrix[row_index - package_row][col_index + package_col] = (1, package.color)

                except IndexError:
                    return False
        return True

    def place(self, package):
        """
        Place a package inside the box.

        Args:
            - package (Package): the Package that I want to fit in to the box

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

                for _ in range(4):  # rotation
                    if self._can_fit(package=package, row_index=current_row_index, col_index=current_col_index):
                        self._fit_package_into_the_box(
                            package=package, row_index=current_row_index, col_index=current_col_index
                        )

                        if self.rotation:
                            # package.reset()
                            pass

                        return True

                    if self.rotation:
                        package.rotate()
                    else:
                        break

        return False  # the Package cannot be fitted.

    def bulk_packing(self, list_of_packages):
        """
        Insert list of packages at once to the box

        Args:
            - list_of_Packages (Package): list of Packages that will be inserted (ordered)

        Returns:
            - bool: True is inserted successfully, False otherwise.
        """

        failed_to_insert = 0
        all_placed_successfully = True

        for package in list_of_packages:
            result = self.place(package)
            if not result:
                failed_to_insert += 1
                all_placed_successfully = False

        return all_placed_successfully, failed_to_insert

    def fitting_percentage(self):
        """
        Calculate the percentage of occupation

        Returns:
            - number (int): percentage of occupation
        """
        space = self.rows * self.cols  # calculate the area
        number_of_occupied_cells = 0

        for rows in range(self.rows):
            for cols in range(self.cols):
                if self.matrix[rows][cols][0] == 1:
                    number_of_occupied_cells += 1

        percentage = (number_of_occupied_cells / space) * 100

        return round(percentage, 2)

    def fitting_decision(self):
        """
        Returns a text representation of the fitting percentage
        0 - 25%: very bad fitting - the box is way too big
        25 - 50: bad fitting - the box is kind of big.
        50 - 75: medium fitting - the box is slightly big.
        75 - 90: good fitting - Good fitting
        90 - 100: perfect - Perfect fitting

        Returns:
            - decision (str): text representation of the percentage
        """

        percentage = self.fitting_percentage()

        if percentage >= 0 and percentage <= 25:
            return "Occupation is %s%% - Very bad, the box is way too big." % percentage

        if percentage > 25 and percentage <= 50:
            return "Occupation is %s%% - Bad, the box is kind of big." % percentage

        if percentage > 50 and percentage <= 75:
            return "Occupation is %s%% - Medium, the box is slightly big." % percentage

        if percentage > 75 and percentage <= 90:
            return "Occupation is %s%% - Good, the box is a good fit." % percentage

        if percentage > 90 and percentage <= 100:
            return "Occupation is %s%% - Perfect, the box is a perfect fit." % percentage

    def compare_box(self, box):
        """
        Allows you to compare the score your current box state with any other box

        Args:
            - box: any Box instance

        Returns:
            - bool: True if the current box is have higher score than the passed one, False otherwise
        """

        if self.fitting_percentage() >= box.fitting_percentage():
            return True
        return False

    def console_print(self):
        """
        String representation of the current box.
        """
        for row in self.matrix:
            row_str = " ".join(str(cell[0]) for cell in row)
            print(row_str)


def main():
    box = Box(4, 4, rotation=True)
    p = Package([[1, 1, 1], [1, 0, 0]])
    p1 = Package([[0, 0, 1], [1, 1, 1]])

    # p1.console_print()


if __name__ == "__main__":
    main()
