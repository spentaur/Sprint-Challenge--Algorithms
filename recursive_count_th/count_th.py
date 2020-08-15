'''
Your function should take in a single parameter (a string `word`)
Your function should return a count of how many occurences of ***"th"*** occur within `word`. Case matters.
Your function must utilize recursion. It cannot contain any loops.
'''


def count_th(word):

    # base case is when the word is less than 2 characters, so i dont care
    # about it
    if len(word) < 2:
        return 0

    # now we go through and get the first two chars of the word
    # if they are 'th', then we add one and return the word, but removing the
    # first two chars
    if word[:2] == 'th':
        return 1 + count_th(word[2:])
    else:
        # if not, just move forward one char
        return count_th(word[1:])
