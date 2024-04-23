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
from random import SystemRandom

from charactertables import get_default


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
