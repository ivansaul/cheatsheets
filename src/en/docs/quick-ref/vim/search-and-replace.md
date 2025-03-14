# Search And Replace

## Search

| -        | -                                   |
| -------- | :---------------------------------- |
| `/foo`   | Search forward                      |
| `/foo\c` | Search forward _(case insensitive)_ |
| `?foo`   | Search backward                     |
| `/\v\d+` | Search with [regex](/regex)         |
| `n`      | Next matching search pattern        |
| `N`      | Previous match                      |
| `*`      | Search for current word forward     |
| `#`      | Search for current word backward    |

## Replace LINE

```vim
:[range]s/{pattern}/{str}/[flags]
```

---

|                   |                                  |
| ----------------- | :------------------------------- |
| `:s/old/new`      | Replace first                    |
| `:s/old/new/g`    | Replace all                      |
| `:s/\vold/new/g`  | Replace all with [regex](/regex) |
| `:s/old/new/gc`   | replace all _(Confirm)_          |
| `:s/old/new/i`    | Ignore case replace first        |
| `:2,6s/old/new/g` | Replace between lines `2`-`6`    |

## Replace FILE

```vim
:%s/{pattern}/{str}/[flags]
```

---

|                   |                                  |
| ----------------- | :------------------------------- |
| `:%s/old/new`     | Replace first                    |
| `:%s/old/new/g`   | Replace all                      |
| `:%s/old/new/gc`  | Replace all _(Confirm)_          |
| `:%s/old/new/gi`  | Replace all _(ignore case)_      |
| `:%s/\vold/new/g` | Replace all with [regex](/regex) |

## Ranges

| -       | -                 |
| ------- | :---------------- |
| `%`     | Entire file       |
| `’<,’>` | Current selection |
| `5`     | Line `5`          |
| `5,10`  | Lines `5` to `10` |
| `$`     | Last line         |
| `2,$`   | Lines `2` to Last |
| `.`     | Current line      |
| `,3`    | Next `3` lines    |
| `-3,`   | Forward `3` lines |

## Global command

```vim
:[range]g/{pattern}/[command]
```

---

|              |                                    |
| ------------ | :--------------------------------- |
| `:g/foo/d`   | Delete lines containing `foo`      |
| `:g!/foo/d`  | Delete lines not containing `foo`  |
| `:g/^\s*$/d` | Delete all blank lines             |
| `:g/foo/t$`  | Copy lines containing `foo` to EOF |
| `:g/foo/m$`  | Move lines containing `foo` to EOF |
| `:g/^/m0`    | Reverse a file                     |
| `:g/^/t.`    | Duplicate every line               |

## Inverse :g

```vim
:[range]v/{pattern}/[command]
```

---

|            |                                                            |
| ---------- | :--------------------------------------------------------- |
| `:v/foo/d` | Delete lines not containing `foo`<br/>_(also `:g!/foo/d`)_ |

## Flags

| -   | -                         |
| --- | :------------------------ |
| `g` | Replace all occurrences   |
| `i` | Ignore case               |
| `I` | Don't ignore case         |
| `c` | Confirm each substitution |

## Substitute expression (magic)

| -             | -                                |
| ------------- | :------------------------------- |
| `&` _\|_ `\0` | Replace with the whole matched   |
| `\1`...`\9`   | Replace with the group 0-9       |
| `\u`          | Uppercase next letter            |
| `\U`          | Uppercase following characters   |
| `\l`          | Lowercase next letter            |
| `\L`          | Lowercase following characters   |
| `\e`          | End of `\u`, `\U`, `\l` and `\L` |
| `\E`          | End of `\u`, `\U`, `\l` and `\L` |

## Examples

```c
:s/a\|b/xxx\0xxx/g           # Modifies "a b"      to "xxxaxxx xxxbxxx"
:s/test/\U& file/                # Modifies "test"     to "TEST FILE"
:s/\(test\)/\U\1\e file/         # Modifies "test"     to "TEST file"
:s/\v([abc])([efg])/\2\1/g      # Modifies "af fa bg" to "fa fa gb"
:s/\v\w+/\u\0/g               # Modifies "bla bla"  to "Bla Bla"
:s/\v([ab])|([cd])/\1x/g         # Modifies "a b c d"  to "ax bx x x"
:%s/.*/\L&/                      # Modifies "HTML"     to "html"
:s/\v<(.)(\w*)/\u\1\L\2/g        # Make every first letter of a word uppercase
:%s/^\(.*\)\n\1/\1/              # Remove duplicate lines
:%s/<\/\=\(\w\+\)\>/\U&/g        # Convert HTML-Tags to uppercase
:g/^pattern/s/$/mytext           # Find and append text to the end
:g/pattern/norm! @i              # Run a macro on matching lines
/^\(.*\)\(\r\?\n\1\)\+$          # View the duplicates lines
/\v^(.*)(\r?\n\1)+$              # View the duplicates lines (very magic)
:v/./,/./-j                      # Compress blank lines into a blank line
:g/<p1>/,/<p2>/d                 # Delete inclusively from <p1> to <p2>
```
