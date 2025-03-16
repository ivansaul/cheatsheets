# Getting Started

## Getting started

Switch and connect

```bash
sudo -u postgres psql
```

List all databases

```bash
postgres=# \l
```

Connect to the database named postgres

```bash
postgres=# \c postgres
```

Disconnect

```bash
postgres=# \q
postgres=# \!
```

## psql commands

| Option              | Example                                      | Description                    |
| ------------------- | -------------------------------------------- | :----------------------------- |
| `[-d] <database>`   | psql -d mydb                                 | Connecting to database         |
| `-U`                | psql -U john mydb                            | Connecting as a specific user  |
| `-h` `-p`           | psql -h localhost -p 5432 mydb               | Connecting to a host/port      |
| `-U` `-h` `-p` `-d` | psql -U admin -h 192.168.1.5 -p 2506 -d mydb | Connect remote PostgreSQL      |
| `-W`                | psql -W mydb                                 | Force password                 |
| `-c`                | psql -c '\c postgres' -c '\dt'               | Execute a SQL query or command |
| `-H`                | psql -c "\l+" -H postgres > database.html    | Generate HTML report           |
| `-l`                | psql -l                                      | List all databases             |
| `-f`                | psql mydb -f file.sql                        | Execute commands from a file   |
| `-V`                | psql -V                                      | Print the psql version         |

## Getting help

| -           | -                              |
| ----------- | :----------------------------- |
| `\h`        | Help on syntax of SQL commands |
| `\h` DELETE | DELETE SQL statement syntax    |
| `\?`        | List of PostgreSQL command     |

Run in PostgreSQL console
