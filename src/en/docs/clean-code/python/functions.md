# Functions

## Functions should do one thing

This is by far the most important rule in software engineering. When functions
do more than one thing, they are harder to compose, test, and reason about.
When you can isolate a function to just one action, they can be refactored
easily and your code will read much cleaner. If you take nothing else away from
this guide other than this, you'll be ahead of many developers.

**Bad:**

```python
from typing import List


class Client:
    active: bool


def email(client: Client) -> None:
    pass


def email_clients(clients: List[Client]) -> None:
    """Filter active clients and send them an email.
    """
    for client in clients:
        if client.active:
            email(client)
```

**Good**:

```python
from typing import List


class Client:
    active: bool


def email(client: Client) -> None:
    pass


def get_active_clients(clients: List[Client]) -> List[Client]:
    """Filter active clients.
    """
    return [client for client in clients if client.active]


def email_clients(clients: List[Client]) -> None:
    """Send an email to a given list of clients.
    """
    for client in get_active_clients(clients):
        email(client)
```

Do you see an opportunity for using generators now?

**Even better**

```python
from typing import Generator, Iterator


class Client:
    active: bool


def email(client: Client):
    pass


def active_clients(clients: Iterator[Client]) -> Generator[Client, None, None]:
    """Only active clients"""
    return (client for client in clients if client.active)


def email_client(clients: Iterator[Client]) -> None:
    """Send an email to a given list of clients.
    """
    for client in active_clients(clients):
        email(client)
```

## Function arguments (2 or fewer ideally)

A large amount of parameters is usually the sign that a function is
doing too much (has more than one responsibility). Try to decompose it
into smaller functions having a reduced set of parameters, ideally less than
three.

If the function has a single responsibility, consider if you can bundle
some or all parameters into a specialized object that will be passed as an
argument to the function. These parameters might be attributes of a single
entity that you can represent with a dedicated data structure. You may also
be able to reuse this entity elsewhere in your program. The reason why this is
a better arrangement is than having multiple parameters is that we may be able
to move some computations, done with those parameters inside the
function, into methods belonging to the new object, therefore reducing the
complexity of the function.

**Bad:**

```python
def create_menu(title, body, button_text, cancellable):
    pass
```

**Java-esque**:

```python
class Menu:
    def __init__(self, config: dict):
        self.title = config["title"]
        self.body = config["body"]
        # ...


menu = Menu(
    {
        "title": "My Menu",
        "body": "Something about my menu",
        "button_text": "OK",
        "cancellable": False
    }
)
```

**Also good**

```python
class MenuConfig:
    """A configuration for the Menu.

    Attributes:
        title: The title of the Menu.
        body: The body of the Menu.
        button_text: The text for the button label.
        cancellable: Can it be cancelled?
    """
    title: str
    body: str
    button_text: str
    cancellable: bool = False


def create_menu(config: MenuConfig) -> None:
    title = config.title
    body = config.body
    # ...


config = MenuConfig()
config.title = "My delicious menu"
config.body = "A description of the various items on the menu"
config.button_text = "Order now!"
# The instance attribute overrides the default class attribute.
config.cancellable = True

create_menu(config)
```

**Fancy**

```python
from typing import NamedTuple


class MenuConfig(NamedTuple):
    """A configuration for the Menu.

    Attributes:
        title: The title of the Menu.
        body: The body of the Menu.
        button_text: The text for the button label.
        cancellable: Can it be cancelled?
    """
    title: str
    body: str
    button_text: str
    cancellable: bool = False


def create_menu(config: MenuConfig):
    title, body, button_text, cancellable = config
    # ...


create_menu(
    MenuConfig(
        title="My delicious menu",
        body="A description of the various items on the menu",
        button_text="Order now!"
    )
)
```

**Even fancier**

```python
from dataclasses import astuple, dataclass


@dataclass
class MenuConfig:
    """A configuration for the Menu.

    Attributes:
        title: The title of the Menu.
        body: The body of the Menu.
        button_text: The text for the button label.
        cancellable: Can it be cancelled?
    """
    title: str
    body: str
    button_text: str
    cancellable: bool = False


def create_menu(config: MenuConfig):
    title, body, button_text, cancellable = astuple(config)
    # ...


create_menu(
    MenuConfig(
        title="My delicious menu",
        body="A description of the various items on the menu",
        button_text="Order now!"
    )
)
```

**Even fancier, Python3.8+ only**

