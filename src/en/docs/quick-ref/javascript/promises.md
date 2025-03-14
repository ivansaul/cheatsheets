# Promises

## Promise states

```javascript
const promise = new Promise((resolve, reject) => {
  const res = true;
  // An asynchronous operation.
  if (res) {
    resolve("Resolved!");
  } else {
    reject(Error("Error"));
  }
});

promise.then(
  (res) => console.log(res),
  (err) => console.error(err),
);
```

## Executor function

```javascript
const executorFn = (resolve, reject) => {
  resolve("Resolved!");
};

const promise = new Promise(executorFn);
```

## setTimeout()

```javascript
const loginAlert = () => {
  console.log("Login");
};

setTimeout(loginAlert, 6000);
```

## .then() method

```javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("Result");
  }, 200);
});

promise.then(
  (res) => {
    console.log(res);
  },
  (err) => {
    console.error(err);
  },
);
```

## Promise.catch()

```javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    reject(Error("Promise Rejected Unconditionally."));
  }, 1000);
});

promise.then((res) => {
  console.log(value);
});

promise.catch((err) => {
  console.error(err);
});
```

## Promise.all()

```javascript
const promise1 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve(3);
  }, 300);
});
const promise2 = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve(2);
  }, 200);
});

Promise.all([promise1, promise2]).then((res) => {
  console.log(res[0]);
  console.log(res[1]);
});
```

## Avoiding nested Promise and .then()

```javascript
const promise = new Promise((resolve, reject) => {
  setTimeout(() => {
    resolve("*");
  }, 1000);
});

const twoStars = (star) => {
  return star + star;
};

const oneDot = (star) => {
  return star + ".";
};

const print = (val) => {
  console.log(val);
};

// Chaining them all together
promise.then(twoStars).then(oneDot).then(print);
```

## Creating

```javascript
const executorFn = (resolve, reject) => {
  console.log("The executor function of the promise!");
};

const promise = new Promise(executorFn);
```

## Chaining multiple .then()

```javascript
const promise = new Promise((resolve) => setTimeout(() => resolve("dAlan"), 100));

promise
  .then((res) => {
    return res === "Alan" ? Promise.resolve("Hey Alan!") : Promise.reject("Who are you?");
  })
  .then(
    (res) => {
      console.log(res);
    },
    (err) => {
      console.error(err);
    },
  );
```

## Fake http Request with Promise

```javascript
const mock = (success, timeout = 1000) => {
  return new Promise((resolve, reject) => {
    setTimeout(() => {
      if (success) {
        resolve({ status: 200, data: {} });
      } else {
        reject({ message: "Error" });
      }
    }, timeout);
  });
};
const someEvent = async () => {
  try {
    await mock(true, 1000);
  } catch (e) {
    console.log(e.message);
  }
};
```
