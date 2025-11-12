# A solution to word search problem using recursive backtracking.

import psycopg

# Get a database connection and a cursor.
conn = psycopg.connect(host="localhost", dbname="postgres", user="postgres", password="1234", port=5432)
cur = conn.cursor()
# Get the board matrix from the database.
cur.execute('''SELECT board FROM boards WHERE id=0;''')
board = cur.fetchone()[0]
# Close the cursor and connection.
cur.close()
conn.close()

# board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
# word = "SEE"
# word = "ABCB"


def exist(board, word):
    # Get the number of rows and cols of the board.
    number_of_rows = len(board)
    number_of_cols = len(board[0])
    
    # First, to solve some trivial cases.
    # If the word is empty, then there definitely exists a match.
    if word == "":
        return True
    # If all the letters are used and it cannot even get to the length of the word,
    # then there doesn't exist a match obviously.
    if (len(word) > number_of_rows * number_of_cols):
        return False
    
    # To traverse all the letters in the board. Any of those letters could be the starting letter.
    for row_index in range(number_of_rows):
        for col_index in range(number_of_cols):
            # Again, deal with a trivial case. If the initial letter of the word doesn't match
            # the current letter from the board, then it will never match and it is safe to
            # start checking the next letter in the board.
            if (word[0] != board[row_index][col_index]):
                continue

            # If the initial letter matches, then we perform the depth first search.
            # The used board is to mark whether a letter has alreaday been used previously, so at first it's all False.
            used_board = [[False for _ in range(number_of_cols)] for _ in range(number_of_rows)]
            if depth_first_search(board, word, row_index, col_index, used_board, 0) == True:
                return True
            else:
                continue
    # All of letters fail to be the starting point, so there is no match.
    return False


def depth_first_search(board, word, row_index, col_index, used_board, searching_start_word_index):
    """Perform depth first search and return a boolean to indicate the search result.

    Arguments:
    board -- the input letter board
    word -- the word to search
    row_index, col-index -- the row and column index of current starting cell
    used_board -- the same size board as the "board", to indicate already used cells
    searching_start_word_index -- based on this index, the search tries to find a word starting from the letter corresponding to the index

    """
    # Stopping condition for recursion
    if searching_start_word_index == len(word):
        return True
    number_of_rows = len(board)
    number_of_cols = len(board[0])
    # To make sure the search is in the correct range in the board.
    if (row_index == number_of_rows) or (col_index == number_of_cols):
        return False
    # To deal with trivial cases.
    # If the selected board letter is not the initial letter, then the search fails.
    if (board[row_index][col_index] != word[searching_start_word_index]):
        return False
    # If the selected board letter has already been used previously, then the search fails.
    if (used_board[row_index][col_index] == True):
        return False
    
    # After checking, it's safe to use the letter on board[row_index][col_index], and we change the corresponding boolean value on used_board.
    used_board[row_index][col_index] = True

    # We can go on to the recursive part.
    # We try searching four directions from the current cell and if any of them is successful, then the search is successful and return True.
    if (depth_first_search(board, word, row_index+1, col_index, used_board, searching_start_word_index+1) or depth_first_search(board, word, row_index, col_index-1, used_board, searching_start_word_index+1)
        or depth_first_search(board, word, row_index, col_index+1, used_board, searching_start_word_index+1) or depth_first_search(board, word, row_index-1, col_index, used_board, searching_start_word_index+1)):
        return True
    
    # All four depth first search fail which means the board[row_index][col_index] cannot be used.
    # We need to reset the corresponding cell in used_board to False. Here's the backtracking part.
    used_board[row_index][col_index] = False

    # All four depth first search fail, then we don't find the word and return False.
    return False


print(exist(board, word))
    
