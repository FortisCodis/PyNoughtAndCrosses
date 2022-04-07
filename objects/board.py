class Board:
    """
    Create a new board of tic-tac-toe.

    It can be printed.
    It manages the adding of symbols on the board.

    Attributes:
        table (list) Content of the board.
    """

    def __init__(self):

        self.table = [
            ["_", "_", "_"],
            ["_", "_", "_"],
            ["_", "_", "_"]
        ]

    def __str__(self) -> str:
        """
        Method which is called to print the board.

        :return: The str board
        """
        display = ""

        for line in self.table:
            display += f"| {line[0]} | {line[1]} | {line[2]} |\n"

        return display

    def __len__(self) -> int:
        """
        Method which is called to have the len of the table.

        :return: The number of lines
        """

        return len(self.table)

    @staticmethod
    def __cell_is_empty(cell_content: str) -> bool:
        """
        Tests if a cell is empty.

        :param: cell_content Content of the cell
        :return: True (if it is empty), False (else)
        """

        if cell_content == "_":
            return True

        else:
            return False

    def add_symbol(self, symbol: str, cell_line: int, cell_column: int) -> bool:
        """
        Adds a symbol on the board.

        :param: symbol - The Symbol to add. A ValueError will be raised if it isn't "X" or "O"
        :param: cell_column Column number of the cell
        :param: cell_line Line number of the cell
        :return: None (if everything went well), False (if the cell is already taken)
        """
        # Errors
        if cell_line > 2 or cell_column > 2:
            raise IndexError("Board index out of range.")

        cell_content = self.table[cell_line][cell_column]

        if not(symbol == "X" or symbol == "O"):
            raise ValueError(f"Unknown symbol {symbol}.")

        if not self.__cell_is_empty(cell_content):
            return False

        else:
            self.table[cell_line][cell_column] = symbol

    def line(self, n: int) -> tuple:
        """
        Shows items of the line n.

        :param: number of the line
        :return: The items of the line n in a tuple.
        """
        return tuple(self.table[n])

    def column(self, n: int) -> tuple:
        """
        Shows items of the column n.

        :param: number of the column
        :return: The items of the column n in a tuple.
        """
        return tuple(line[n] for line in self.table)

    def diagonal(self, n: int) -> tuple:
        """
        Shows items of the diagonal n.

        There are two diagonals (the first (n=0) is the one which starts to the cell 0, 0).

        :param: number of the diagonal
        :return: The items of the diagonal n in a tuple.
        """
        if n not in (0, 1):
            return ()

        diagonal = ()
        if n == 0:

            i = 0
            for line in self.table:
                diagonal += tuple(line[i])
                i += 1

        elif n == 1:

            i = -1  # We start to the last element
            for line in self.table:
                diagonal += tuple(line[i])
                i -= 1

        return diagonal

    def is_complete(self) -> bool:
        """
        Tests if the board is complete.

        :return: True, False
        """
        for line in self.table:
            for cell in line:
                if self.__cell_is_empty(cell):
                    return False

        return True
