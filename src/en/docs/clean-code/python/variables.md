# Variables

## Use meaningful and pronounceable variable names

**Bad:**

```python
import datetime

ymdstr = datetime.date.today().strftime("%y-%m-%d")
```

Additionally, there's no need to add the type of the variable (str) to its
name.

**Good**:

```python
import datetime

current_date: str = datetime.date.today().strftime("%y-%m-%d")
```

## Use the same vocabulary for the same type of variable

**Bad:**
Here we use three different names for the same underlying entity:

```python
def get_user_info(): pass


def get_client_data(): pass


def get_customer_record(): pass
```

**Good**:
If the entity is the same, you should be consistent in referring to it in your
functions:

```python
def get_user_info(): pass


def get_user_data(): pass


def get_user_record(): pass
```

**Even better**
Python is (also) an object oriented programming language. If it makes sense,
package the functions together with the concrete implementation of the entity
in your code, as instance attributes, property methods, or methods:

```python
from typing import Union, Dict


class Record:
    pass


class User:
    info: str

    @property
    def data(self) -> Dict[str, str]:
        return {}

    def get_record(self) -> Union[Record, None]:
        return Record()
```

## Use searchable names

We will read more code than we will ever write. It's important that the code we
do write is readable and searchable. By *not* naming variables that end up
being meaningful for understanding our program, we hurt our readers. Make your
names searchable.

**Bad:**

```python
import time

# What is the number 86400 for again?
time.sleep(86400)
```

**Good**:

```python
import time

# Declare them in the global namespace for the module.
SECONDS_IN_A_DAY = 60 * 60 * 24
time.sleep(SECONDS_IN_A_DAY)
```

## Use explanatory variables

**Bad:**

```python
import re

address = "One Infinite Loop, Cupertino 95014"
city_zip_code_regex = r"^[^,\\]+[,\\\s]+(.+?)\s*(\d{5})?$"

matches = re.match(city_zip_code_regex, address)
if matches:
    print(f"{matches[1]}: {matches[2]}")
```

**Not bad**:

It's better, but we are still heavily dependent on regex.

```python
import re

address = "One Infinite Loop, Cupertino 95014"
city_zip_code_regex = r"^[^,\\]+[,\\\s]+(.+?)\s*(\d{5})?$"
matches = re.match(city_zip_code_regex, address)

if matches:
    city, zip_code = matches.groups()
    print(f"{city}: {zip_code}")
```

**Good**:

Decrease dependence on regex by naming subpatterns.

```python
import re

address = "One Infinite Loop, Cupertino 95014"
city_zip_code_regex = r"^[^,\\]+[,\\\s]+(?P<city>.+?)\s*(?P<zip_code>\d{5})?$"

matches = re.match(city_zip_code_regex, address)
if matches:
    print(f"{matches['city']}, {matches['zip_code']}")
```

## Avoid Mental Mapping

Don’t force the reader of your code to translate what the variable means.
Explicit is better than implicit.

**Bad:**

```python
seq = ("Austin", "New York", "San Francisco")

for item in seq:
    # do_stuff()
    # do_some_other_stuff()

    # Wait, what's `item` again?
    print(item)
```

**Good**:

```python
locations = ("Austin", "New York", "San Francisco")

for location in locations:
    # do_stuff()
    # do_some_other_stuff()
    # ...
    print(location)
```

## Don't add unneeded context

If your class/object name tells you something, don't repeat that in your
variable name.

**Bad:**

```python
class Car:
    car_make: str
    car_model: str
    car_color: str
```

**Good**:

```python
class Car:
    make: str
    model: str
    color: str
```

## Use default arguments instead of short circuiting or conditionals

**Tricky**

Why write:

```python
import hashlib


def create_micro_brewery(name):
    name = "Hipster Brew Co." if name is None else name
    slug = hashlib.sha1(name.encode()).hexdigest()
    # etc.
```

... when you can specify a default argument instead? This also makes it clear
that you are expecting a string as the argument.

**Good**:

```python
import hashlib


def create_micro_brewery(name: str = "Hipster Brew Co."):
    slug = hashlib.sha1(name.encode()).hexdigest()
    # etc.
```
