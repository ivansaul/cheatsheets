# Text Objects

## Usage

<!-- Confusing and should be fixed -->

| Shortcut |              Description               | -            |
| -------- | :------------------------------------: | :----------- |
| `v`      |     <pur>i</pur> _/_ <pur>a</pur>      | <yel>p</yel> |
| Operator | <pur>i</pur>nner _/_ <pur>a</pur>round | Text object  |

Operate with an [operator](#available-operators) inner or around text blocks

## Text objects

| Shortcut                                             | Description                            |
| ---------------------------------------------------- | :------------------------------------- |
| <yel>p</yel>                                         | Paragraph                              |
| <yel>w</yel>                                         | Word                                   |
| <yel>W</yel>                                         | WORD <br/>_(surrounded by whitespace)_ |
| <yel>s</yel>                                         | Sentence                               |
| <yel>[</yel> <yel>(</yel> <yel>{</yel> <yel>\<</yel> | A [], (), or {} block                  |
| <yel>]</yel> <yel>)</yel> <yel>}</yel> <yel>\></yel> | A [], (), or {} block                  |
| <yel>'</yel> <yel>"</yel> <yel>\`</yel>              | A quoted string                        |
| <yel>b</yel>                                         | A block [(                             |
| <yel>B</yel>                                         | A block in [{                          |
| <yel>t</yel>                                         | A HTML tag block                       |

See `:help text-objects`

## Delete

| Shortcut                    | Description                           |
| --------------------------- | :------------------------------------ |
| `d`<pur>i</pur><yel>w</yel> | Delete inner word                     |
| `d`<pur>i</pur><yel>s</yel> | Delete inner sentence                 |
| `d`<pur>i</pur><yel>"</yel> | Delete in quotes                      |
| `d`<pur>a</pur><yel>"</yel> | Delete in quotes _(including quotes)_ |
| `d`<pur>i</pur><yel>p</yel> | Delete a paragraph                    |

## Selections

| Shortcut                                            | Description                               |
| --------------------------------------------------- | :---------------------------------------- |
| `v`<pur>i</pur><yel>"</yel>                         | Select inner quotes "`...`{.underline}"   |
| `v`<pur>a</pur><yel>"</yel>                         | Select quotes `"..."`{.underline}         |
| `v`<pur>i</pur><yel>[</yel>                         | Select inner brackets [`...`{.underline}] |
| `v`<pur>a</pur><yel>[</yel>                         | Select brackets `[...]`{.underline}       |
| `v`<pur>i</pur><yel>w</yel>                         | Select inner word                         |
| `v`<pur>i</pur><yel>p</yel>                         | Select inner paragraph                    |
| `v`<pur>i</pur><yel>p</yel><pur>i</pur><yel>p</yel> | Select more paragraph                     |

## Misc

| Shortcut                    | Description                          |
| --------------------------- | :----------------------------------- |
| `c`<pur>i</pur><yel>w</yel> | Change inner word                    |
| `c`<pur>i</pur><yel>"</yel> | Change inner quotes                  |
| `c`<pur>i</pur><yel>t</yel> | Change inner tags (HTML)             |
| `c`<pur>i</pur><yel>p</yel> | Change inner paragraph               |
| `y`<pur>i</pur><yel>p</yel> | Yank inner paragraph                 |
| `y`<pur>a</pur><yel>p</yel> | Yank paragraph _(including newline)_ |
