# alembic_tutorial
Talk at Galvanize, 2020/01/16

* (edit the environment.yml file)
* conda env update


### Alembic tutorial -
https://alembic.sqlalchemy.org/en/latest/tutorial.html

* alembic init tutorial
  Creating directory /home/sanhita/workspace/projects/alembic_tutorial/tutorial ...  done
  Creating directory /home/sanhita/workspace/projects/alembic_tutorial/tutorial/versions ...  done
  Generating /home/sanhita/workspace/projects/alembic_tutorial/alembic.ini ...  done
  Generating /home/sanhita/workspace/projects/alembic_tutorial/tutorial/env.py ...  done
  Generating /home/sanhita/workspace/projects/alembic_tutorial/tutorial/README ...  done
  Generating /home/sanhita/workspace/projects/alembic_tutorial/tutorial/script.py.mako ...  done
  Please edit configuration/connection/logging settings in '/home/sanhita/workspace/projects/alembic_tutorial/alembic.ini' before
  proceeding.

* Edit alembic.ini -
sqlalchemy.url = postgresql+psycopg2://postgres:letmein@localhost:5432/postgres

* alembic revision -m "create name table"
  Generating /home/sanhita/workspace/projects/alembic_tutorial/tutorial/versions/e5bf121019be_create_name_table.py ...  done

  This still doesn't do anything to the database

* alembic upgrade head
INFO  [alembic.runtime.migration] Context impl PostgresqlImpl.
INFO  [alembic.runtime.migration] Will assume transactional DDL.
INFO  [alembic.runtime.migration] Running upgrade  -> 42929998ff36, create name table

* Go to the database. Either use `psql` or your favorite tool. Some popular ones I know are -
  * pgAdmin
  * pgcli - command line based
  * datagrip

* `\dt`
              List of relations
 Schema |      Name       | Type  |  Owner   
--------+-----------------+-------+----------
 public | alembic_version | table | postgres
(1 row)

* ```
  SELECT *
  FROM tutorial.names
  ```
