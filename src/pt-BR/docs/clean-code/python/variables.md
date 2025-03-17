# Variáveis

## Use nomes significantes e pronunciáveis em suas variáveis

**Ruim:**

```python
import datetime


ymdstr = datetime.date.today().strftime("%y-%m-%d")
```

**Bom**:

```python
import datetime


current_date: str = datetime.date.today().strftime("%y-%m-%d")
```

## Use o mesmo vocabulário para o mesmo tipo de variável

**Ruim:**
Usamos três nomes diferentes para a mesma entidade:

```python
def get_user_info(): pass
def get_client_data(): pass
def get_customer_record(): pass
```

**Bom**:
Se a entidade for a mesma, você deve ser consistente ao se referir a ela em suas funções:

```python
def get_user_info(): pass
def get_user_data(): pass
def get_user_record(): pass
```

**Melhor ainda**:
Python é (também) uma linguagem de programação orientada a objetos. Se fizer sentido, empacote as funções junto com a implementação concreta da entidade em seu código, como atributos de instância, métodos ou métodos de propriedade:

```python
from typing import Union, Dict, Text


class Record:
    pass


class User:
    info : str

    @property
    def data(self) -> Dict[Text, Text]:
        return {}

    def get_record(self) -> Union[Record, None]:
        return Record()
```

## Use nomes fáceis de pesquisar

Nós vamos ler mais código do que escrever, por isso é importante que o código que escrevemos seja legível e fácil de achar. Ao *não* nomear variáveis, prejudicamos nossos leitores.
Torne seus nomes fáceis de procurar.

**Ruim:**

```python
import time


# Para que é o número 86400?
time.sleep(86400)
```

**Bom**:

```python
import time


# Declare-os no namespace global do módulo.
SECONDS_IN_A_DAY = 60 * 60 * 24
time.sleep(SECONDS_IN_A_DAY)
```

## Use variáveis explicativas

**Ruim:**

```python
import re


address = "One Infinite Loop, Cupertino 95014"
city_zip_code_regex = r"^[^,\\]+[,\\\s]+(.+?)\s*(\d{5})?$"

matches = re.match(city_zip_code_regex, address)
if matches:
    print(f"{matches[1]}: {matches[2]}")
```

**Nada mal**: É melhor, mas ainda dependemos muito do regex.

```python
import re


address = "One Infinite Loop, Cupertino 95014"
city_zip_code_regex = r"^[^,\\]+[,\\\s]+(.+?)\s*(\d{5})?$"
matches = re.match(city_zip_code_regex, address)

if matches:
    city, zip_code = matches.groups()
    print(f"{city}: {zip_code}")
```

**Bom**: Diminua a dependência de regex nomeando as variáveis em subgrupo

```python
import re


address = "One Infinite Loop, Cupertino 95014"
city_zip_code_regex = r"^[^,\\]+[,\\\s]+(?P<city>.+?)\s*(?P<zip_code>\d{5})?$"

matches = re.match(city_zip_code_regex, address)
if matches:
    print(f"{matches['city']}, {matches['zip_code']}")
```

## Evite mapear mentalmente

Não force o leitor do seu código a traduzir o que a variável significa.
Explicito é melhor que implito.

**Ruim:**

```python
seq = ("Austin", "New York", "San Francisco")

for item in seq:
    #do_stuff()
    #do_some_other_stuff()

    # Espere, `item` de novo?
    print(item)
```

**Bom**:

```python
locations = ("Austin", "New York", "San Francisco")

for location in locations:
    #do_stuff()
    #do_some_other_stuff()
    # ...
    print(location)
```

## Não adicione contextos desnecessários

Se o nome da sua classe/objeto expressa algo, não repita isso no nome da variável.

**Ruim:**

```python
class Car:
    car_make: str
    car_model: str
    car_color: str
```

**Bom**:

```python
class Car:
    make: str
    model: str
    color: str
```

## Use argumentos padrões ao invés de encadear condicionais

**Muito ruim**

Porque escrever:

```python
import hashlib


def create_micro_brewery(name):
    name = "Hipster Brew Co." if name is None else name
    slug = hashlib.sha1(name.encode()).hexdigest()
    # etc.
```

... quando você pode especificar um argumento padrão em vez disso? Isso também deixa claro que
você está esperando uma string como argumento.

**Bom**:

```python
from typing import Text
import hashlib


def create_micro_brewery(name: Text = "Hipster Brew Co."):
    slug = hashlib.sha1(name.encode()).hexdigest()
    # etc.
```