```python
from typing import TypedDict


class MenuConfig(TypedDict):
    """A configuration for the Menu.

    Attributes:
        title: The title of the Menu.
        body: The body of the Menu.
        button_text: The text for the button label.
        cancellable: Can it be cancelled?
    """
    title: str
    body: str
    button_text: str
    cancellable: bool


def create_menu(config: MenuConfig):
    title = config["title"]
    # ...


create_menu(
    # You need to supply all the parameters
    MenuConfig(
        title="My delicious menu",
        body="A description of the various items on the menu",
        button_text="Order now!",
        cancellable=True
    )
)
```

## Function names should say what they do

**Bad:**

```python
class Email:
    def handle(self) -> None:
        pass


message = Email()
# What is this supposed to do again?
message.handle()
```

**Good:**

```python
class Email:
    def send(self) -> None:
        """Send this message"""


message = Email()
message.send()
```

## Functions should only be one level of abstraction

When you have more than one level of abstraction, your function is usually
doing too much. Splitting up functions leads to reusability and easier testing.

**Bad:**

```python
# type: ignore

def parse_better_js_alternative(code: str) -> None:
    regexes = [
        # ...
    ]

    statements = code.split('\n')
    tokens = []
    for regex in regexes:
        for statement in statements:
            pass

    ast = []
    for token in tokens:
        pass

    for node in ast:
        pass
```

**Good:**

```python
from typing import Tuple, List, Dict

REGEXES: Tuple = (
    # ...
)


def parse_better_js_alternative(code: str) -> None:
    tokens: List = tokenize(code)
    syntax_tree: List = parse(tokens)

    for node in syntax_tree:
        pass


def tokenize(code: str) -> List:
    statements = code.split()
    tokens: List[Dict] = []
    for regex in REGEXES:
        for statement in statements:
            pass

    return tokens


def parse(tokens: List) -> List:
    syntax_tree: List[Dict] = []
    for token in tokens:
        pass

    return syntax_tree
```

## Don't use flags as function parameters

Flags tell your user that this function does more than one thing. Functions
should do one thing. Split your functions if they are following different code
paths based on a boolean.

**Bad:**

```python
from tempfile import gettempdir
from pathlib import Path


def create_file(name: str, temp: bool) -> None:
    if temp:
        (Path(gettempdir()) / name).touch()
    else:
        Path(name).touch()
```

**Good:**

```python
from tempfile import gettempdir
from pathlib import Path


def create_file(name: str) -> None:
    Path(name).touch()


def create_temp_file(name: str) -> None:
    (Path(gettempdir()) / name).touch()
```

## Avoid side effects

A function produces a side effect if it does anything other than take a value
in and return another value or values. For example, a side effect could be
writing to a file, modifying some global variable, or accidentally wiring all
your money to a stranger.

Now, you do need to have side effects in a program on occasion - for example,
like in the previous example, you might need to write to a file. In these
cases, you should centralize and indicate where you are incorporating side
effects. Don't have several functions and classes that write to a particular
file - rather, have one
(and only one) service that does it.

The main point is to avoid common pitfalls like sharing state between objects
without any structure, using mutable data types that can be written to by
anything, or using an instance of a class, and not centralizing where your side
effects occur. If you can do this, you will be happier than the vast majority
of other programmers.

**Bad:**

```python
# type: ignore

# This is a module-level name.
# It's good practice to define these as immutable values, such as a string.
# However...
fullname = "Ryan McDermott"


def split_into_first_and_last_name() -> None:
    # The use of the global keyword here is changing the meaning of the
    # the following line. This function is now mutating the module-level
    # state and introducing a side-effect!
    global fullname
    fullname = fullname.split()


split_into_first_and_last_name()

# MyPy will spot the problem, complaining about 'Incompatible types in
# assignment: (expression has type "List[str]", variable has type "str")'
print(fullname)  # ["Ryan", "McDermott"]

# OK. It worked the first time, but what will happen if we call the
# function again?
```

**Good:**

```python
from typing import List, AnyStr


def split_into_first_and_last_name(name: AnyStr) -> List[AnyStr]:
    return name.split()


fullname = "Ryan McDermott"
name, surname = split_into_first_and_last_name(fullname)

print(name, surname)  # => Ryan McDermott
```

**Also good**

```python
from dataclasses import dataclass


@dataclass
class Person:
    name: str

    @property
    def name_as_first_and_last(self) -> list:
        return self.name.split()


# The reason why we create instances of classes is to manage state!
person = Person("Ryan McDermott")
print(person.name)  # => "Ryan McDermott"
print(person.name_as_first_and_last)  # => ["Ryan", "McDermott"]
```
