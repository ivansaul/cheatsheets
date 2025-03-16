# Miscellaneous

## Backup

Use pg_dumpall to backup all databases

```bash
pg_dumpall -U postgres > all.sql
```

Use pg_dump to backup a database

```bash
pg_dump -d mydb -f mydb_backup.sql
```

| -    | -                                              |
| ---- | :--------------------------------------------- |
| `-a` | Dump only the data, not the schema             |
| `-s` | Dump only the schema, no data                  |
| `-c` | Drop database before recreating                |
| `-C` | Create database before restoring               |
| `-t` | Dump the named table(s) only                   |
| `-F` | Format (`c`: custom, `d`: directory, `t`: tar) |

Use `pg_dump -?` to get the full list of options

## Restore

Restore a database with psql

```bash
psql -U user mydb < mydb_backup.sql
```

Restore a database with pg_restore

```bash
pg_restore -d mydb mydb_backup.sql -c
```

| -    | -                                                                            |
| ---- | :--------------------------------------------------------------------------- |
| `-U` | Specify a database user                                                      |
| `-c` | Drop database before recreating                                              |
| `-C` | Create database before restoring                                             |
| `-e` | Exit if an error has encountered                                             |
| `-F` | Format (`c`: custom, `d`: directory, `t`: tar, `p`: plain text sql(default)) |

Use `pg_restore -?` to get the full list of options

## Remote access

Get location of postgresql.conf

```bash
psql -U postgres -c 'SHOW config_file'
```

Append to postgresql.conf

```bash
listen_addresses = '*'
```

Append to pg_hba.conf (Same location as postgresql.conf)

```bash
host  all  all  0.0.0.0/0  md5
host  all  all  ::/0       md5
```

Restart PostgreSQL server

```bash
sudo systemctl restart postgresql
```

## Import/Export CSV

Export table into CSV file

```bash
\copy table TO '<path>' CSV
\copy table(col1,col1) TO '<path>' CSV
\copy (SELECT...) TO '<path>' CSV
```

Import CSV file into table

```bash
\copy table FROM '<path>' CSV
\copy table(col1,col1) FROM '<path>' CSV
```

See also: [Copy](https://www.postgresql.org/docs/current/sql-copy.html)
