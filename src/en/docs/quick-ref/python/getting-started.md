# Getting Started

## Introduction

- [Python](https://www.python.org/) _(python.org)_
- [Python Document](https://docs.python.org/3/index.html) _(docs.python.org)_
- [Learn X in Y minutes](https://learnxinyminutes.com/docs/python/) _(learnxinyminutes.com)_
- [Regex in python](/regex#regex-in-python) _(cheatsheets.zip)_

## Hello World

```python
>>> print("Hello, World!")
Hello, World!
```

The famous "Hello World" program in Python

## Variables

```python
age = 18      # age is of type int
name = "John" # name is now of type str
print(name)
```

Python can't declare a variable without assignment.

## Data Types

|                                    |          |
| ---------------------------------- | -------- |
| `str`                              | Text     |
| `int`, `float`, `complex`          | Numeric  |
| `list`, `tuple`, `range`           | Sequence |
| `dict`                             | Mapping  |
| `set`, `frozenset`                 | Set      |
| `bool`                             | Boolean  |
| `bytes`, `bytearray`, `memoryview` | Binary   |

## Slicing String

```python
>>> msg = "Hello, World!"
>>> print(msg[2:5])
llo
```

## Lists

```python
mylist = []
mylist.append(1)
mylist.append(2)
for item in mylist:
    print(item) # prints out 1,2
```

## If Else

```python
num = 200
if num > 0:
    print("num is greater than 0")
else:
    print("num is not greater than 0")
```

## Loops

```python
for item in range(6):
    if item == 3: break
    print(item)
else:
    print("Finally finished!")
```

## Functions

```python
>>> def my_function():
...     print("Hello from a function")
...
>>> my_function()
Hello from a function
```

## File Handling

```python
with open("myfile.txt", "r", encoding='utf8') as file:
    for line in file:
        print(line)
```

## Arithmetic

```python
result = 10 + 30 # => 40
result = 40 - 10 # => 30
result = 50 * 5  # => 250
result = 16 / 4  # => 4.0 (Float Division)
result = 16 // 4 # => 4 (Integer Division)
result = 25 % 2  # => 1
result = 5 ** 3  # => 125
```

The `/` means quotient of x and y, and the `//` means floored quotient of x and y, also see
[StackOverflow](https://stackoverflow.com/a/183870/13192320)

## Plus-Equals

```python
counter = 0
counter += 10           # => 10
counter = 0
counter = counter + 10  # => 10

message = "Part 1."

# => Part 1.Part 2.
message += "Part 2."
```

## f-Strings (Python 3.6+)

```python
>>> website = 'cheatsheets.zip'
>>> f"Hello, {website}"
"Hello, cheatsheets.zip"

>>> num = 10
>>> f'{num} + 10 = {num + 10}'
'10 + 10 = 20'
```
