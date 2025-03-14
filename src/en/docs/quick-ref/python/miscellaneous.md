# Miscellaneous

## Comments

```python
# This is a single line comments.
```

```python
""" Multiline strings can be written
    using three "s, and are often used
    as documentation.
"""
```

```python
''' Multiline strings can be written
    using three 's, and are often used
    as documentation.
'''
```

## Generators

```python
def double_numbers(iterable):
    for i in iterable:
        yield i + i
```

Generators help you make lazy code.

## Generator to list

```python
values = (-x for x in [1,2,3,4,5])
gen_to_list = list(values)

# => [-1, -2, -3, -4, -5]
print(gen_to_list)
```

## Handle exceptions

```python
try:
    # Use "raise" to raise an error
    raise IndexError("This is an index error")
except IndexError as e:
    pass                 # Pass is just a no-op. Usually you would do recovery here.
except (TypeError, NameError):
    pass                 # Multiple exceptions can be handled together, if required.
else:                    # Optional clause to the try/except block. Must follow all except blocks
    print("All good!")   # Runs only if the code in try raises no exceptions
finally:                 # Execute under all circumstances
    print("We can clean up resources here")
```
