# Loops

## Basic

```python
primes = [2, 3, 5, 7]
for prime in primes:
    print(prime)
```

Prints: 2 3 5 7

## With index

```python
animals = ["dog", "cat", "mouse"]
# enumerate() adds counter to an iterable
for i, value in enumerate(animals):
    print(i, value)
```

Prints: 0 dog 1 cat 2 mouse

## While

```python
x = 0
while x < 4:
    print(x)
    x += 1  # Shorthand for x = x + 1
```

Prints: 0 1 2 3

## Break

```python
x = 0
for index in range(10):
    x = index * 10
    if index == 5:
     break
    print(x)
```

Prints: 0 10 20 30 40

## Continue

```python
for index in range(3, 8):
    x = index * 10
    if index == 5:
     continue
    print(x)
```

Prints: 30 40 60 70

## Range

```python
for i in range(4):
    print(i) # Prints: 0 1 2 3

for i in range(4, 8):
    print(i) # Prints: 4 5 6 7

for i in range(4, 10, 2):
    print(i) # Prints: 4 6 8
```

## With zip()

```python
words = ['Mon', 'Tue', 'Wed']
nums = [1, 2, 3]
# Use zip to pack into a tuple list
for w, n in zip(words, nums):
    print('%d:%s, ' %(n, w))
```

Prints: 1:Mon, 2:Tue, 3:Wed,

## for/else

```python
nums = [60, 70, 30, 110, 90]
for n in nums:
    if n > 100:
        print("%d is bigger than 100" %n)
        break
else:
    print("Not found!")
```

Also see: [Python Tips](https://book.pythontips.com/en/latest/for_-_else.html)
