# Modules

## Export

```ts
export interface StringValidator {
  isAcceptable(s: string): boolean;
}

export class ZipCodeValidator implements StringValidator {
  isAcceptable(s: string) {
    return s.length === 5;
  }
}
```

## Import

```ts
import { ZipCodeValidator } from "./ZipCodeValidator";

let myValidator = new ZipCodeValidator();
```

## Namespaces

```ts
namespace Validation {
  export interface StringValidator {
    isAcceptable(s: string): boolean;
  }

  export class LettersOnlyValidator implements StringValidator {
    isAcceptable(s: string) {
      return /^[A-Za-z]+$/.test(s);
    }
  }
}

let validator = new Validation.LettersOnlyValidator();
```
