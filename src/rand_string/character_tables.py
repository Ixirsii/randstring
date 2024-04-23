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

from typing import Mapping


def get_default_charset() -> Mapping[float, str]:
    """
    Get the default character set for generating a random string.

    The default character set is only lowercase ASCII characters.
    """
    return __weights_to_charset(__get_lowercase_weights())


def get_alphabetic_charset() -> Mapping[float, str]:
    """
    Get the character set containing the whole alphabet, both upper and lower.
    """
    return __weights_to_charset(
        {**__get_lowercase_weights(), **__get_uppercase_weights()}
    )


def get_alphanumeric_charset() -> Mapping[float, str]:
    """
    Get the character set containing alphabetic and numeric characters.
    """
    return __weights_to_charset(
        {
            **__get_lowercase_weights(),
            **__get_uppercase_weights(),
            **__get_integer_weights(),
        }
    )


def get_full_charset() -> Mapping[float, str]:
    """
    Get the character set containing all printable ASCII characters.
    """
    return __weights_to_charset(
        {
            **__get_lowercase_weights(),
            **__get_uppercase_weights(),
            **__get_integer_weights(),
            **__get_symbol_weights(),
        }
    )


def get_integer_charset() -> Mapping[float, str]:
    """
    Get the character set containing only integers 0-9.
    """
    return __weights_to_charset(__get_integer_weights())


def get_lowercase_charset() -> Mapping[float, str]:
    """
    Get the character set containing only lowercase ASCII characters.
    """
    return __weights_to_charset(__get_lowercase_weights())


def get_symbol_charset() -> Mapping[float, str]:
    """
    Get the character set containing only ASCII symbols.
    """
    return __weights_to_charset(__get_symbol_weights())


def get_uppercase_charset() -> Mapping[float, str]:
    """
    Get the character set containing only uppercase ASCII characters.
    """
    return __weights_to_charset(__get_uppercase_weights())


# ############################################################################# #
# ######################### Private utility functions ######################### #
# ############################################################################# #


def __get_integer_weights() -> Mapping[str, float]:
    return {
        "0": 0.1,
        "1": 0.1,
        "2": 0.1,
        "3": 0.1,
        "4": 0.1,
        "5": 0.1,
        "6": 0.1,
        "7": 0.1,
        "8": 0.1,
        "9": 0.1,
    }


def __get_lowercase_weights() -> Mapping[str, float]:
    """
    Get the default character set of all lower case alphabetic letters.

    E  12.49% T   9.28% A   8.04% O   7.64% I   7.57% N   7.23%
    S   6.51% R   6.28% H   5.05% L   4.07% D   3.82% C   3.34%
    U   2.73% M   2.51% F   2.40% P   2.14% G   1.87% W   1.68%
    Y   1.66% B   1.48% V   1.05% K   0.54% X   0.23% J   0.16%
    Q   0.12% Z   0.09%
    """
    return {
        "a": 0.0804,
        "b": 0.0148,
        "c": 0.0334,
        "d": 0.0382,
        "e": 0.1249,
        "f": 0.0240,
        "g": 0.0187,
        "h": 0.0505,
        "i": 0.0757,
        "j": 0.0016,
        "k": 0.0054,
        "l": 0.0407,
        "m": 0.0251,
        "n": 0.0723,
        "o": 0.0764,
        "p": 0.0214,
        "q": 0.0012,
        "r": 0.0628,
        "s": 0.0651,
        "t": 0.0928,
        "u": 0.0273,
        "v": 0.0105,
        "w": 0.0168,
        "x": 0.0023,
        "y": 0.0166,
        "z": 0.0009,
    }


def __get_symbol_weights() -> Mapping[str, float]:
    """
    Get the default character set of all ASCII symbols.
    """
    return {
        "`": 0.0322,
        "~": 0.0323,
        "!": 0.0322,
        "@": 0.0323,
        "#": 0.0322,
        "$": 0.0323,
        "%": 0.0322,
        "^": 0.0323,
        "&": 0.0322,
        "*": 0.0323,
        "(": 0.0322,
        ")": 0.0323,
        "-": 0.0322,
        "_": 0.0323,
        "=": 0.0322,
        "+": 0.0323,
        "[": 0.0322,
        "{": 0.0323,
        "]": 0.0322,
        "}": 0.0323,
        "\\": 0.0322,
        "|": 0.0323,
        ";": 0.0322,
        ":": 0.0323,
        "'": 0.0322,
        '"': 0.0323,
        ",": 0.0322,
        "<": 0.0323,
        ".": 0.0322,
        ">": 0.0323,
        "/": 0.0322,
        "?": 0.0323,
    }


def __get_uppercase_weights() -> Mapping[str, float]:
    """
    Get the default character set of all upper case alphabetic letters.

    E  12.49% T   9.28% A   8.04% O   7.64% I   7.57% N   7.23%
    S   6.51% R   6.28% H   5.05% L   4.07% D   3.82% C   3.34%
    U   2.73% M   2.51% F   2.40% P   2.14% G   1.87% W   1.68%
    Y   1.66% B   1.48% V   1.05% K   0.54% X   0.23% J   0.16%
    """
    return {
        "A": 0.0804,
        "B": 0.0148,
        "C": 0.0334,
        "D": 0.0382,
        "E": 0.1249,
        "F": 0.0240,
        "G": 0.0187,
        "H": 0.0505,
        "I": 0.0757,
        "J": 0.0016,
        "K": 0.0054,
        "L": 0.0407,
        "M": 0.0251,
        "N": 0.0723,
        "O": 0.0764,
        "P": 0.0214,
        "Q": 0.0012,
        "R": 0.0628,
        "S": 0.0651,
        "T": 0.0928,
        "U": 0.0273,
        "V": 0.0105,
        "W": 0.0168,
        "X": 0.0023,
        "Y": 0.0166,
        "Z": 0.0009,
    }


def __weights_to_charset(character_weights: Mapping[str, float]) -> Mapping[float, str]:
    running_total: float = 0
    charset: Mapping[float, str] = {}

    for character, weight in character_weights.items():
        running_total += weight
        charset[running_total] = character

    return charset
