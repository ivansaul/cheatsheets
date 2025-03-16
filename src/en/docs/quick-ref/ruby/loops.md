# Loops

## while loop

```ruby
# variable count
count = 4
# using while loop
# here conditional is count i.e. 4
while count >= 1
  # statements to be executed
  puts "Ruby Cheatsheet"
  count = count - 1
  # while loop ends here
end
```

output

```
Ruby Cheatsheet
Ruby Cheatsheet
Ruby Cheatsheet
Ruby Cheatsheet
```

## for loop

```ruby
# loop using range as expression
text = "Ruby Cheatsheet"
# using for loop with the range
for count in 1..5 do
  puts text
end
```

output

```
Ruby Cheatsheet
Ruby Cheatsheet
Ruby Cheatsheet
Ruby Cheatsheet
Ruby Cheatsheet
```

## do..while loop

```ruby
# starting of do..while loop
loop do
  puts "Ruby Cheatsheet"
  val = '7'
  # using boolean expressions
  if val == '7'
    break
  end
  # ending of ruby do..while loop
end
```

output

```
Ruby Cheatsheet
```

## until loop

```ruby
var = 7
# here do is optional
until var == 11 do
  # code to be executed
  puts var * 10
  var = var + 1
  # here loop ends
end
```

output

```
70
80
90
100
```

## Break out of loop

```ruby
salary = [399, 234, 566, 533, 233]
salary.each do |s|
  break if s == 566
  puts s
end
# output
# 399
# 234
```

By using the `break` keyword

## skip within loop

```ruby
salary = [399, 234, 566, 533, 233]
salary.each do |s|
  next if s == 533
  puts s
end
# output
# 399
# 234
# 566
# 233
```

By using next keyword

## Repeat current iteration

```ruby
data = [456, 3000]
retry_count = 0
status = "network failure"
sum = 0
data.each do |d|
    if retry_count == 3
        status = "connection established"
        retry_count = 0
        redo
    elsif status == "network failure" and retry_count < 5
        puts "network failure #{retry_count}"
        retry_count += 1
        redo
    elsif status == "connection established"
        puts d
        sum += d
    end
end
# output of sum
# 3456
```

## Start the cycle again

```ruby
numbers = [2, 2, 44, 44]
sum = 0
begin
    numbers.each do |s|
        if rand(1..10) == 5
            puts "hi 5, let's do it again!"
            sum = 0
            raise "hi 5"
        end
        puts s
        sum += s
    end
rescue
    retry
end
```
