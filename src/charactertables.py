"""
randstring is a python module that generates a randomized string
Copyright (c) Ryan Porterfield 2013.
All rights reserved.

Redistribution and use in source and binary forms, with or without
modification, are permitted provided that the following conditions are met:

-Redistributions of source code must retain the above copyright notice, this
list of conditions and the following disclaimer.

-Redistributions in binary form must reproduce the above copyright notice,
this list of conditions and the following disclaimer in the documentation
and/or other materials provided with the distribution.

-Neither the name of KlashAPI nor the names of its
contributors may be used to endorse or promote products derived from
this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
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
