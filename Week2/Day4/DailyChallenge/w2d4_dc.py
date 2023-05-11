def matrix():
    given_matrix = """7i3\nTsi\nh%x\ni #\nsM \n$a \n#t%\n^r!"""
    matrix_list = (given_matrix.split('\n'))
    ordered = [[matrix_list[row][column] for row in range(len(matrix_list))] for column in range(3)] #makes list of lists
                                                                                                     # in correct order
    string = ""
    for col in ordered:
        for letter in range(len(col)):
            if not col[letter].isalpha():
                col[letter] = ' '  # make all non-letters into space
            string += col[letter]  # string: This   is  Matr ix
    string = " ".join(string.split())  # split makes each word into a list item w/o spaces. join makes into str w/spaces
    print(string)


matrix()  # This is Matr ix - in the exercise there is a '3' between the 'r' and 'i' so there is a space