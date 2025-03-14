# Operators

## Walrus

```python
values = [1, "text", True, "", 2]
i = 0

# It assigns a value to a variable and compares it in a boolean expression
while (data := values[i]):

    print(data, end=",")
    i = i + 1

# Expected result: 1, "text", True
```
