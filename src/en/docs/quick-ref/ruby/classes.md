# Classes

## Classes Example

```ruby
class Person
    # when you create a new object, it looks for a method named initialize and executes it, like a constructor in java
    # def initialize(name, number)
    #    @name = name
    #    @number = number
    # end
    # instance variable
    # @name
    # class variable
    # @@count
    # attr_accessor acts as a getter and setter for the following instance attributes
    attr_accessor :name, :number
    # class variable must be initialized
    @@count = 0
    def self.count
        @@count
    end
    def self.count=(count)
        @@count = count
    end
    def initialize
        @@count += 1
    end
end
# create an instance of the Person class
p1 = Person.new
# set attributes of the Person class
p1.name = "Yukihiro Matsumoto"
p1.number = 9999999999
# get attributes of the Person class
puts "#{p1.name}"
puts "#{p1.number}"
puts "#{Person.count}"
# Yukihiro Matsumoto
# 9999999999
# 1
p2 = Person.new
p2.name = "Yukihiro Matsumoto"
p2.number = 9999999999
# get attributes of the Person class
puts "#{p2.name}"
puts "#{p2.number}"
puts "#{Person.count}"
# Yukihiro Matsumoto
# 9999999999
# 2
# set class variable
Person.count = 3
puts "#{Person.count}"
# 3
```

## Inherit a class

```ruby
class Person
    attr_accessor :name, :number
end
# Inherit methods and properties from parent class using < symbol
class Student < Person
    attr_accessor :id
end
s = Student.new
s.name = "James Bond"
s.number = 700
s.id = 678
puts "#{p.name}"
James Bond
puts "#{p.number}"
700
puts "#{p.id}"
678
```

## Check instance type

```ruby
class Vehicle; end
class Car < Vehicle; end
class Audi < Car; end
car = Car.new
car.instance_of? Vehicle
false
car.instance_of? Car
true
car.instance_of? Audi
false
a = 7
a.instance_of? Integer
true
a.instance_of? Numeric
false
```

Returns true if the object is an instance of the given class and not a subclass or superclass

## Print all method names of a class

```ruby
puts (String.methods).sort
# Exclude methods inherited from Object class
puts (String.methods - Object.public_instance_methods).sort
```

## Check if a class has a specific method

```ruby
String.respond_to?(:prepend)
true
String.respond_to?(:append)
false
```
