# Operators

## Usage

| Shortcut | Description  |
| -------- | :----------- |
| `d`      | <yel>w</yel> |
| Operator | Motion       |

Combine [operators](#available-operators) with [motions](#motions) to use them

## Available Operators

| Shortcut | Description                     |
| -------- | :------------------------------ |
| `d`      | Delete                          |
| `y`      | Yank _(copy)_                   |
| `c`      | Change _(delete then insert)_   |
| `p`      | Paste                           |
| `=`      | Formats code                    |
| `g~`     | Toggle case                     |
| `gU`     | Uppercase                       |
| `gu`     | Lowercase                       |
| `>`      | Indent right                    |
| `<`      | Indent left                     |
| `!`      | Filter through external program |

## Examples

| Combination          | Description                           |
| -------------------- | :------------------------------------ |
| `d`<yel>d</yel>      | Delete current line                   |
| `d`<yel>j</yel>      | Delete two lines                      |
| `d`<yel>w</yel>      | Delete to next word                   |
| `d`<yel>b</yel>      | Delete to beginning of word           |
| `d`<yel>fa</yel>     | Delete until `a` char                 |
| `d`<yel>/hello</yel> | Delete until `hello`                  |
| `c`<yel>c</yel>      | Change current line, synonym with `S` |
| `y`<yel>y</yel>      | Copy current line                     |
| `>`<yel>j</yel>      | Indent 2 lines                        |
| gg`d`<yel>G</yel>    | Delete a complete document            |
| gg`=`<yel>G</yel>    | Indent a complete document            |
| gg`y`<yel>G</yel>    | Copy a whole document                 |

## Counts

```console
[count] <operator> <motion>
<operator> [count] <motion>
```

---

| Combination      | Description                |
| ---------------- | :------------------------- |
| 2`d`<yel>d</yel> | Delete `2` lines           |
| 6`y`<yel>y</yel> | Copy `6` lines             |
| `d`3<yel>w</yel> | Delete `3` words           |
| `d`5<yel>j</yel> | Delete `5` lines downwards |
| `>`4<yel>k</yel> | Indent `4` lines upwards   |
