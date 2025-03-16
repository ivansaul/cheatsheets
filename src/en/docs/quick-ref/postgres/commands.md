# Commands

## Tables

| -                | -                               |
| ---------------- | :------------------------------ |
| `\d <table>`     | Describe table                  |
| `\d+ <table>`    | Describe table with details     |
| `\dt`            | List tables from current schema |
| `\dt *.*`        | List tables from all schemas    |
| `\dt <schema>.*` | List tables for a schema        |
| `\dp`            | List table access privileges    |
| `\det[+]`        | List foreign tables             |

## Query buffer

| -            | -                                  |
| ------------ | :--------------------------------- |
| `\e [FILE]`  | Edit the query buffer (or file)    |
| `\ef [FUNC]` | Edit function definition           |
| `\p`         | Show the contents                  |
| `\r`         | Reset (clear) the query buffer     |
| `\s [FILE]`  | Display history or save it to file |
| `\w FILE`    | Write query buffer to file         |

## Informational

| -               | -                               |
| --------------- | :------------------------------ |
| `\l[+]`         | List all databases              |
| `\dn[S+]`       | List schemas                    |
| `\di[S+]`       | List indexes                    |
| `\du[+]`        | List roles                      |
| `\ds[S+]`       | List sequences                  |
| `\df[antw][S+]` | List functions                  |
| `\deu[+]`       | List user mappings              |
| `\dv[S+]`       | List views                      |
| `\dl`           | List large objects              |
| `\dT[S+]`       | List data types                 |
| `\da[S]`        | List aggregates                 |
| `\db[+]`        | List tablespaces                |
| `\dc[S+]`       | List conversions                |
| `\dC[+]`        | List casts                      |
| `\ddp`          | List default privileges         |
| `\dd[S]`        | Show object descriptions        |
| `\dD[S+]`       | List domains                    |
| `\des[+]`       | List foreign servers            |
| `\dew[+]`       | List foreign-data wrappers      |
| `\dF[+]`        | List text search configurations |
| `\dFd[+]`       | List text search dictionaries   |
| `\dFp[+]`       | List text search parsers        |
| `\dFt[+]`       | List text search templates      |
| `\dL[S+]`       | List procedural languages       |
| `\do[S]`        | List operators                  |
| `\dO[S+]`       | List collations                 |
| `\drds`         | List per-database role settings |
| `\dx[+]`        | List extensions                 |

`S`: show system objects, `+`: additional detail

## Connection

| -                      | -                           |
| ---------------------- | :-------------------------- |
| `\c [DBNAME]`          | Connect to new database     |
| `\encoding [ENCODING]` | Show or set client encoding |
| `\password [USER]`     | Change the password         |
| `\conninfo`            | Display information         |

## Formatting

| -                         | -                                          |
| ------------------------- | :----------------------------------------- |
| `\a`                      | Toggle between unaligned and aligned       |
| `\C [STRING]`             | Set table title, or unset if none          |
| `\f [STRING]`             | Show or set field separator for unaligned  |
| `\H`                      | Toggle HTML output mode                    |
| <code>\t [on\|off]</code> | Show only rows                             |
| `\T [STRING]`             | Set or unset HTML \<table\> tag attributes |
| <code>\x [on\|off]</code> | Toggle expanded output                     |

## Input/Output

| -                 | -                                                              |
| ----------------- | :------------------------------------------------------------- |
| `\copy ...`       | Import/export table<br> _See also:_ [copy](#import-export-csv) |
| `\echo [STRING]`  | Print string                                                   |
| `\i FILE`         | Execute file                                                   |
| `\o [FILE]`       | Export all results to file                                     |
| `\qecho [STRING]` | String to output stream                                        |

## Variables

| -                     | -                                             |
| --------------------- | :-------------------------------------------- |
| `\prompt [TEXT] NAME` | Set variable                                  |
| `\set [NAME [VALUE]]` | Set variable _(or list all if no parameters)_ |
| `\unset NAME`         | Delete variable                               |

## Misc

| -                              | -                    |
| ------------------------------ | :------------------- |
| `\cd [DIR]`                    | Change the directory |
| <code>\timing [on\|off]</code> | Toggle timing        |
| `\! [COMMAND]`                 | Execute in shell     |
| `\! ls -l`                     | List all in shell    |

## Large Objects

- `\lo_export LOBOID FILE`
- `\lo_import FILE [COMMENT]`
- `\lo_list`
- `\lo_unlink LOBOID`
