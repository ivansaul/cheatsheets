# Miscellaneous

## Case

| Shortcut       | Description             |
| -------------- | :---------------------- |
| `vU`           | _Uppercase_ character   |
| `vu`           | _Lowercase_ character   |
| `~`            | _Toggle case_ character |
| `viw` `U`      | _Uppercase_ word        |
| `viw` `u`      | _Lowercase_ word        |
| `viw` `~`      | _Toggle case_ word      |
| `VU` _/_ `gUU` | _Uppercase_ line        |
| `Vu` _/_ `guu` | _Lowercase_ line        |
| `V~` _/_ `g~~` | _Toggle case_ line      |
| `gggUG`        | _Uppercase_ all text    |
| `ggguG`        | _Lowercase_ all text    |
| `ggg~G`        | _Toggle case_ all text  |

## Jumping

| Shortcut | Description              |
| -------- | :----------------------- |
| `<C-o>`  | Go back to previous      |
| `<C-i>`  | Go forward               |
| `gf`     | Go to file in cursor     |
| `ga`     | Display hex, ascii value |

## Misc command-lines

| -              | -                                          |
| -------------- | :----------------------------------------- |
| `:h`           | Help open help view                        |
| `:edit!`       | Reload current file                        |
| `:2,8m0`       | Move lines `2`-`8` to `0`                  |
| `:noh`         | Clear search highlights                    |
| `:sort`        | Sort lines                                 |
| `:ter`         | Open a terminal window                     |
| `:set paste`   | Enable Insert Paste sub-mode               |
| `:set nopaste` | disable Insert Paste sub-mode              |
| `:cq`          | Exiting with an error<br/>_(aborting Git)_ |

## Navigating

| Shortcut       | Description               |
| -------------- | :------------------------ |
| `%`            | Nearest/matching `{[()]}` |
| `[(` _\|_ `[{` | Previous `(` or `{`       |
| `])` _\|_ `]{` | Next `)` or `}`           |
| `[m`           | Previous method start     |
| `[M`           | Previous method end       |

## Counters

| Shortcut | Description     |
| -------- | :-------------- |
| `<C-a>`  | Increase number |
| `<C-x>`  | Decrease number |

## Tags

| Shortcut             | Description                                     |
| -------------------- | :---------------------------------------------- |
| `:tag Classname`     | Jump to first definition of Classname           |
| `<C-]>`              | Jump to definition                              |
| `g]`                 | See all definitions                             |
| `<C-t>`              | Go back to last tag                             |
| `<C-o> <C-i>`        | Back/forward                                    |
| `:tselect Classname` | Find definitions of Classname                   |
| `:tjump Classname`   | Find definitions of Classname (auto-select 1st) |

## Formatting

| -       | -                                |
| ------- | -------------------------------- |
| `:ce 8` | Center lines between `8` columns |
| `:ri 4` | Right-align lines at `4` columns |
| `:le`   | Left-align lines                 |

See `:help formatting`

## Marks

| Shortcut            | Description                                          |
| ------------------- | :--------------------------------------------------- |
| <code>\`^</code>    | Last position of cursor in insert mode               |
| <code>\`.</code>    | Last change in current buffer                        |
| <code>\`"</code>    | Last exited current buffer                           |
| <code>\`0</code>    | In last file edited                                  |
| <code>''</code>     | Back to line in current buffer where jumped from     |
| <code>\`\`</code>   | Back to position in current buffer where jumped from |
| <code>\`[</code>    | To beginning of previously changed or yanked text    |
| <code>\`]</code>    | To end of previously changed or yanked text          |
| <code>\`&lt;</code> | To beginning of last visual selection                |
| <code>\`&gt;</code> | To end of last visual selection                      |
| `ma`                | Mark this cursor position as `a`                     |
| <code>\`a</code>    | Jump to the cursor position `a`                      |
| `'a`                | Jump to the beginning of the line with position `a`  |
| <code>d'a</code>    | Delete from current line to line of mark `a`         |
| <code>d\`a</code>   | Delete from current position to position of mark `a` |
| <code>c'a</code>    | Change text from current line to line of `a`         |
| <code>y\`a</code>   | Yank text from current position to position of `a`   |
| `:marks`            | List all current marks                               |
| `:delm a`           | Delete mark `a`                                      |
| `:delm a-d`         | Delete marks `a`, `b`, `c`, `d`                      |
| `:delm abc`         | Delete marks `a`, `b`, `c`                           |

## Calculator

| Shortcut         | Description      |
| ---------------- | :--------------- |
| `<C-r>` `=` 7\*7 | Shows the result |
| `<C-r>` `=` 10/2 | Shows the result |

Do this in INSERT mode

## Shell

| -            | -                              |
| ------------ | :----------------------------- |
| `:!<shell>`  | Interpret Shell Command        |
| `:r!<shell>` | Read in output of shell        |
| `:r!date`    | Insert date                    |
| `:!!date`    | Replace current line with date |

## Command line

| Shortcut     | Description                               |
| ------------ | :---------------------------------------- |
| `<C-r><C-w>` | Insert current word into the command line |
| `<C-r>"`     | Paste from " register                     |
| `<C-x><C-f>` | Auto-completion of path in insert mode    |

## Tricks

Remove duplicate lines

```bash
:sort | %!uniq -u
```

To number the lines in the file

```bash
:%!cat -n
```

Copy whole doc to clipboard

```bash
:%w !pbcopy            # Mac OS X
:%w !xclip -i -sel c   # GNU/Linux
:%w !xsel -i -b        # GNU/Linux
```
