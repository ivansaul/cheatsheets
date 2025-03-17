# Classes  

## Princípio da Responsabilidade Única (SRP)  

Robert C. Martin escreve:  

> Uma classe deve ter apenas um motivo para mudar.  

Os "motivos para mudar" são, essencialmente, as responsabilidades gerenciadas por uma classe ou função.  

No exemplo a seguir, criamos um elemento HTML que representa um comentário com a versão do documento:  

**Ruim**  

```python
from importlib import metadata


class VersionCommentElement:
     """Um elemento que renderiza um comentário HTML com o número da versão do programa."""

     def get_version(self) -> str:
          """Obter a versão do pacote"""
          return metadata.version("pip")

     def render(self) -> None:
          print(f'<!-- Versão: {self.get_version()} -->')


VersionCommentElement().render()
```

Esta classe tem duas responsabilidades:  

- Recuperar o número da versão do pacote Python  
- Renderizar-se como um elemento HTML  

Qualquer alteração em uma dessas responsabilidades pode afetar a outra.  

Podemos reescrever a classe e separar essas responsabilidades:  

**Bom**  

```python
from importlib import metadata


def get_version(pkg_name: str) -> str:
     """Recuperar a versão de um determinado pacote"""
     return metadata.version(pkg_name)


class VersionCommentElement:
     """Um elemento que renderiza um comentário HTML com o número da versão do programa."""

     def __init__(self, version: str):
          self.version = version

     def render(self) -> None:
          print(f'<!-- Versão: {self.version} -->')


VersionCommentElement(get_version("pip")).render()
```

O resultado é que a classe agora só precisa se preocupar em renderizar a si mesma. Ela recebe o texto da versão durante a instanciação, e esse texto é gerado por uma função separada, `get_version()`. Alterar uma não afeta a outra, desde que o contrato entre elas permaneça o mesmo, ou seja, a função fornece uma string e o método `__init__` da classe aceita uma string.  

Como bônus adicional, `get_version()` agora pode ser reutilizada em outros lugares.  

## Princípio Aberto/Fechado (OCP)  

> "Incorpore novos recursos estendendo o sistema, não modificando-o."  
> Uncle Bob.  

Objetos devem estar abertos para extensão, mas fechados para modificação. Deve ser possível aumentar a funcionalidade de um objeto (por exemplo, uma classe) sem modificar seus contratos internos. Isso pode ser alcançado ao projetar o objeto para ser estendido de maneira clara.  

No exemplo a seguir, tentamos implementar um framework web simples que lida com requisições HTTP e retorna respostas. A classe `View` possui um único método `.get()`, que será chamado quando o servidor HTTP receber uma requisição GET de um cliente.  

`View` é intencionalmente simples e retorna respostas `text/plain`. No entanto, gostaríamos de retornar respostas HTML baseadas em um arquivo de modelo, então criamos uma subclasse chamada `TemplateView`.  

**Ruim**  

```python
from dataclasses import dataclass


@dataclass
class Response:
     """Uma resposta HTTP"""

     status: int
     content_type: str
     body: str


class View:
     """Uma visão simples que retorna respostas em texto puro"""

     def get(self, request) -> Response:
          """Lidar com uma requisição GET e retornar uma mensagem na resposta"""
          return Response(
               status=200,
               content_type='text/plain',
               body="Bem-vindo ao meu site"
          )


class TemplateView(View):
     """Uma visão que retorna respostas HTML baseadas em um arquivo de modelo."""

     def get(self, request) -> Response:
          """Lidar com uma requisição GET e retornar um documento HTML na resposta"""
          with open("index.html") as fd:
               return Response(
                    status=200,
                    content_type='text/html',
                    body=fd.read()
               )

```

A classe `TemplateView` modificou o comportamento interno de sua classe pai para permitir uma funcionalidade mais avançada. Ao fazer isso, agora depende de `View` não alterar a implementação do método `.get()`, que precisa permanecer inalterado. Não podemos, por exemplo, adicionar verificações adicionais a todas as classes derivadas de `View`, pois o comportamento foi sobrescrito em pelo menos um subtipo, o que exigiria sua atualização.  

