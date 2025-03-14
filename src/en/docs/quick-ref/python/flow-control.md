# Flow control

## Basic

```python
num = 5
if num > 10:
    print("num is totally bigger than 10.")
elif num < 10:
    print("num is smaller than 10.")
else:
    print("num is indeed 10.")
```

## One line (ternary operator)

```python
>>> a = 330
>>> b = 200
>>> r = "a" if a > b else "b"
>>> print(r)
a
```

## else if

```python
value = True
if not value:
    print("Value is False")
elif value is None:
    print("Value is None")
else:
    print("Value is True")
```

## match case

```python
x = 1
match x:
  case 0:
    print("zero")
  case 1:
    print("one")
  case _:
    print("multiple")
```
