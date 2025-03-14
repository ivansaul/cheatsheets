# Working with Multiple Files

## Buffers

| -          | -                                |
| ---------- | :------------------------------- |
| `:e file`  | Edit a file in a new buffer      |
| `:bn`      | Go to the next buffer            |
| `:bp`      | Go to the previous buffer        |
| `:bd`      | Remove file from buffer list     |
| `:b 5`     | Open buffer #5                   |
| `:b file`  | Go to a buffer by file           |
| `:ls`      | List all open buffers            |
| `:sp file` | Open and split window            |
| `:vs file` | Open and vertically split window |
| `:hid`     | Hide this buffer                 |
| `:wn`      | Write file and move to next      |
| `:tab ba`  | Edit all buffers as tabs         |

## Windows

| -                       | -                           |
| ----------------------- | :-------------------------- |
| `<C-w>` `s`             | Split window                |
| `<C-w>` `v`             | Split window vertically     |
| `<C-w>` `w`             | Switch windows              |
| `<C-w>` `q`             | Quit a window               |
| `<C-w>` `T`             | Break out into a new tab    |
| `<C-w>` `x`             | Swap current with next      |
| `<C-w>` `-` _/_ `+`     | Decrease/Increase height    |
| `<C-w>` `<` _/_ `>`     | Decrease/Increase width     |
| `<C-w>` <code>\|</code> | Max out the width           |
| `<C-w>` `_`      | Max out the height          |
| `<C-w>` `=`             | Equally high and wide       |
| `<C-w>` `h` _/_ `l`     | Go to the left/right window |
| `<C-w>` `j` _/_ `k`     | Go to the up/down window    |

## Tabs

| Shortcut       | Description                       |
| -------------- | :-------------------------------- |
| `:tabe [file]` | <yel>E</yel>dit file in a new tab |
| `:tabf [file]` | Open if exists in new tab         |
| `:tabc`        | <yel>C</yel>lose current tab      |
| `:tabo`        | Close <yel>o</yel>ther tabs       |
| `:tabs`        | List all <yel>tabs</yel>          |
| `:tabr`        | Go to fi<yel>r</yel>st tab        |
| `:tabl`        | Go to <yel>l</yel>ast tab         |
| `:tabm 0`      | <yel>M</yel>ove to position `0`   |
| `:tabn`        | Go to <yel>n</yel>ext tab         |
| `:tabp`        | Go to <yel>p</yel>revious tab     |

### Normal mode

| Shortcut | Description                   |
| -------- | :---------------------------- |
| `gt`     | Go to <yel>n</yel>ext tab     |
| `gT`     | Go to <yel>p</yel>revious tab |
| `2gt`    | Go to tab number `2`          |
