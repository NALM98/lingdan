import re

def is_palindrome(line):
    line = line.lower()
    arr = list(filter(None, re.split('\W|\d', line)))
    line = ''.join(arr)
    rev_line = line[::-1]
    if line == rev_line:
        return True
    else:
        answer = 'It is not a palindrome'
    return False

print(is_palindrome(input()))
