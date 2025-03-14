# Functions

## Basic

```python
def hello_world():
    print('Hello, World!')
```

## Return

```python
def add(x, y):
    print("x is %s, y is %s" %(x, y))
    return x + y

add(5, 6)    # => 11
```

## Positional arguments

```python
def varargs(*args):
    return args

varargs(1, 2, 3)  # => (1, 2, 3)
```

Type of "args" is tuple.

## Keyword arguments

```python
def keyword_args(**kwargs):
    return kwargs

# => {"big": "foot", "loch": "ness"}
keyword_args(big="foot", loch="ness")
```

Type of "kwargs" is dict.

## Returning multiple

```python
def swap(x, y):
    return y, x

x = 1
y = 2
x, y = swap(x, y)  # => x = 2, y = 1
```

## Default Value

```python
def add(x, y=10):
    return x + y

add(5)      # => 15
add(5, 20)  # => 25
```

## Anonymous functions

```python
# => True
(lambda x: x > 2)(3)

# => 5
(lambda x, y: x ** 2 + y ** 2)(2, 1)
```
