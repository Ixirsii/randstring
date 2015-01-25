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

from charactertables import get_default
import itertools
from random import SystemRandom


class StringGenerator():
    """
    Docstring
    """

    # Number of Lines: 3
    def __init__(self, verbose=False, table_list=get_default(),
                 rule_set=None):
        self._verbose = verbose
        self._rand = SystemRandom()
        self._table_list = table_list

    # Number of Lines: 1
    def create_string(self, length):
        """
        TODO: Edit this
        """
        pass

    # Number of Lines: 1
    def create_strings(self, num_strings, length):
        """
        Create 'num_strings' number of strings, each with length 'length'
        """
        return [self.create_string(length) for i in range(num_strings)]

    # Number of Lines: 1
    def get_rand(self):
        """
        DOCSTRING
        """
        pass


if __name__ == "__main__":
    print("You ran this program from the command line. :-)")
    print("Unfortunately it's supposed to be used as a module and doesn't "
          "do anything. :-(")
else:
    print("Imported randstring")

#
