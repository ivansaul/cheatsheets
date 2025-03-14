# Objects

## Accessing Properties

```javascript
const apple = {
  color: "Green",
  price: { bulk: "$3/kg", smallQty: "$4/kg" },
};
console.log(apple.color); // => Green
console.log(apple.price.bulk); // => $3/kg
```

## Naming Properties

```javascript
// Example of invalid key names
const trainSchedule = {
  // Invalid because of the space between words.
  platform num: 10,
  // Expressions cannot be keys.
  40 - 10 + 2: 30,
  // A + sign is invalid unless it is enclosed in quotations.
  +compartment: 'C'
}
```

## Non-existent properties

```javascript
const classElection = {
  date: "January 12",
};

console.log(classElection.place); // undefined
```

## Mutable

```javascript
const student = {
  name: "Sheldon",
  score: 100,
  grade: "A",
};

console.log(student);
// { name: 'Sheldon', score: 100, grade: 'A' }

delete student.score;
student.grade = "F";
console.log(student);
// { name: 'Sheldon', grade: 'F' }

student = {};
// TypeError: Assignment to constant variable.
```

## Assignment shorthand syntax

```javascript
const person = {
  name: "Tom",
  age: "22",
};
const { name, age } = person;
console.log(name); // 'Tom'
console.log(age); // '22'
```

## Delete operator

```javascript
const person = {
  firstName: "Matilda",
  age: 27,
  hobby: "knitting",
  goal: "learning JavaScript",
};

delete person.hobby; // or delete person[hobby];

console.log(person);
/*
{
  firstName: "Matilda"
  age: 27
  goal: "learning JavaScript"
}
*/
```

## Objects as arguments

```javascript
const origNum = 8;
const origObj = { color: "blue" };

const changeItUp = (num, obj) => {
  num = 7;
  obj.color = "red";
};

changeItUp(origNum, origObj);

// Will output 8 since integers are passed by value.
console.log(origNum);

// Will output 'red' since objects are passed
// by reference and are therefore mutable.
console.log(origObj.color);
```

## Shorthand object creation

```javascript
const activity = "Surfing";
const beach = { activity };
console.log(beach); // { activity: 'Surfing' }
```

## this Keyword

```javascript
const cat = {
  name: "Pipey",
  age: 8,
  whatName() {
    return this.name;
  },
};
console.log(cat.whatName()); // => Pipey
```

## Factory functions

```javascript
// A factory function that accepts 'name',
// 'age', and 'breed' parameters to return
// a customized dog object.
const dogFactory = (name, age, breed) => {
  return {
    name: name,
    age: age,
    breed: breed,
    bark() {
      console.log("Woof!");
    },
  };
};
```

## Object methods

```javascript
const engine = {
  // method shorthand, with one argument
  start(adverb) {
    console.log(`The engine starts up ${adverb}...`);
  },
  // anonymous arrow function expression with no arguments
  sputter: () => {
    console.log("The engine sputters...");
  },
};

engine.start("noisily");
engine.sputter();
```

## Getters and setters

```javascript
const myCat = {
  _name: "Dottie",
  get name() {
    return this._name;
  },
  set name(newName) {
    this._name = newName;
  },
};

// Reference invokes the getter
console.log(myCat.name);

// Assignment invokes the setter
myCat.name = "Yankee";
```
