"""A board is a list of list of str. For example, the board
    ANTT
    XSOB
is represented as the list
    [['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']]

A word list is a list of str. For example, the list of words
    ANT
    BOX
    SOB
    TO
is represented as the list
    ['ANT', 'BOX', 'SOB', 'TO']
"""


def is_valid_word(wordlist, word):
    """ (list of str, str) -> bool

    Return True if and only if word is an element of wordlist.

    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], 'TO')
    True
    >>> is_valid_word(['dog', 'cat', 'giraffe', 'slug'], 'animal')
    False
    >>> is_valid_word(['ANT', 'BOX', 'SOB', 'TO'], '')
    False
    """
    return word in wordlist


def make_str_from_row(board, row_index):
    """ (list of list of str, int) -> str

    Return the characters from the row of the board with index row_index
    as a single string.

    >>> make_str_from_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 0)
    'ANTT'
    >>> make_str_from_row([['a', 'b', 'c'], ['m', 'y', 'm', 'y'], ['s', 'o'], ['d']],4)
    ''
    >>> make_str_from_row([['a', 'b', 'c'], ['m', 'y', 'm', 'y'], ['s', 'o'], ['d']],3)
    'd'
    """

    single_string = ''
    
    if row_index < len(board):
        for letter in board[row_index]:
            single_string += letter

    return single_string


def make_str_from_column(board, column_index):
    """ (list of list of str, int) -> str

    Return the characters from the column of the board with index column_index
    as a single string.

    >>> make_str_from_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 1)
    'NS'
    >>> make_str_from_column([['r', 's', 't', 'u'], ['g', 'a', 'd'], ['x', 'y', 'f', 'b']], 3)
    'u b'
    """

    single_string = ''

    for row in range(len(board)):
        if column_index < len(board[row]):
            single_string += board[row][column_index]
        else:
            single_string += ' '

    return single_string


def board_contains_word_in_row(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the rows of the board contains
    word.

    Precondition: board has at least one row and one column, and word is a
    valid word.

    >>> board_contains_word_in_row([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'SOB')
    True
    """

    for row_index in range(len(board)):
        if word in make_str_from_row(board, row_index):
            return True

    return False


def board_contains_word_in_column(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if one or more of the columns of the board
    contains word.

    Preconditions:
       1) board has at least one row and one column, and word is a valid word.
       2) len(board[0] == len(board[n]

    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'NO')
    False
    >>> board_contains_word_in_column([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'TO')
    True
    """

    for column_index in range(len(board[0])):
        if word in make_str_from_column(board, column_index):
            return True

    return False

def board_contains_word(board, word):
    """ (list of list of str, str) -> bool

    Return True if and only if word appears in board.

    Precondition: board has at least one row and one column.

    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], 'ANT')
    True
    >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B'], ['E', 'Z', 'N', 'S']], 'ON')
    True
    >>> >>> board_contains_word([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B'], ['E', 'Z', 'N', 'S']], 'NOT')
    False
    """

    return board_contains_word_in_row(board, word) or board_contains_word_in_column(board,word)


def word_score(word):
    """ (str) -> int

    Return the point value the word earns.

    Word length: < 3: 0 points
                 3-6: 1 point per character for all characters in word
                 7-9: 2 points per character for all characters in word
                 10+: 3 points per character for all characters in word

    >>> word_score('DRUDGERY')
    16
    >>> word_score('A')
    0
    >>> word_score('DOG')
    3
    >>> word_score('APPLES')
    6
    >>> word_score('SUPERCALIFRAGILISTICSUPERALIDOSCIOUS')
    108
    >>> word_score('1234567')
    14
    """

    num_letters = len(word)

    if num_letters < 3:
        return 0
    elif num_letters <= 6:
        return num_letters
    elif num_letters > 12:
        return 3 * num_letters
    else:
        return ((num_letters - 1) // 3) * num_letters


def update_score(player_info, word):
    """ ([str, int] list, str) -> NoneType

    player_info is a list with the player's name and score. Update player_info
    by adding the point value word earns to the player's score.

    >>> update_score(['Jonathan', 4], 'ANT')
    >>> update_score(['Snoozle', 23], 'MARGARINE')
    >>> update_score(['Rod', 1], 'IN')
    """

    player_info[1] += word_score(word)


def num_words_on_board(board, words):
    """ (list of list of str, list of str) -> int

    Return how many words appear on board.

    >>> num_words_on_board([['A', 'N', 'T', 'T'], ['X', 'S', 'O', 'B']], ['ANT', 'BOX', 'SOB', 'TO'])
    3
    """

    words_on_board = 0

    for the_word in words:
        if board_contains_word(board, the_word):
            words_on_board += 1

    return words_on_board


def read_words(words_file):
    """ (file open for reading) -> list of str

    Return a list of all words (with newlines removed) from open file
    words_file.

    Precondition: Each line of the file contains a word in uppercase characters
    from the standard English alphabet.
    """

    wordlist = []
    
    for line in words_file:
        wordlist.append(line.rstrip('\n'))

    return wordlist


def read_board(board_file):
    """ (file open for reading) -> list of list of str

    Return a board read from open file board_file. The board file will contain
    one row of the board per line. Newlines are not included in the board.

    (when board_file contents = "EFJA\nJCOW\nSSSD\n)
    >>> read_board(board_file)
    ['E', 'F', 'J', 'A'], ['J', 'C', 'O', 'W'], ['S', 'S', 'S', 'D']
    """

    board = []
    row = 0

    board_line = board_file.readline()


    while board_line != '':
        
        board.append([])
        for ltr in range(len(board_line)):
            if board_line[ltr] != '\n':
                board[row].append(board_line[ltr])
                
        board_line = board_file.readline()
        row += 1

    return board
        

