# Classes

## Constructor

```php
class Student {
    public function __construct($name) {
        $this->name = $name;
    }
   public function print() {
        echo "Name: " . $this->name;
    }
}
$alex = new Student("Alex");
$alex->print();    # => Name: Alex
```

## Inheritance

```php
class ExtendClass extends SimpleClass
{
    // Redefine the parent method
    function displayVar()
    {
        echo "Extending class\n";
        parent::displayVar();
    }
}

$extended = new ExtendClass();
$extended->displayVar();
```

## Classes variables

```php
class MyClass
{
    const MY_CONST       = 'value';
    static $staticVar    = 'static';

    // Visibility
    public static $var1  = 'pubs';

    // Class only
    private static $var2 = 'pris';

    // The class and subclasses
    protected static $var3 = 'pros';

    // The class and subclasses
    protected $var6      = 'pro';

    // The class only
    private $var7        = 'pri';
}
```

Access statically

```php
echo MyClass::MY_CONST;   # => value
echo MyClass::$staticVar; # => static
```

## Magic Methods

```php
class MyClass
{
    // Object is treated as a String
    public function __toString()
    {
        return $property;
    }
    // opposite to __construct()
    public function __destruct()
    {
        print "Destroying";
    }
}
```

## Interface

```php
interface Foo
{
    public function doSomething();
}
interface Bar
{
    public function doSomethingElse();
}
class Cls implements Foo, Bar
{
    public function doSomething() {}
    public function doSomethingElse() {}
}
```
