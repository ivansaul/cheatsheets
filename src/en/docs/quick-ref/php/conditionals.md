# Conditionals

## If elseif else

```php
$a = 10;
$b = 20;

if ($a > $b) {
    echo "a is bigger than b";
} elseif ($a == $b) {
    echo "a is equal to b";
} else {
    echo "a is smaller than b";
}
```

## Switch

```php
$x = 0;
switch ($x) {
    case '0':
        print "it's zero";
        break;
    case 'two':
    case 'three':
        // do something
        break;
    default:
        // do something
}
```

## Ternary operator

```php
# => Does
print (false ? 'Not' : 'Does');

$x = false;
# => Does
print($x ?: 'Does');

$a = null;
$b = 'Does print';
# => a is unset
echo $a ?? 'a is unset';
# => print
echo $b ?? 'b is unset';
```

## Match

```php
$statusCode = 500;
$message = match($statusCode) {
  200, 300 => null,
  400 => 'not found',
  500 => 'server error',
  default => 'known status code',
};
echo $message; # => server error
```

See: [Match](https://www.php.net/manual/en/control-structures.match.php)

## Match expressions

```php
$age = 23;

$result = match (true) {
    $age >= 65 => 'senior',
    $age >= 25 => 'adult',
    $age >= 18 => 'young adult',
    default => 'kid',
};

echo $result; # => young adult
```
