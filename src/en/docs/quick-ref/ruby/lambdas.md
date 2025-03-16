# Lambdas

## Declare a lambda

```ruby
l = lambda { puts "Hello World" }
# shorthand
l = -> { puts "Hello World" }
# transfer lambda
l.call
# output => Hello World
```

There are multiple ways to call a lambda

```ruby
l.()
l[]
```

## strict arguments

```ruby
l = -> (count) { "Hello World " * count }
l.call 5
# output
# "Hello World Hello World Hello World Hello World Hello World "
l.call 5, 2
# output
wrong number of arguments (given 2, expected 1)
```

## declare a lambda in block

```ruby
def give_me_data
    puts "I am inside give_me_data method"
    l = -> { return 10 }
    l.call
    puts "I am back in give_me_data method"
end

return_value = give_me_data
puts return_value

# output
# I am inside give_me_data method
# I am back in give_me_data method
# nil # because puts return nil
```

## lambdas are returned from the lambda itself, just like regular methods

```ruby
l = -> { return 10 }
l.call

# output => 10
```
