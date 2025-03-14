# Strings

## Array-like

```python
>>> hello = "Hello, World"
>>> print(hello[1])
e
>>> print(hello[-1])
d
```

Get the character at position 1 or last

## Looping

```python
>>> for char in "foo":
...     print(char)
f
o
o
```

Loop through the letters in the word "foo"

## Slicing string

```java
 ┌───┬───┬───┬───┬───┬───┬───┐
 | m | y | b | a | c | o | n |
 └───┴───┴───┴───┴───┴───┴───┘
 0   1   2   3   4   5   6   7
-7  -6  -5  -4  -3  -2  -1
```

---

```python
>>> s = 'mybacon'
>>> s[2:5]
'bac'
>>> s[0:2]
'my'
```

```python
>>> s = 'mybacon'
>>> s[:2]
'my'
>>> s[2:]
'bacon'
>>> s[:2] + s[2:]
'mybacon'
>>> s[:]
'mybacon'
```

```python
>>> s = 'mybacon'
>>> s[-5:-1]
'baco'
>>> s[2:6]
'baco'
```

### With a stride

```python
>>> s = '12345' * 5
>>> s
'1234512345123451234512345'
>>> s[::5]
'11111'
>>> s[4::5]
'55555'
>>> s[::-5]
'55555'
>>> s[::-1]
'5432154321543215432154321'
```

## String Length

```python
>>> hello = "Hello, World!"
>>> print(len(hello))
13
```

The len() function returns the length of a string

## Multiple copies

```python
>>> s = '===+'
>>> n = 8
>>> s * n
'===+===+===+===+===+===+===+===+'
```

## Check String

```python
>>> s = 'spam'
>>> s in 'I saw spamalot!'
True
>>> s not in 'I saw The Holy Grail!'
True

```

## Concatenates

```python
>>> s = 'spam'
>>> t = 'egg'
>>> s + t
'spamegg'
>>> 'spam' 'egg'
'spamegg'
```

## Formatting

```python
name = "John"
print("Hello, %s!" % name)
```

```python
name = "John"
age = 23
print("%s is %d years old." % (name, age))
```

### format() Method

```python
txt1 = "My name is {fname}, I'm {age}".format(fname="John", age=36)
txt2 = "My name is {0}, I'm {1}".format("John", 36)
txt3 = "My name is {}, I'm {}".format("John", 36)
```

## Input

```python
>>> name = input("Enter your name: ")
Enter your name: Tom
>>> name
'Tom'
```

Get input data from console

## Join

```python
>>> "#".join(["John", "Peter", "Vicky"])
'John#Peter#Vicky'
```

## Endswith

```python
>>> "Hello, world!".endswith("!")
True
```
