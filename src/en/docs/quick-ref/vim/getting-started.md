# Getting Started

## Motion Diagrams

```bash
▼/▶ Cursor   ▽/▷ Target
```

### Left-right motions

```bash
┌───────────── |
├───────────── 0      $ ──────────────┐
│  ┌────────── ^      fe ────────┐    │
│  │  ┌─────── Fo     te ───────┐│    │
│  │  │┌────── To     30| ───┐  ││    │
│  │  ││ ┌──── ge     w ───┐ │  ││    │
│  │  ││ │ ┌── b      e ─┐ │ │  ││    │
│  │  ││ │ │  ┌h      l┐ │ │ │  ││    │
▽  ▽  ▽▽ ▽ ▽  ▽▼      ▼▽ ▽ ▽ ▽  ▽▽    ▽
   echo "A cheatsheet from quickref.me"
```

### Up-down motions

```bash
                 - SCREEN 1 START
   ┌─┬─────────▷ #!/usr/bin/python
   │ │     ┌───▷
   │ │     │     print("Hello")
   │ │     { } ▶ print("Vim")
   │ │       │   print("!")
   │ │       └─▷
   │ │ ┌───┬───▷ print("Welcome")
G gg H M L k j ▶ print("to")
│        │   └─▷ print("cheatsheets.zip")
│        │       print("/vim")
│        │
│        └─────▷
│                - SCREEN 1 END
└──────────────▷ print("SCREEN 2")
```

## Motions

| Shortcut                       | Description       |
| ------------------------------ | :---------------- |
| `h` _\|_ `j` _\|_ `k` _\|_ `l` | Arrow keys        |
| `<C-u>` _/_ `<C-d>`            | Half-page up/down |
| `<C-b>` _/_ `<C-f>`            | Page up/down      |

### Words

| Shortcut     | Description               |
| ------------ | :------------------------ |
| `b` _/_ `w`  | Previous/Next word        |
| `ge` _/_ `e` | Previous/Next end of word |

### Line

| Shortcut             | Description                 |
| -------------------- | :-------------------------- |
| `0` _(zero)_ _/_ `$` | Start/End of line           |
| `^`                  | Start of line _(non-blank)_ |

### Character

| Shortcut                            | Description                         |
| ----------------------------------- | :---------------------------------- |
| `Fe` _/_ `fe`                       | Move to previous/next `e`           |
| `To` _/_ `to`                       | Move before/after previous/next `o` |
| <code>\|</code>_/_ <code>n\|</code> | Go to first/`n`th column            |

### Document

| Shortcut       | Description              |
| -------------- | :----------------------- |
| `gg` _/_ `G`   | First/Last line          |
| `:n` _\|_ `nG` | Go to line `n`           |
| `}` _/_ `{`    | Next/Previous empty line |

### Window

| Shortcut               | Description                 |
| ---------------------- | :-------------------------- |
| `H` _/_ `M` _/_ `L`    | Top/Middle/Bottom screen    |
| `zt` _/_ `zz` _/_ `zb` | Top/Center/Bottom this line |

## Insert Mode

| Shortcut               | Description                   |
| ---------------------- | :---------------------------- |
| `i` _/_ `a`            | Insert before/after cursor    |
| `I` _/_ `A`            | Insert start/end of line      |
| `o` _/_ `O` _(letter)_ | Insert new line below/above   |
| `s` _/_ `S`            | Delete char/line and insert   |
| `C` _/_ `cc`           | Change to end of/current line |
| `gi`                   | Insert at last insert point   |
| `Esc` _\|_ `<C-[>`     | Exit insert mode              |

## Saving and Exiting

| Shortcut                  | Description             |
| ------------------------- | :---------------------- |
| `:w`                      | Save                    |
| `:q`                      | Close file              |
| `:wq` _\|_ `:x` _\|_ `ZZ` | Save and quit           |
| `:wqa`                    | Save and quit all files |
| `:q!` _\|_ `ZQ`           | Force quit              |
| `:qa`                     | Close all files         |
| `:qa!`                    | Force quit all files    |
| `:w` now.txt              | Write to `now.txt`      |
| `:sav` new.txt            | Save and edit `new.txt` |
| `:w` !sudo tee %          | Write to readonly file  |

## Normal Mode

| Shortcut              | Description                  |
| --------------------- | :--------------------------- |
| `r`                   | Replace one character        |
| `R`                   | Enter Replace mode           |
| `u` _/_ `3u`          | Undo changes `1` / `3` times |
| `U`                   | Undo changes on one line     |
| `J`                   | Join with next line          |
| `<C-r>` _/_ 5 `<C-r>` | Redo changes `1` / `5` times |

## Cut and paste

| Shortcut         | Description                   |
| ---------------- | :---------------------------- |
| `x`              | Delete character _(Cut)_      |
| `p` _/_ `P`      | Paste after/before            |
| `xp`             | Swap two characters           |
| `D`              | Delete to end of line _(Cut)_ |
| `dw`             | Delete word _(Cut)_           |
| `dd`             | Delete line _(Cut)_           |
| `ddp`            | Swap two lines                |
| `yy`             | Yank line _(Copy)_            |
| `"*p` _\|_ `"+p` | Paste from system clipboard   |
| `"*y` _\|_ `"+y` | Paste to system clipboard     |

### In visual mode

| Shortcut     | Description              |
| ------------ | :----------------------- |
| `d` _\|_ `x` | Delete selection _(Cut)_ |
| `s`          | Replace selection        |
| `y`          | Yank selection _(Copy)_  |

## Repeating

| Shortcut | Description                                 |
| -------- | :------------------------------------------ |
| `.`      | Repeat last command                         |
| `;`      | Repeat latest `f`, `t`, `F` or `T`          |
| `,`      | Repeat latest `f`, `t`, `F` or `T` reversed |
| `&`      | Repeat last `:s`                            |
| `@:`     | Repeat a command-line command               |

## Visual mode

| Shortcut    | Description             |
| ----------- | :---------------------- |
| `v`         | Enter visual mode       |
| `V`         | Enter visual line mode  |
| `<C-v>`     | Enter visual block mode |
| `ggVG`      | Select all text         |
| `>` _/_ `<` | Shift text right/left   |

## Macros

| -     | -                     |
| ----- | :-------------------- |
| `qi`  | Record macro `i`      |
| `q`   | Stop recording macro  |
| `@i`  | Run macro `i`         |
| `7@i` | Run macro `i` 7 times |
| `@@`  | Repeat last macro     |

You can save macro for any letters not just `i`
