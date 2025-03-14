# Type Hints

`Type hints` was introduced in `Python 3.5`, and it is a way to specify the type of a variable or an argument.

## Variable & Parameter

```python
string: str = "ha"
times: int = 3


# wrong hit, but run correctly
result: str = 1 + 2
print(result)  # => 3


def say(name: str, start: str = "Hi"):
    return start + ", " + name

print(say("Python"))  # => Hi, Python
```

## Built-in date type

```python
from typing import Dict, Tuple, List

bill: Dict[str, float] = {
    "apple": 3.14,
    "watermelon": 15.92,
    "pineapple": 6.53,
}
completed: Tuple[str] = ("DONE",)
succeeded: Tuple[int, str] = (1, "SUCCESS")
statuses: Tuple[str, ...] = (
    "DONE", "SUCCESS", "FAILED", "ERROR",
)
codes: List[int] = (0, 1, -1, -2)
```

## Built-in date type (3.10+)

```python
bill: dict[str, float] = {
    "apple": 3.14,
    "watermelon": 15.92,
    "pineapple": 6.53,
}
completed: tuple[str] = ("DONE",)
succeeded: tuple[int, str] = (1, "SUCCESS")
statuses: tuple[str, ...] = (
    "DONE", "SUCCESS", "FAILED", "ERROR",
)
codes: list[int] = (0, 1, -1, -2)
```

## Positional argument

```python
def calc_summary(*args: int):
    return sum(args)

print(calc_summary(3, 1, 4))  # => 8
```

Indicate all arguments' type is int.

## Returned

```python
def say_hello(name) -> str:
    return "Hello, " + name

var = "Python"
print(say_hello(var))  # => Hello, Python
```

## Union returned

```python
from typing import Union

def resp200(meaningful) -> Union[int, str]:
    return "OK" if meaningful else 200
```

Means returned value type may be int or str.

## Keyword argument

```python
def calc_summary(**kwargs: int):
    return sum(kwargs.values())

print(calc_summary(a=1, b=2))  # => 3
```

Indicate all parameters' value type is int.

## Multiple returns

```python
def resp200() -> (int, str):
    return 200, "OK"

returns = resp200()
print(returns)  # => (200, 'OK')
print(type(returns))  # tuple
```

## Union returned (3.10+)

```python
def resp200(meaningful) -> int | str:
    return "OK" if meaningful else 200
```

Since Python 3.10

## Property

```python
class Employee:
    name: str
    age: int

    def __init__(self, name, age):
        self.name = name
        self.age = age
        self.graduated: bool = False
```

## Self instance

```python
class Employee:
    name: str

    def set_name(self, name) -> "Employee":
        self.name = name
        return self

    def copy(self) -> 'Employee':
        return type(self)(self.name)
```

## Self instance (3.11+)

```python
from typing import Self

class Employee:
    name: str
    age: int

    def set_name(self: Self, name) -> Self:
        self.name = name
        return self
```

## Type & Generic

```python
from typing import TypeVar, Type

T = TypeVar("T")

# "mapper" is a type, like int, str, MyClass and so on.
# "default" is an instance of type T, such as 314, "string", MyClass() and so on.
# returned is an instance of type T too.
def converter(raw, mapper: Type[T], default: T) -> T:
    try:
        return mapper(raw)
    except:
        return default

raw: str = input("Enter an integer: ")
result: int = converter(raw, mapper=int, default=0)
```

## Function

```python
from typing import TypeVar, Callable, Any

T = TypeVar("T")

def converter(raw, mapper: Callable[[Any], T], default: T) -> T:
    try:
        return mapper(raw)
    except:
        return default

# Callable[[Any], ReturnType] means a function declare like:
# def func(arg: Any) -> ReturnType:
#     pass

# Callable[[str, int], ReturnType] means a function declare like:
# def func(string: str, times: int) -> ReturnType:
#     pass

# Callable[..., ReturnType] means a function declare like:
# def func(*args, **kwargs) -> ReturnType:
#     pass

def is_success(value) -> bool:
    return value in (0, "OK", True, "success")

resp = dict(code=0, message="OK", data=[])
successed: bool = converter(resp["message"], mapper=is_success, default=False)
```
