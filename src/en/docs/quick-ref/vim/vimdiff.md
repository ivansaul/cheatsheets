# Vimdiff

## Usage

```bash

vimdiff file1 file2 [file3]
vim -d file1 file2 [file3]
```

## Editing

```console
:[range]diffget [bufspec]
:[range]diffput [bufspec]
```

---

| Shortcut            | Description             |
| ------------------- | :---------------------- |
| `do` _/_ `:diffget` | Obtain (get) difference |
| `dp` _/_ `:diffput` | Put difference          |
| `:dif`              | Re-scan differences     |
| `:diffo`            | Switch off diff mode    |
| `:1,$+1diffget`     | Get all differences     |
| `ZQ`                | Quit without changes    |

## Folds

| Shortcut      | Description                  |
| ------------- | :--------------------------- |
| `zo` _/_ `zO` | Open                         |
| `zc` _/_ `zC` | Close                        |
| `za` _/_ `zA` | Toggle                       |
| `zv`          | Open folds for this line     |
| `zM`          | Close all                    |
| `zR`          | Open all                     |
| `zm`          | Fold more _(foldlevel += 1)_ |
| `zr`          | Fold less _(foldlevel -= 1)_ |
| `zx`          | Update folds                 |

## Jumping

| Shortcut | Description         |
| -------- | :------------------ |
| `]c`     | Next difference     |
| `[c`     | Previous difference |
