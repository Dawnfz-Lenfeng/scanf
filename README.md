# scanf: A scanf for Python based on RE
This Python library provides a simple implementation of the scanf function found in C. 
It allows you to parse input strings according to a specified format string, 
similar to how scanf works in C.

It not only supports `%d`, `%s`, etc., 
but also supports width specification such as `%3d`, `%.5f`, and so on.

## Usage
`scanf.scanf(format_s: str, input_s=None)`

### Arguments
* **format_s**: The format string specifying how to parse the input string.
* **input_s**: (Optional) The input string to be parsed. If not provided, it defaults to `input()`.

scanf supports the following formats:

| Format  | Type  | Description                                                                                                          |
|---------|-------|----------------------------------------------------------------------------------------------------------------------|
| `%c`    | str   | Single character                                                                                                     |
| `%7c`   | str   | Seven characters                                                                                                     |
| `%s`    | str   | A string terminated by whitespace                                                                                    |
| `%5s`   | str   | String of up to five characters terminated by whitespace                                                             |
| `%d`    | int   | An integer                                                                                                           |
| `%6d`   | int   | Integer with up to six digits                                                                                        |
| `%f`    | float | A floating-point number, supporting both standard decimal notation and scientific notation (like .6, 3.5, 1.23e-5)   |
| `%3.5f` | float | Floating-point number with up to three digits before the decimal point and up to five digits after (not recommended) |
| `%.5f`  | float | Floating-point number with up to five digits after the decimal point (recommended)                                   |
| `%x`    | int   | A hexadecimal number                                                                                                 |
| `%o`    | int   | An octal number                                                                                                      |
| `%b`    | int   | A binary number                                                                                                      |

### Returns
If no match is found, it returns `None`. 
If a single match is found, it returns the matched value. If multiple matches are found, 
it returns a tuple of the matched values.

### Examples
* **Not provide input_s**
```python
from scanf import scanf

scanf('%4d-%d-%d-%s')
```
```pycon
>>> [stdin] 2024-1-29-myfirstprogram
>>> (2024, 1, 29, 'myfirstprogram')
```
---
* **A single match is found**
```python
scanf('%x', '0x1364E11something else')
# actually only matched '0x1364E11'
```
```pycon
>>> 20240129 
```
**Note**
1. hexadecimal / octal / binary numbers will be automatically converted to decimal. 
If you want to output in a specific base, you can convert it yourself.
2. Matching is done from the beginning and not "fully matched", so formatted matching can ignore the content that comes after.
---
* **About width specification for floats**
```python
_, f = scanf('%d%2.1f', '202417.29')
print(f)
# expect 17.2
```
```pycon
# But actually
>>> 7.2
```
This happens because during the matching process, scanf prioritizes matching as many characters as possible with the earliest format specifier. 

In this case, `%d` matches `20241` instead of `2024`, causing the subsequent `%2.1f` to match `7.2` instead of `17.2`. 

To address this issue, you can use `%4d%.1f` instead of `%d%2.1f`.
```python
_, f = scanf('%4d%.5f', '202417.2')
print(f)
```
```pycon
>>> 17.29
```
That is why width specification for floats like `%.3f` is more recommended.

---
* **About match whitespace**
```python
scanf('%d%d', '12 34')
# expect (12, 34)
```
```pycon
# But actually
>>> None
```
This occurs because the current implementation does not support **flexible whitespace matching**. 
(In fact, I am unsure whether this feature is important.)

---

## Other resources
For more information see:
* https://en.wikipedia.org/wiki/Scanf
* https://docs.python.org/3.12/library/re.html
* https://github.com/Dawnfz-Lenfeng/scanf/

## Releases
### 0.2.0: 2024-01-29
* Updated test files
* Added support for floating-point numbers in scientific notation
* Added support for integers and floating-point numbers with optional leading '+' sign
* Added support for matching Inf and NaN
* Resolved the issue where special characters in format_s could be escaped

### 0.1.0: 2024-01-29
* Initial release
* Basic functionality implemented
* Supports various data types, including int, float, str.
* Provides different formatting options such as width, precision, radix, etc.
* Documentation updated with basic usage instructions
