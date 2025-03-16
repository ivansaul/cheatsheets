# Boolean Enumerable Method

## boolean enumerable method

| Name       | When to use                                                              |
| :--------- | :----------------------------------------------------------------------- |
| `all?`     | When you want to check if all elements meet your condition               |
| `any?`     | When you want to check if at least one item meets your condition         |
| `one?`     | When you want to check if one element meets your requirement             |
| `none?`    | When you want to check if no item meets your condition, the opposite of? |
| `empty?`   | When you want to check if an object is empty                             |
| `include?` | When you want to check if an element exists in the object                |

## all?

```ruby
[2, 4, 6, 8, 10].all? { |num| num % 2 == 0 }
# true
[1, 4, 6, 8, 10].all? { |num| num % 2 == 0 }
# false
```

## any?

```ruby
[1, 3, 5, 7, 10].any? { |num| num % 2 == 0 }
# true
[1, 3, 5, 7, 19].any? { |num| num % 2 == 0 }
# false
```

## one?

```ruby
[1, 3, 2, 5, 7].one? { |num| num % 2 == 0 }
# true
[1, 3, 2, 5, 4].one? { |num| num % 2 == 0 }
# false
```

## none?

```ruby
[1, 3, 5, 7, 9].none? { |num| num % 2 == 0 }
# true
[2, 3, 5, 7, 9].none? { |num| num % 2 == 0 }
# false
```

## empty?

```ruby
[].empty?
# true
[1, 3, 5, 7, 9].empty?
# false
```
