# File Handling

## Read file

### Line by line

```python
with open("myfile.txt") as file:
    for line in file:
        print(line)
```

### With line number

```python
file = open('myfile.txt', 'r')
for i, line in enumerate(file, start=1):
    print("Number %s: %s" % (i, line))
```

## String

### Write a string

```python
contents = {"aa": 12, "bb": 21}
with open("myfile1.txt", "w+") as file:
    file.write(str(contents))
```

### Read a string

```python
with open('myfile1.txt', "r+") as file:
    contents = file.read()
print(contents)
```

## Object

### Write an object

```python
contents = {"aa": 12, "bb": 21}
with open("myfile2.txt", "w+") as file:
    file.write(json.dumps(contents))
```

### Read an object

```python
with open('myfile2.txt', "r+") as file:
    contents = json.load(file)
print(contents)
```

## Delete a File

```python
import os
os.remove("myfile.txt")
```

## Check and Delete

```python
import os
if os.path.exists("myfile.txt"):
    os.remove("myfile.txt")
else:
    print("The file does not exist")
```

## Delete Folder

```python
import os
os.rmdir("myfolder")
```
