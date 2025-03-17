# Funções

## Argumentos de funções (2 ou menos, idealmente)

Limitar a quantidade de parametros de uma função é incrivelmente importantante porque isso torna sua função fácil de testar. Ter mais de três de leva em uma explosão onde você tem que testar vários casos diferentes, com argumentos separados.

Um ou dois argumentos é o caso ideal, e três deve ser evitado se possível. Algo além disso deve ser deixado de lado. Usualmente, se você tem mais de dois argumentos, suas funções estão tentando fazer coisas demais. Nos casos que não estão, na maior parte do tempo um objeto irá ser o suficiente como argumento.

**Ruim:**

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

**Muito bom**

```python
from typing import Text


class MenuConfig:
    """A configuration for the Menu.

    Attributes:
        title: The title of the Menu.
        body: The body of the Menu.
        button_text: The text for the button label.
        cancellable: Can it be cancelled?
    """
    title: Text
    body: Text
    button_text: Text
    cancellable: bool = False


def create_menu(config: MenuConfig) -> None:
    title = config.title
    body = config.body
    # ...


config = MenuConfig()
config.title = "My delicious menu"
config.body = "A description of the various items on the menu"
config.button_text = "Order now!"
# O atributo de instância substitui o atributo de classe padrão.
config.cancellable = True

create_menu(config)
```

**Chique**

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

**Ainda mais chique**

```python
from typing import Text
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
    title: Text
    body: Text
    button_text: Text
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

**Ainda mais chique, versões Python3.8+**

```python
from typing import TypedDict, Text


class MenuConfig(TypedDict):
    """A configuration for the Menu.

    Attributes:
        title: The title of the Menu.
        body: The body of the Menu.
        button_text: The text for the button label.
        cancellable: Can it be cancelled?
    """
    title: Text
    body: Text
    button_text: Text
    cancellable: bool


def create_menu(config: MenuConfig):
    title = config["title"]
    # ...


create_menu(
    # Você precisa informar todos os parâmetros
    MenuConfig(
        title="My delicious menu",
        body="A description of the various items on the menu",
        button_text="Order now!",
        cancellable=True
    )
)
```

## Funções devem fazer somente uma coisa

Esta é, de longe, a regra mais importante da engenharia de software. Quando as funções fazem mais de uma coisa, elas são mais difíceis de compor, testar e pensar sobre. Quando você consegue isolar a função para apenas uma ação, elas podem ser refatoradas sem muita dificuldade e seu código será fácilmente lido. Se você não tirar mais nada deste guia além disso, você estará à frente de muitos programadores.

**Ruim:**

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

**Bom**:

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

Você vê uma oportunidade para usar geradores agora?

**Melhor ainda**

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

## Nomes das funções devem dizer o que elas fazem

**Ruim:**

```python
class Email:
    def handle(self) -> None:
        pass

message = Email()
# O que isso quer dizer?
message.handle()
```

**Bom:**

```python
class Email:
    def send(self) -> None:
        """Send this message"""

message = Email()
message.send()
```

## Funções devem estar em apenas um nível de abstração

Quando você tem mais de um nível de abstração possívelmente sua função está fazendo coisa demais. Dividir suas funções desencadeia em código reusável e fácil de testar.

**Ruim:**

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

**Bom:**

```python
from typing import Tuple, List, Text, Dict


REGEXES: Tuple = (
   # ...
)


def parse_better_js_alternative(code: Text) -> None:
    tokens: List = tokenize(code)
    syntax_tree: List = parse(tokens)

    for node in syntax_tree:
        pass


def tokenize(code: Text) -> List:
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

## Não use sinalizadores como parâmetros de função

Os sinalizadores informam ao usuário que esta função faz mais de uma coisa. Funções
deve fazer uma coisa. Divida suas funções se elas estiverem seguindo um código diferente
caminhos baseados em verdadeiro ou falso.

**Ruim:**

```python
from typing import Text
from tempfile import gettempdir
from pathlib import Path


def create_file(name: Text, temp: bool) -> None:
    if temp:
        (Path(gettempdir()) / name).touch()
    else:
        Path(name).touch()
```

**Bom:**

```python
from typing import Text
from tempfile import gettempdir
from pathlib import Path


def create_file(name: Text) -> None:
    Path(name).touch()


def create_temp_file(name: Text) -> None:
    (Path(gettempdir()) / name).touch()
```

## Evite efeitos colaterais

Uma função produz um efeito colateral se fizer qualquer coisa além de assumir um valor ao invés de retornar outro valor ou valores. Por exemplo, um efeito colateral pode ser a escrita
a um arquivo, modificando alguma variável global ou transferindo acidentalmente todo o seu dinheiro
para um estranho.

No entanto, você precisa ter efeitos colaterais em um programa de vez em quando - por exemplo, como
no exemplo anterior, você pode precisar gravar em um arquivo. Nestes casos, você
deve centralizar e indicar onde você está incorporando efeitos colaterais. Não tem
várias funções e classes que gravam em um arquivo específico - em vez disso, têm um
(e apenas um) serviço que o faz.

O ponto principal é evitar armadilhas comuns, como o compartilhamento de estado entre objetos
sem qualquer estrutura, usando tipos de dados mutáveis ​​que podem ser gravados por qualquer coisa ou usando uma instância de uma classe, e não centralizando onde ocorrem seus efeitos colaterais.
Se você puder fazer isso, ficará mais feliz do que a grande maioria dos outros programadores.

**Ruim:**

```python
# type: ignore

# Este é um nome de nível de módulo..
# É uma boa prática defini-los como valores imutáveis, como uma string.
# No entanto...
fullname = "Ryan McDermott"

def split_into_first_and_last_name() -> None:
    # O uso da palavra-chave global aqui está mudando o significado da
    # seguinte linha. Esta função agora está alterando o nível do módulo
    # estado e introduzindo um efeito colateral!
    global fullname
    fullname = fullname.split()

split_into_first_and_last_name()

# MyPy irá detectar o problema,  'Incompatible types in
# assignment: (expression has type "List[str]", variable has type "str")'
print(fullname)  # ["Ryan", "McDermott"]

# OK. Funcionou da primeira vez, mas o que acontecerá se chamarmos de
# funcionar de novo?
```

**Bom:**

```python
from typing import List, AnyStr


def split_into_first_and_last_name(name: AnyStr) -> List[AnyStr]:
    return name.split()

fullname = "Ryan McDermott"
name, surname = split_into_first_and_last_name(fullname)

print(name, surname)  # => Ryan McDermott
```

**Muito bom**

```python
from typing import Text
from dataclasses import dataclass


@dataclass
class Person:
    name: Text

    @property
    def name_as_first_and_last(self) -> list:
        return self.name.split()


# A razão pela qual criamos instâncias de classes é para gerenciar o estado!
person = Person("Ryan McDermott")
print(person.name)  # => "Ryan McDermott"
print(person.name_as_first_and_last)  # => ["Ryan", "McDermott"]
```
