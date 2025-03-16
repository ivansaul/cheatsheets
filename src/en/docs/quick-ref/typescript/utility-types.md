# Utility Types

## Partial

```ts
interface User {
  id: number;
  name: string;
  age: number;
}

let partialUser: Partial<User> = {
  name: "Alice",
};
```

## Readonly

```ts
let readonlyUser: Readonly<User> = {
  id: 1,
  name: "Bob",
  age: 25,
};

// readonlyUser.age = 26; // Error: cannot reassign a readonly property
```

## Pick

```ts
type UserName = Pick<User, "name">;

let userName: UserName = {
  name: "Charlie",
};
```

## Omit

```ts
type UserWithoutAge = Omit<User, "age">;

let userWithoutAge: UserWithoutAge = {
  id: 2,
  name: "Dave",
};
```
