#!/usr/bin/python3

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

import sys


def test(result, expected, test_info=None):
    if result == expected:
        prefix = "[\033[92mPASS\033[00m]"
        success = True
    else:
        prefix = "[\033[91mFAIL\033[00m]"
        success = False
    if test_info is not None:
        print(''.join(['\t', test_info]))
    print(prefix, '\tgot:', result, '\texpected:', expected)
    return success


def test_one():
    consonant = charactertables.get_default_consonant()
    if test(type(consonant), dict):
        test(len(consonant), 20, test_info='Length of consonants')
    symbol = charactertables.get_default_symbol()
    if test(type(symbol), dict):
        test(len(symbol), 31, test_info='Length of ASCII symbols')
    vowel = charactertables.get_default_vowel()
    if test(type(vowel), dict):
        test(len(vowel), 6, test_info='Length of vowel')


def test_two():
    integer = charactertables.get_default_integer()
    if test(type(integer), dict):
        test(len(integer), 10, test_info='Length of integers')
    lowercase = charactertables.get_default_lowercase()
    if test(type(lowercase), dict):
        test(len(lowercase), 26, test_info='Length of lowercase')
    uppercase = charactertables.get_default_uppercase()
    if test(type(uppercase), dict):
        test(len(uppercase), 26, test_info='Length of uppercase')


def test_three():
    alphabet = charactertables.get_default_alphabet()
    if test(type(alphabet), dict):
        test(len(alphabet), 26 * 2, test_info='Length of alphabet')


def test_tables():
    test_one()
    test_two()
    test_three()


def main():
    test(type(charactertables.get_default()), list)
    test_tables()


if __name__ == '__main__':
    sys.path.insert(0, '../')
    import charactertables
    import randstring
    main()

# EOF
