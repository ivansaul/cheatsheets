# Flow Control

## if

```ruby
num = 2
puts 'two' if num == 2
```

If the condition is true, execute the code

## if elsif else

```ruby
temp = 19
if temp >= 25
  puts "hot"
elsif temp < 25 && temp >= 18
  puts "normal"
else
  puts "cold"
end
# output => normal
```

## unless

```ruby
# Unless contrary to if , evaluates when the statement is false
name = "rob"
# if name != "bob"
unless name == "bob"
  puts "hello stranger"
else
  puts "hello bob"
end
# output => hello stranger
num = 6
puts 'not two' unless num == 2
# output => not two
```

## case

```ruby
# case returns the value of the last expression executed
case input
# Check for an integer, 19
when 19
  puts "It's 19"
  # 检查一个确切的字符串，“Zaman”
when "Zaman"
  puts "Hi Zaman"
when 7..11
  puts "It's between 7 and 11"
  # Check multiple values, "coffee"
when "tea", "coffee"
  puts "Happy days"
end
```

## case( short syntax )

```ruby
case input
  when 19 then puts "It's 19"
end
```

## case( Optional failure )

```ruby
case input
  when 19 then puts "It's 19"
else
  puts "It's not 19"
end
```

## case( Get return value )

```ruby
marks = 86
result = case marks
        when 0..49 then "Fail"
        when 50..64 then "Pass"
        when 65..74 then "Credit"
        when 75..84 then "Distinction"
        when 85..100 then "High Distinction"
        else "Invalid marks"
        end

puts result
# High Distinction
```
