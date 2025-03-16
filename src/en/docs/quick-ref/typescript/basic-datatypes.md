# Basic Datatypes

## basic types

```ts
let isDone: boolean = false;
let age: number = 30;
let userName: string = "John";
let list: number[] = [1, 2, 3];
let tuple: [string, number] = ["hello", 10];
let notSure: any = 4;
notSure = "maybe a string instead";
```

## enums

```ts
enum Color {
  Red,
  Green,
  Blue,
}
let c: Color = Color.Green;
```

## interface

```ts
interface Person {
  firstName: string;
  lastName: string;
  age?: number; // Optional property
}

function greet(person: Person) {
  return "Hello, " + person.firstName + " " + person.lastName;
}
```

## Functions

```ts
function add(x: number, y: number): number {
  return x + y;
}

let myAdd = function (x: number, y: number): number {
  return x + y;
};

let myArrowAdd = (x: number, y: number): number => x + y;

function buildName(firstName: string, lastName = "Smith") {
  return firstName + " " + lastName;
}

function buildFullName(firstName: string, ...restOfName: string[]) {
  return firstName + " " + restOfName.join(" ");
}
```

## Classes

```ts
class Greeter {
  greeting: string;
  constructor(message: string) {
    this.greeting = message;
  }
  greet() {
    return "Hello, " + this.greeting;
  }
}

let greeter = new Greeter("world");
```

## Inheritance

```ts
class Animal {
  move(distance: number = 0) {
    console.log(`Animal moved ${distance} meters.`);
  }
}

class Dog extends Animal {
  bark() {
    console.log("Woof! Woof!");
  }
}

const dog = new Dog();
dog.bark();
dog.move(10);
dog.bark();
```

## Generics

```ts
function identity<T>(arg: T): T {
  return arg;
}

let output1 = identity<string>("myString");
let output2 = identity<number>(42);
```

## Type Assertions

```ts
let someValue: any = "this is a string";
let strLength: number = (<string>someValue).length;
// or
let strLength2: number = (someValue as string).length;
```
