# Miscellaneous

## Basic error handling

```php
try {
    // Do something
} catch (Exception $e) {
    // Handle exception
} finally {
    echo "Always print!";
}
```

## Exception in PHP 8.0

```php
$nullableValue = null;

try {
 $value = $nullableValue ?? throw new InvalidArgumentException();
} catch (InvalidArgumentException) { // Variable is optional
    // Handle my exception
    echo "print me!";
}
```

## Custom exception

```php
class MyException extends Exception {
    // do something
}
```

Usage

```php
try {
    $condition = true;
    if ($condition) {
        throw new MyException('bala');
    }
} catch (MyException $e) {
    // Handle my exception
}
```

## Nullsafe Operator

```php
// As of PHP 8.0.0, this line:
$result = $repo?->getUser(5)?->name;

// Equivalent to the following code:
if (is_null($repo)) {
    $result = null;
} else {
    $user = $repository->getUser(5);
    if (is_null($user)) {
        $result = null;
    } else {
        $result = $user->name;
    }
}
```

See also: [Nullsafe Operator](https://wiki.php.net/rfc/nullsafe_operator)

## Regular expressions

```php
$str = "Visit cheatsheets.zip";
echo preg_match("/ch/i", $str); # => 1
```

See: [Regex in PHP](/regex#regex-in-php)

## fopen() mode

| -    | -                        |
| ---- | ------------------------ |
| `r`  | Read                     |
| `r+` | Read and write, prepend  |
| `w`  | Write, truncate          |
| `w+` | Read and write, truncate |
| `a`  | Write, append            |
| `a+` | Read and write, append   |

## Runtime defined Constants

```php
define("CURRENT_DATE", date('Y-m-d'));

// One possible representation
echo CURRENT_DATE;   # => 2021-01-05

# => CURRENT_DATE is: 2021-01-05
echo 'CURRENT_DATE is: ' . CURRENT_DATE;
```
