# Modules

## Import modules

```python
import math
print(math.sqrt(16))  # => 4.0
```

## From a module

```python
from math import ceil, floor
print(ceil(3.7))   # => 4.0
print(floor(3.7))  # => 3.0
```

## Import all

```python
from math import *
```

## Shorten module

```python
import math as m

# => True
math.sqrt(16) == m.sqrt(16)
```

## Functions and attributes

```python
import math
dir(math)
```
