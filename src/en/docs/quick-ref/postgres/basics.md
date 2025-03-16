# Basics

## Recon

Show version

```console
SHOW SERVER_VERSION;
```

Show system status

```sql
\conninfo
```

Show environmental variables

```sql
SHOW ALL;
```

List users

```sql
SELECT rolname FROM pg_roles;
```

Show current user

```sql
SELECT current_user;
```

Show current user's permissions

```console
\du
```

Show current database

```sql
SELECT current_database();
```

Show all tables in database

```sql
\dt
```

List functions

```sql
\df <schema>
```

## Databases

List databases

```sql
\l
```

Connect to database

```sql
\c <database_name>
```

Show current database

```sql
SELECT current_database();
```

[Create database](http://www.postgresql.org/docs/current/static/sql-createdatabase.html)

```sql
CREATE DATABASE <database_name> WITH OWNER <username>;
```

[Drop database](http://www.postgresql.org/docs/current/static/sql-dropdatabase.html)

```sql
DROP DATABASE IF EXISTS <database_name>;
```

[Rename database](http://www.postgresql.org/docs/current/static/sql-alterdatabase.html)

```sql
ALTER DATABASE <old_name> RENAME TO <new_name>;
```

## Tables

List tables, in current db

```sql
\dt

SELECT table_schema,table_name FROM information_schema.tables ORDER BY table_schema,table_name;
```

List tables, globally

```sql
\dt *.*.

SELECT * FROM pg_catalog.pg_tables
```

List table schema

```sql
\d <table_name>
\d+ <table_name>

SELECT column_name, data_type, character_maximum_length
FROM INFORMATION_SCHEMA.COLUMNS
WHERE table_name = '<table_name>';
```

[Create table](http://www.postgresql.org/docs/current/static/sql-createtable.html)

```sql
CREATE TABLE <table_name>(
  <column_name> <column_type>,
  <column_name> <column_type>
);
```

Create table, with an auto-incrementing primary key

```sql
CREATE TABLE <table_name> (
  <column_name> SERIAL PRIMARY KEY
);
```

[Delete table](http://www.postgresql.org/docs/current/static/sql-droptable.html)

```sql
DROP TABLE IF EXISTS <table_name> CASCADE;
```

## Permissions

Become the postgres user, if you have permission errors

```shell
sudo su - postgres
psql
```

[Grant](http://www.postgresql.org/docs/current/static/sql-grant.html) all permissions on database

```sql
GRANT ALL PRIVILEGES ON DATABASE <db_name> TO <user_name>;
```

Grant connection permissions on database

```sql
GRANT CONNECT ON DATABASE <db_name> TO <user_name>;
```

Grant permissions on schema

```sql
GRANT USAGE ON SCHEMA public TO <user_name>;
```

Grant permissions to functions

```sql
GRANT EXECUTE ON ALL FUNCTIONS IN SCHEMA public TO <user_name>;
```

Grant permissions to select, update, insert, delete, on a all tables

```sql
GRANT SELECT, UPDATE, INSERT ON ALL TABLES IN SCHEMA public TO <user_name>;
```

Grant permissions, on a table

```sql
GRANT SELECT, UPDATE, INSERT ON <table_name> TO <user_name>;
```

Grant permissions, to select, on a table

```sql
GRANT SELECT ON ALL TABLES IN SCHEMA public TO <user_name>;
```

## Columns

[Add column](http://www.postgresql.org/docs/current/static/sql-altertable.html)

```sql
ALTER TABLE <table_name> IF EXISTS
ADD <column_name> <data_type> [<constraints>];
```

Update column

```sql
ALTER TABLE <table_name> IF EXISTS
ALTER <column_name> TYPE <data_type> [<constraints>];
```

Delete column

```sql
ALTER TABLE <table_name> IF EXISTS
DROP <column_name>;
```

Update column to be an auto-incrementing primary key

```sql
ALTER TABLE <table_name>
ADD COLUMN <column_name> SERIAL PRIMARY KEY;
```

Insert into a table, with an auto-incrementing primary key

```sql
INSERT INTO <table_name>
VALUES (DEFAULT, <value1>);


INSERT INTO <table_name> (<column1_name>,<column2_name>)
VALUES ( <value1>,<value2> );
```

## Data

[Select](http://www.postgresql.org/docs/current/static/sql-select.html) all data

```sql
SELECT * FROM <table_name>;
```

Read one row of data

```sql
SELECT * FROM <table_name> LIMIT 1;
```

Search for data

```sql
SELECT * FROM <table_name> WHERE <column_name> = <value>;
```

[Insert](http://www.postgresql.org/docs/current/static/sql-insert.html) data

```sql
INSERT INTO <table_name> VALUES( <value_1>, <value_2> );
```

[Update](http://www.postgresql.org/docs/current/static/sql-update.html) data

```sql
UPDATE <table_name>
SET <column_1> = <value_1>, <column_2> = <value_2>
WHERE <column_1> = <value>;
```

[Delete](http://www.postgresql.org/docs/current/static/sql-delete.html) all data

```sql
DELETE FROM <table_name>;
```

Delete specific data

```sql
DELETE FROM <table_name>
WHERE <column_name> = <value>;
```

## Users

List roles

```sql
SELECT rolname FROM pg_roles;
```

[Create user](http://www.postgresql.org/docs/current/static/sql-createuser.html)

```sql
CREATE USER <user_name> WITH PASSWORD '<password>';
```

[Drop user](http://www.postgresql.org/docs/current/static/sql-dropuser.html)

```sql
DROP USER IF EXISTS <user_name>;
```

[Alter](http://www.postgresql.org/docs/current/static/sql-alterrole.html) user password

```sql
ALTER ROLE <user_name> WITH PASSWORD '<password>';
```

## Schema

List schemas

```sql
\dn

SELECT schema_name FROM information_schema.schemata;

SELECT nspname FROM pg_catalog.pg_namespace;
```

[Create schema](http://www.postgresql.org/docs/current/static/sql-createschema.html)

```sql
CREATE SCHEMA IF NOT EXISTS <schema_name>;
```

[Drop schema](http://www.postgresql.org/docs/current/static/sql-dropschema.html)

```sql
DROP SCHEMA IF EXISTS <schema_name> CASCADE;
```

## Dates

Show [current date](https://www.postgresql.org/docs/15/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT) YYYY-MM-DD

```sql
SELECT current_date;
```

Calculate
[age](<https://www.postgresql.org/docs/15/functions-datetime.html#:~:text=age%20(%20timestamp%2C%20timestamp%20)%20%E2%86%92%20interval>)
between two dates

```sql
SELECT age(timestamp, timestamp);
```

Show [current time](https://www.postgresql.org/docs/15/functions-datetime.html#FUNCTIONS-DATETIME-CURRENT) with time
zone

```sql
SELECT current_time;
```

[Make](<https://www.postgresql.org/docs/15/functions-datetime.html#:~:text=make_date%20(%20year%20int%2C%20month%20int%2C%20day%20int%20)%20%E2%86%92%20date>)
dates using integers

```sql
SELECT make_date(2021,03,25);
```
