# Set

## Create Set

```javascript
// Empty Set Object
const emptySet = new Set();

// Set Object with values
const setObj = new Set([1, true, "hi"]);
```

## Add

```javascript
const emptySet = new Set();

// add values
emptySet.add("a"); // 'a'
emptySet.add(1); // 'a', 1
emptySet.add(true); // 'a', 1, true
emptySet.add("a"); // 'a', 1, true
```

## Delete

```javascript
const emptySet = new Set([1, true, "a"]);

// delete values
emptySet.delete("a"); // 1, true
emptySet.delete(true); // 1
emptySet.delete(1); //
```

## Has

```javascript
const setObj = new Set([1, true, "a"]);

// returns true or false
setObj.has("a"); // true
setObj.has(1); // true
setObj.has(false); // false
```

## Clear

```javascript
const setObj = new Set([1, true, "a"]);

// clears the set
console.log(setObj); // 1, true, 'a'
setObj.clear(); //
```

## Size

```javascript
const setObj = new Set([1, true, "a"]);

consoloe.log(setObj.size); // 3
```

## ForEach

```javascript
const setObj = new Set([1, true, "a"]);

setObj.forEach(function (value) {
  console.log(value);
});

// 1
// true
// 'a'
```
