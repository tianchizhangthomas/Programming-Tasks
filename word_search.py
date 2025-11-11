
board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"

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
            return depth_first_search(board, word, row_index, col_index, used_board, 0)


def depth_first_search(board, word, row_index, col_index, used_board, searching_start_word_index):
    pass

    


