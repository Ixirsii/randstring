"""
randstring is a python module that generates a randomized string
Copyright (C) 2013 Ryan Porterfield

This program is free software: you can redistribute it and/or
modify it under the terms of the GNU General Public License
as published by the Free Software Foundation; either version 2
of the License, or (at your option) any later version.

This program is distributed in the hope that it will be useful,
but WITHOUT ANY WARRANTY; without even the implied warranty of
MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
GNU General Public License for more details.

You should have received a copy of the GNU General Public License
along with this program; if not, see <http://www.gnu.org/licenses/>.
"""

import itertools


# Number of Lines: 6
def get_default():
    """
    TODO: Rename this method
    TODO: Edit this
    """
    tables = []
    tables.append(get_default_lowercase())
    tables.append(get_default_uppercase())
    tables.append(get_default_integer())
    tables.append(get_default_symbol())
    return tables


# Number of lines: 5
def get_default_alphabet():
    """
    Get the default weighted dict of the whole alphabet, both upper and lower
    case
    """
    try:
        _alphabet
    except NameError:
        __set_alphabet()
    return _alphabet


# Number of Lines: 5
def get_default_consonant():
    """
    Get the default weighted dict of lower case consonants
    """
    try:
        _consonant
    except NameError:
        __set_consonant()
    return _consonant


# Number of Lines: 5
def get_default_integer():
    """
    Get the default weighted dict of integers 0-9
    """
    try:
        _integer
    except NameError:
        __set_integer()
    return _integer


# Number of Lines: 1
def get_default_lowercase():
    """
    Get the default weighted dict of all lower case alphabetic letters
    """
    try:
        _lowercase
    except NameError:
        __set_lowercase()
    return _lowercase


# Number of Lines: 1
def get_default_symbol():
    """
    Get the default weighted dict of all ASCII symbols
    """
    pass


# Number of Lines: 4
def get_default_uppercase():
    """
    Get the default weighted dict of all upper case alphabetic letters
    """
    try:
        _uppercase
    except NameError:
        __set_uppercase()
    return _uppercase


# Number of Lines: 1
def get_default_vowel():
    """
    Get the default weighted dict of lower case vowels
    """
    try:
        _vowel
    except NameError:
        __set_vowel()
    return _vowel


# Number of Lines: 3
def __set_alphabet():
    global _alphabet
    _alphabet = get_default_lowercase().copy()
    _alphabet.update(get_default_uppercase())


# Number of Lines: 2
def __set_consonant():
    global _consonant
    _consonant = {
        'b': 1, 'c': 2, 'd': 4, 'f': 1, 'g': 1, 'h': 1, 'j': 1, 'k': 3,
        'l': 1, 'm': 2, 'n': 2, 'p': 2, 'q': 1, 'r': 4, 's': 3, 't': 3,
        'v': 1, 'w': 1, 'x': 2, 'z': 2}


# Number of Lines: 5
def __set_integer():
    global _integer
    all_letters = get_default_alphabet()
    weight = list(itertools.accumulate(all_letters.values()))[-1] / 10
    weight = int(weight)
    _integer = dict.fromkeys(list(range(10)), weight)


# Number of Lines: 3
def __set_lowercase():
    global _lowercase
    _lowercase = get_default_consonant().copy()
    _lowercase.update(get_default_vowel())


# Number of Lines: 4
def __set_uppercase():
    global _uppercase
    _uppercase = {}
    for letter, weight in get_default_lowercase().items():
        _uppercase[letter.upper()] = weight - 1 if weight > 1 else weight


# Number of Lines: 2
def __set_vowel():
    global _vowel
    _vowel = {'a': 4, 'e': 2, 'i': 2, 'o': 1, 'u': 1, 'y': 2}


if __name__ == "__main__":
    print("You ran this program from the command line. :-)")
    print("Unfortunately it's supposed to be used as a module and doesn't "
          "do anything. :-(")
else:
    print("Imported charactertables")

#
