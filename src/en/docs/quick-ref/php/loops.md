# Loops

## while

```php
$i = 1;
# => 12345
while ($i <= 5) {
    echo $i++;
}
```

## do while

```php
$i = 1;
# => 12345
do {
    echo $i++;
} while ($i <= 5);
```

## for i

```php
# => 12345
for ($i = 1; $i <= 5; $i++) {
    echo $i;
}
```

## break

```php
# => 123
for ($i = 1; $i <= 5; $i++) {
    if ($i === 4) {
        break;
    }
    echo $i;
}
```

## continue

```php
# => 1235
for ($i = 1; $i <= 5; $i++) {
    if ($i === 4) {
        continue;
    }
    echo $i;
}
```

## foreach

```php
$a = ['foo' => 1, 'bar' => 2];
# => 12
foreach ($a as $k) {
    echo $k;
}
```
