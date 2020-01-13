# alembic_tutorial
Talk at Galvanize, 2020/01/16

https://docs.google.com/presentation/d/13X8ji8LfLHLB1_b3-ZLT_V4eUmJOPzNIuPSTFxHkZbU/edit?usp=sharing

* (edit the environment.yml file)
* conda env update


### Alembic tutorial -
https://alembic.sqlalchemy.org/en/latest/tutorial.html

* alembic init tutorial
.

.

.

  Please edit configuration/connection/logging settings in '/home/sanhita/workspace/projects/alembic_tutorial/alembic.ini' before
  proceeding.

* Edit alembic.ini -

sqlalchemy.url = postgresql+psycopg2://postgres:letmein@localhost:5432/postgres

* alembic revision -m "create name table"

...  done

  This still doesn't do anything to the database

* alembic upgrade head

.

.

INFO  [alembic.runtime.migration] Running upgrade  -> 42929998ff36, create name table

* Go to the database. Either use `psql` or your favorite tool. Some popular ones I know are -
  * pgAdmin
  * pgcli - command line based
  * datagrip

* `\dt`

              List of relations
| Schema |      Name       | Type  |  Owner   |
|--------+-----------------+-------+----------|
| public | alembic_version | table | postgres|
(1 row)

* ```
  SELECT *
  FROM tutorial.names
  ```
