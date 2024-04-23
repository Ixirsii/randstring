"""
Functions to generate random strings with specified lengths and characters.

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

from random import uniform
from typing import Mapping, Optional

from .character_tables import get_default_charset


def create_string(
    length: int, character_table: Optional[Mapping[float, str]] = None
) -> str:
    """
    Create a random string of length 'length' using the weighted caracter map
    'character_table'.

    'character_table' defaults to only lowercase letters if a custom table
    is not passed.
    """
    if character_table is None:
        character_table = get_default_charset()

    result: str = ""
    upper_limit: float = next(reversed(character_table.keys()), 0)

    for _ in range(length):
        random = uniform(0, upper_limit)

        for key, value in character_table.items():
            if key >= random:
                result += value
                break

    return result


def create_strings(
    lengths: list[int], character_table: Optional[Mapping[float, str]] = None
) -> list[str]:
    """
    Map 'lengths' to a list of random strings each of length 'lengths[i]'
    """
    strings = map(lambda length: create_string(length, character_table), lengths)

    return list(strings)
