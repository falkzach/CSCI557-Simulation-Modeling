# Begin by reading the file, one line at a time. For example:
# inFile = open('five letter words.txt', 'rb', 0)
inFile = open('nameswords5letter.txt', 'rb', 0)
words = []
for line in inFile:
    # Figure out how to fill the list 'words'. Look at 'string'
    # and 'split' to help. Write for loops over lists of strings with
    # for word in list_of_words:
    tokens = line.decode().rstrip().split(' ')
    words.extend(tokens)

inFile.close()  # a good idea to do!

# Find all palidromes in list (this is the center):
# recognize that string characters can be accessed like
# list elements word[start:stop:step]
# reversing a word can be done by stepping through it backwards
palindromes = [x for x in words if x == x[::-1]]


# Find all words that have meaning when spelled backwards
# similar to finding palindromes
reverses = [x for x in words if x[::-1] in words]

# Heavily nested loops over word lists, checking if "SATORness" is
# preserved. When it is, print the square and count it.
# At the end, report how many you find.

sators = 0

for palindrome in palindromes:
    satorSquare = [['' for x in range(len(palindrome))] for y in range(len(palindrome))]
    chars = list(palindrome)
    satorSquare[2] = chars

    # fill center cross with palindrome
    for i in range(0, len(palindrome)):
        satorSquare[2][i] = chars[i]
        satorSquare[i][2] = chars[i]

    # find inside word that works
    # find words for center from reverses by checking letters at index 2
    centerChar = palindrome[1]
    seconds = [x for x in reverses if x[2] == centerChar]

    # find outside word that works
    # find words for outer from reverses by checking letters at index 1 and 3
    if (len(seconds)):
        for second in seconds:
            # print("second:", second)
            secondChars = list(second)
            secondCharsReversed = list(reversed(second))
            for i in range(0, len(palindrome)):
                satorSquare[1][i] = secondChars[i]
                satorSquare[i][1] = secondChars[i]
                satorSquare[3][i] = secondCharsReversed[i]
                satorSquare[i][3] = secondCharsReversed[i]

            leftChar = secondChars[0]
            middleChar = palindrome[0]
            rightChar = secondCharsReversed[0]
            # print(leftChar, middleChar, rightChar)

            thirds = [x for x in reverses if x[1] == leftChar and x[2] == middleChar and x[3] == rightChar]
            # print("thirds:", thirds)

            if(len(thirds)):
                for third in thirds:
                    thirdChars = list(third)
                    thirdCharsReversed = list(reversed(third))

                    for i in range(0, len(palindrome)):
                        satorSquare[0][i] = thirdChars[i]
                        satorSquare[i][0] = thirdChars[i]
                        satorSquare[4][i] = thirdCharsReversed[i]
                        satorSquare[i][4] = thirdCharsReversed[i]

                    for row in satorSquare:
                        print(''.join(row))
                    print('\n')
                    sators += 1

print("Count: ", sators)
