from sqlalchemy import create_engine

# Note: delChemy is a custom database name. I created a new database on pgAdmin
# called delChemy. Then added and ran the queries in delphi.sql. Then ran the
# queries in populate_table.sql. (by ran i mean I opened delphi.sql file with
# a text editor. copied all the queries, then ran them in the query editor of
# pgAdmin4.
db_url = f"postgresql+psycopg2://postgres:postoffice@localhost:5432/delChemy"

engine = create_engine(db_url, future=True)

connection = engine.connect()
print(connection)

