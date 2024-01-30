"""
A scanf for python based on RE

This Python library provides a simple implementation of the scanf function found in C.
It allows you to parse input strings according to a specified format string,
similar to how scanf works in C.
"""

import re

__all__ = ['scanf']

# It is easy to add more format types
# Notice that '\' in regexp needs to be converted to '\\' because patterns like '\1' will be escaped
_format_regexp = [(re.compile(token), regexp) for token, regexp in (
    ('%c', r'(.)'),
    (r'%(\d+)c', r'(.{1,\1})'),

    ('%d', r'([+-]?\\d+)'),
    (r'%(\d+)d', r'([+-]?\\d{1,\1})'),

    ('%s', r'(\\S+)'),
    (r'%(\d+)s', r'(\\S{1,\1})'),

    # support scientific notation, inf and nan
    ('%f', r'([+-]?\\d*\\.\\d+(?:[eE][+-]?\\d+)?|[+-]?inf|[+-]?Inf|[+-]?nan|[+-]?NaN)'),
    (r'%(\d*)\\.(\d*)f', r'([+-]?\\d{0,\1}\\.\\d{1,\2})'),

    ('%o', r'([+-]?0o[0-7]+)'),
    ('%x', r'([+-]?0x[0-9a-fA-F]+)'),
    ('%b', r'([+-]?0b[01]+)')
)]

_format_cast = {
    'c': lambda x: x,
    's': lambda x: x,
    'd': int,
    'f': float,
    'o': lambda x: int(x, 8),
    'x': lambda x: int(x, 16),
    'b': lambda x: int(x, 2)
}

_format_tokens = re.compile('|'.join([token.pattern for token, _ in _format_regexp]))


def scanf(format_s: str, input_s=None):
    """
    Parse the input string according to the specified format string.

    :param format_s: The format string specifying how to parse the input string.
    :param input_s: (Optional) The input string to be parsed. If not provided, it defaults to `input()`.
    :return: The parsed value(s) according to the format string. Returns None if no match is found.

    Scanf supports the following formats:

    - `%c`: Single character
    - `%7c`: Seven characters
    - `%s`: A string terminated by whitespace
    - `%5s`: String of up to five characters terminated by whitespace
    - `%d`: An integer
    - `%6d`: Integer with up to six digits
    - `%f`: A floating-point number
    - `%.5f`: Floating-point number with up to five digits after the decimal point (recommended)
    - `%x`: A hexadecimal number
    - `%o`: An octal number
    - `%b`: A binary number
    """

    if input_s is None:
        input_s = input()

    # Avoid special characters being escaped
    # Avoid '%' being escaped
    format_s = re.escape(format_s).replace('%%', '%-')

    # Find matching format tokens
    match_tokens = [match.group() for match in _format_tokens.finditer(format_s)]

    # Convert the format string into a regular expression pattern
    for token, regexp in _format_regexp:
        format_s = token.sub(regexp, format_s)

    # Notice that '-' has been replaced with '\-' so there can't be an additional '%-'
    format_s = format_s.replace('%-', '%')

    # Perform regular expression matching
    matches = re.match(format_s, input_s)

    if not matches:
        return None

    matches = matches.groups()

    if len(matches) != len(match_tokens):
        return None

    # If only one match is found, return the single value
    # otherwise, return a tuple
    if len(match_tokens) == 1:
        return _format_cast[match_tokens[0][-1]](matches[0])

    return tuple([_format_cast[token[-1]](match) for token, match in zip(match_tokens, matches)])


if __name__ == "__main__":
    import unittest
    from test import TestScanf

    suite = unittest.TestLoader().loadTestsFromTestCase(TestScanf)
    unittest.TextTestRunner(verbosity=2).run(suite)