Vamos redesenhar nossas classes para corrigir esse problema e permitir que `View` seja estendida (não modificada) de maneira mais limpa:  

**Bom**  

```python
from dataclasses import dataclass


@dataclass
class Response:
     """Uma resposta HTTP"""

     status: int
     content_type: str
     body: str


class View:
     """Uma visão simples que retorna respostas em texto puro"""

     content_type = "text/plain"

     def render_body(self) -> str:
          """Renderizar o corpo da mensagem da resposta"""
          return "Bem-vindo ao meu site"

     def get(self, request) -> Response:
          """Lidar com uma requisição GET e retornar uma mensagem na resposta"""
          return Response(
               status=200,
               content_type=self.content_type,
               body=self.render_body()
          )


class TemplateView(View):
     """Uma visão que retorna respostas HTML baseadas em um arquivo de modelo."""

     content_type = "text/html"
     template_file = "index.html"

     def render_body(self) -> str:
          """Renderizar o corpo da mensagem como HTML"""
          with open(self.template_file) as fd:
               return fd.read()
```

Observe que precisamos sobrescrever apenas o método `render_body()`, que tem uma responsabilidade bem definida e **permite que subtipos o sobrescrevam**. Ele foi projetado para ser estendido.  

Outra boa abordagem para combinar os benefícios da herança e da composição de objetos é usar [Mixins](https://docs.djangoproject.com/en/4.1/topics/class-based-views/mixins/).  

Mixins são classes minimalistas projetadas para serem usadas exclusivamente em conjunto com outras classes relacionadas. Elas são "misturadas" à classe-alvo por meio de herança múltipla para modificar seu comportamento.  

Algumas regras:  

- Mixins devem sempre herdar de `object`.  
- Mixins sempre vêm antes da classe-alvo,  
  ex.: `class Foo(MixinA, MixinB, TargetClass): ...`  

**Também bom**  

```python
from dataclasses import dataclass, field
from typing import Protocol


@dataclass
class Response:
     """Uma resposta HTTP"""

     status: int
     content_type: str
     body: str
     headers: dict = field(default_factory=dict)


class View:
     """Uma visão simples que retorna respostas em texto puro"""

     content_type = "text/plain"

     def render_body(self) -> str:
          """Renderizar o corpo da mensagem da resposta"""
          return "Bem-vindo ao meu site"

     def get(self, request) -> Response:
          """Lidar com uma requisição GET e retornar uma mensagem na resposta"""
          return Response(
               status=200,
               content_type=self.content_type,
               body=self.render_body()
          )


class TemplateRenderMixin:
     """Mixin para visões que renderizam documentos HTML usando um arquivo de modelo.
 
     Não deve ser usada sozinha!
     """
     template_file: str = ""

     def render_body(self) -> str:
          """Renderizar o corpo da mensagem como HTML"""
          if not self.template_file:
               raise ValueError("O caminho para um arquivo de modelo deve ser fornecido.")

          with open(self.template_file) as fd:
               return fd.read()


class ContentLengthMixin:
     """Mixin que adiciona um cabeçalho Content-Length na resposta.
 
     Não deve ser usada sozinha!
     """

     def get(self, request) -> Response:
          """Modificar a resposta para incluir o novo cabeçalho"""
          response = super().get(request)  # type: ignore
          response.headers['Content-Length'] = len(response.body)
          return response


class TemplateView(TemplateRenderMixin, ContentLengthMixin, View):
     """Uma visão que retorna respostas HTML baseadas em um arquivo de modelo."""

     content_type = "text/html"
     template_file = "index.html"
```

Mixins tornam a composição de objetos mais fácil, encapsulando funcionalidades reutilizáveis em classes com uma única responsabilidade, permitindo um desacoplamento limpo.

Aquí tienes la traducción al portugués:  

---

## Princípio da Substituição de Liskov (LSP)

> “Funções que usam ponteiros ou referências para classes base  
> devem ser capazes de usar objetos de classes derivadas sem saber disso”,  
> Uncle Bob.

Este princípio leva o nome de Barbara Liskov, que colaborou com a cientista da computação Jeannette Wing no artigo seminal  
*"A behavioral notion of subtyping" (1994).* Um dos conceitos centrais do artigo é que  
"um subtipo (deve) preservar o comportamento dos métodos do supertipo, bem como todas as propriedades invariantes e históricas do supertipo".

Em essência, uma função que aceita um supertipo também deve aceitar todos os seus  
subtipos sem necessidade de modificação.

Você consegue identificar o problema no seguinte código?

**Ruim**

```python
from dataclasses import dataclass


@dataclass
class Response:
     """Uma resposta HTTP"""

     status: int
     content_type: str
     body: str


class View:
     """Uma view simples que retorna respostas em texto puro"""

     content_type = "text/plain"

     def render_body(self) -> str:
          """Renderiza o corpo da mensagem da resposta"""
          return "Bem-vindo ao meu site"

     def get(self, request) -> Response:
          """Lida com uma requisição GET e retorna uma mensagem na resposta"""
          return Response(
               status=200,
               content_type=self.content_type,
               body=self.render_body()
          )


class TemplateView(View):
     """Uma view que retorna respostas HTML baseadas em um arquivo de template."""

     content_type = "text/html"

     def get(self, request, template_file: str) -> Response:  # type: ignore
          """Renderiza o corpo da mensagem como HTML"""
          with open(template_file) as fd:
               return Response(
                    status=200,
                    content_type=self.content_type,
                    body=fd.read()
               )


def render(view: View, request) -> Response:
     """Renderiza uma View"""
     return view.get(request)

```

A expectativa é que a função `render()` consiga trabalhar com `View`  
e seu subtipo `TemplateView`, mas este último quebrou a compatibilidade  
ao modificar a assinatura do método `.get()`. Isso resultará em uma exceção `TypeError`  
quando usado com `TemplateView`.

Se quisermos que a função `render()` funcione com qualquer subtipo de `View`, devemos  
garantir que seu protocolo público não seja quebrado. Mas como saber qual é esse protocolo?  
Ferramentas de tipagem, como *mypy*, gerarão um erro ao detectar problemas como esse:

```
error: Signature of "get" incompatible with supertype "View"
<string>:36: note:      Superclasse:
<string>:36: note:          def get(self, request: Any) -> Response
<string>:36: note:      Subclasse:
<string>:36: note:          def get(self, request: Any, template_file: str) -> Response
```

## Princípio da Segregação de Interface (ISP)

> “Mantenha interfaces pequenas  
> para que os usuários não acabem dependendo de coisas que não precisam.”,  
> Uncle Bob.

Vários idiomas de programação orientada a objetos, como Java e Go,  
possuem o conceito de interfaces. Uma interface define os métodos e  
propriedades públicas de um objeto sem implementá-los. Elas são úteis quando não  
queremos acoplar a assinatura de uma função a um objeto concreto,  
mas sim dizer: "Não me importo com qual objeto você me dá, desde que ele tenha  
certos métodos e atributos que eu espero usar".

O Python não tem interfaces. Em vez disso, temos Classes Base Abstratas (ABCs),  
que são um pouco diferentes, mas podem servir ao mesmo propósito.

**Bom**

```python
from abc import ABCMeta, abstractmethod


# Define a Classe Abstrata para um objeto genérico Greeter
class Greeter(metaclass=ABCMeta):
     """Um objeto que pode executar uma ação de saudação."""

     @staticmethod
     @abstractmethod
     def greet(name: str) -> None:
          """Exibe uma saudação para o usuário com o nome fornecido"""


class FriendlyActor(Greeter):
     """Um ator que cumprimenta o usuário com uma saudação amigável"""

     @staticmethod
     def greet(name: str) -> None:
          """Cumprimenta uma pessoa pelo nome"""
          print(f"Olá {name}!")


def welcome_user(user_name: str, actor: Greeter):
     """Dá boas-vindas a um usuário com um nome específico usando o ator fornecido"""
     actor.greet(user_name)


welcome_user("Barbara", FriendlyActor())
```

Agora imagine o seguinte cenário: temos vários documentos PDF  
que criamos e queremos disponibilizar para os visitantes do nosso site.  
Estamos usando um framework web em Python e poderíamos projetar uma classe  
para gerenciar esses documentos. Então, criamos uma classe base abstrata  
abrangente para nosso documento.

**Erro**

```python
import abc


class Persistable(metaclass=abc.ABCMeta):
     """Serializa um arquivo para dados e vice-versa"""

     @property
     @abc.abstractmethod
     def data(self) -> bytes:
          """Os dados brutos do arquivo"""

     @classmethod
     @abc.abstractmethod
     def load(cls, name: str):
          """Carrega o arquivo do disco"""

     @abc.abstractmethod
     def save(self) -> None:
          """Salva o arquivo no disco"""


class PDFDocument(Persistable):
     """Um documento PDF"""

     @property
     def data(self) -> bytes:
          """Os bytes brutos do documento PDF"""
          ...  # Código omitido

     @classmethod
     def load(cls, name: str):
          """Carrega o arquivo do sistema de arquivos local"""
          ...  # Código omitido


def view(request):
     """Uma view que lida com uma requisição GET para um documento"""
     requested_name = request.qs['name']
     return PDFDocument.load(requested_name).data
```

Porém, não podemos instanciar `PDFDocument` sem implementar `.save()`,  
o que gera um erro:

```
Can't instantiate abstract class PDFDocument with abstract method save.
```

O problema é que criamos uma *interface* que tem recursos que não precisamos agora.  
A solução é decompor a interface em interfaces menores e compostáveis.

**Bom**

```python
import abc


class DataCarrier(metaclass=abc.ABCMeta):
     """Carrega um conjunto de dados"""

     @property
     def data(self):
          ...


class Loadable(DataCarrier):
     """Pode carregar dados do armazenamento pelo nome"""

     @classmethod
     @abc.abstractmethod
     def load(cls, name: str):
          ...


class Saveable(DataCarrier):
     """Pode salvar dados no armazenamento"""

     @abc.abstractmethod
     def save(self) -> None:
          ...


class PDFDocument(Loadable):
     """Um documento PDF"""

     @property
     def data(self) -> bytes:
          ...  # Código omitido

     @classmethod
     def load(cls, name: str) -> None:
          ...  # Código omitido


def view(request):
     """Uma view que lida com uma requisição GET para um documento"""
     requested_name = request.qs['name']
     return PDFDocument.load(requested_name).data
```

---

## Princípio da Inversão de Dependência (DIP)

> “Dependa de abstrações, não de detalhes concretos.”  
> Uncle Bob.

Imagine que queremos escrever uma view web que retorna uma resposta HTTP  
transmitindo linhas de um arquivo CSV gerado dinamicamente.  
Queremos usar o escritor CSV da biblioteca padrão.

**Ruim**

```python
import csv
from io import StringIO


class StreamingHttpResponse:
     """Uma resposta HTTP em streaming"""
     ...  # Código omitido


def some_view(request):
     rows = (
          ['Primeira linha', 'Foo', 'Bar', 'Baz'],
          ['Segunda linha', 'A', 'B', 'C', '"Teste"', "Aqui está uma citação"]
     )

     def stream():
          buffer_ = StringIO()
          writer = csv.writer(buffer_, delimiter=';', quotechar='"')
          for row in rows:
               writer.writerow(row)
               buffer_.seek(0)
               data = buffer_.read()
               buffer_.seek(0)
               buffer_.truncate()
               yield data

     response = StreamingHttpResponse(stream(), content_type='text/csv')
     response['Content-Disposition'] = 'attachment; filename="arquivo.csv"'

     return response
```

Essa implementação é trabalhosa. Uma melhor abordagem é usar um objeto  
que implemente `.write()` para retornar os dados imediatamente.

Este exemplo foi retirado de [uma contribuição feita para a documentação do Django](https://code.djangoproject.com/ticket/21179) por este autor.
