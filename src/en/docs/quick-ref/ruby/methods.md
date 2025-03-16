# Methods

## Declare a method

```ruby
def method_name(parameter1, parameter2)
    puts "#{parameter1} #{parameter2}"
    parameter1 + parameter2
end
```

---

```ruby
res = method_name(20, 10)
# output => 30
def method_name(parameter1, parameter2)
    puts "#{parameter1} #{parameter2}"
    return parameter1 + parameter2
end
# output => 30
```

## Call method

```ruby
res = method_name(parameter1, parameter2)
# Methods can be called without parentheses
res = method_name parameter1, parameter2
```

## Class method

Class methods are class-level methods. There are multiple ways to define class methods

```ruby
class Mobile
    def self.ring
        "ring ring ring..."
    end
end

Mobile.ring
```

---

```ruby
class Mobile
    def Mobile.ring
        "ring ring ring..."
    end
end
Mobile.ring
```

---

```ruby
class Mobile
    class << self
    def ring
        "ring ring ring..."
       end
    end
end
Mobile.ring
```

Class methods are instance methods of class objects. When a new class is created, an object of type "Class" is
initialized and assigned to a global constant (in this case Mobile)

```ruby
Mobile = Class.new do
    def self.ring
        "ring ring ring..."
    end
end
Mobile.ring
```

```ruby
Mobile = Class.new
class << Mobile
    def ring
        "ring ring ring..."
    end
end
Mobile.ring
```

## Use another parameter as default value

```ruby
def method_name(num1, num2 = num1)
    return num1 + num2
end
res = method_name(10)
# output => 20
```

## Define default values for method parameters

```ruby
def method_name(parameter1, parameter2, type = "ADD")
    puts "#{parameter1} #{parameter2}"
    return parameter1 + parameter2 if type == "ADD"
    return parameter1 - parameter2 if type == "SUB"
end
res = method_name(20, 10)
# output => 30
```

## Pass variable length arguments to method parameters

```ruby
def method_name(type, *values)
    return values.reduce(:+) if type == "ADD"
    return values.reduce(:-) if type == "SUB"
end
numbers = [2, 2, 2, 3, 3, 3]
res = method_name("ADD", *numbers)
# output => 15
res = method_name("SUB", *numbers)
# output => -11
# Or you can provide a value like this
res = method_name("ADD", 2, 2, 2, 3, 3, 3)
# output => 15
```

## Modify object

```ruby
a = ["Drama", "Mystery", "Crime",
"Sci-fi", "Disaster", "Thriller"]
a.sort
puts a
# We did not modify the object
# Drama
# Mystery
# Crime
# Sci-fi
# Disaster
# Thriller
a.sort!
puts a
# Modify object
# Crime
# Disaster
# Drama
# Mystery
# Sci-fi
# Thriller
```

When you want to modify the object, use `!` after the method

## Boolean method

In ruby, methods ending with a question mark (?) are called boolean methods, which return `true` or `false`

```ruby
"some text".nil?
# false
nil.nil?
# true
```

You can have your own boolean method

```ruby
def is_vowel?(char)
    ['a','e','i','o','u'].include? char
end
is_vowel? 'a'
# true
is_vowel? 'b'
# false
```
