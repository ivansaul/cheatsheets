# Não se repita (DRY)

Mais informações sobre o príncipio [DRY](https://en.wikipedia.org/wiki/Don%27t_repeat_yourself).

Como programador, você deve evitar código duplicado. A duplicação é ruim porque isso significa
que há mais de um lugar para alterar algo, se precisar mudar alguma lógica

Imagine que você é dono de um restaurante e você toma conta do seu estoque: todos os seus tomates, cebolas, alhos, temperos, etc. Se você tem multiplas listas onde guarda estas informações, então você terá que atualizar todas elas quando servir um prato que tenha tomates. Se você tivesse apenas uma lista, teria apenas um lugar para atualizar!

Frequentemente, você possui código duplicado porque você tem duas ou mais coisas levemente diferentes, que possuem muito em comum, mas suas diferenças lhe forçam a ter mais duas ou três funções que fazem muito das mesmas coisas. Remover código duplicado significa criar uma abstração que seja capaz de lidar com este conjunto de coisas diferentes com apenas uma função/módulo/classe.

Conseguir a abstração correta é crítico, por isso que você deveria seguir os princípios SOLID descritos na seção Classes. Abstrações ruins podem ser piores do que código duplicado, então tome cuidado! Dito isto, se você puder fazer uma boa abstração, faça-a! Não repita a si mesmo, caso contrário você se pegará atualizando muitos lugares toda vez que precisar mudar qualquer coisinha.

**Ruim:**

```python
from typing import List, Text, Dict
from dataclasses import dataclass

@dataclass
class Developer:
    def __init__(self, experience: float, github_link: Text) -> None:
        self._experience = experience
        self._github_link = github_link
        
    @property
    def experience(self) -> float:
        return self._experience
    
    @property
    def github_link(self) -> Text:
        return self._github_link
    
@dataclass
class Manager:
    def __init__(self, experience: float, github_link: Text) -> None:
        self._experience = experience
        self._github_link = github_link
        
    @property
    def experience(self) -> float:
        return self._experience
    
    @property
    def github_link(self) -> Text:
        return self._github_link
    

def get_developer_list(developers: List[Developer]) -> List[Dict]:
    developers_list = []
    for developer in developers:
        developers_list.append({
        'experience' : developer.experience,
        'github_link' : developer.github_link
            })
    return developers_list

def get_manager_list(managers: List[Manager]) -> List[Dict]:
    managers_list = []
    for manager in managers:
        managers_list.append({
        'experience' : manager.experience,
        'github_link' : manager.github_link
            })
    return managers_list

## create list objects of developers
company_developers = [
    Developer(experience=2.5, github_link='https://github.com/1'),
    Developer(experience=1.5, github_link='https://github.com/2')
]
company_developers_list = get_developer_list(developers=company_developers)

## create list objects of managers
company_managers = [
    Manager(experience=4.5, github_link='https://github.com/3'),
    Manager(experience=5.7, github_link='https://github.com/4')
]
company_managers_list = get_manager_list(managers=company_managers)
```

**Bom:**

```python
from typing import List, Text, Dict
from dataclasses import dataclass

@dataclass
class Employee:
    def __init__(self, experience: float, github_link: Text) -> None:
        self._experience = experience
        self._github_link = github_link
        
    @property
    def experience(self) -> float:
        return self._experience
    
    @property
    def github_link(self) -> Text:
        return self._github_link
    


def get_employee_list(employees: List[Employee]) -> List[Dict]:
    employees_list = []
    for employee in employees:
        employees_list.append({
        'experience' : employee.experience,
        'github_link' : employee.github_link
            })
    return employees_list

## create list objects of developers
company_developers = [
    Employee(experience=2.5, github_link='https://github.com/1'),
    Employee(experience=1.5, github_link='https://github.com/2')
]
company_developers_list = get_employee_list(employees=company_developers)

## create list objects of managers
company_managers = [
    Employee(experience=4.5, github_link='https://github.com/3'),
    Employee(experience=5.7, github_link='https://github.com/4')
]
company_managers_list = get_employee_list(employees=company_managers)
```
