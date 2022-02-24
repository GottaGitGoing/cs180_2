# from sqlalchemy import create_engine
# from sqlalchemy import text
#
# # Note: delChemy is a custom database name. I created a new database on pgAdmin
# # called delChemy. Then added and ran the queries in delphi.sql. Then ran the
# # queries in populate_table.sql. (by ran i mean I opened delphi.sql file with
# # a text editor. copied all the queries, then ran them in the query editor of
# # pgAdmin4.
# db_url = f"postgresql+psycopg2://postgres:postoffice@localhost:5432/delChemy"
# engine = create_engine(db_url, future=True)
# connection = engine.connect()
#
# stmt = text("select * from delphi.customer")
# result = connection.execute(stmt)
#
# for i in result:
#     print(i)
# # for i,j,k,l in result:
# #     print(i,j,k,l)
# # print(result.first())


import sqlalchemy

# Note: delChemy is a custom database name. I created a new database on pgAdmin
# called delChemy. Then added and ran the queries in delphi.sql. Then ran the
# queries in populate_table.sql. (by ran i mean I opened delphi.sql file with
# a text editor. copied all the queries, then ran them in the query editor of
# pgAdmin4.
db_url = f"postgresql+psycopg2://postgres:postoffice@localhost:5432/delChemy"
engine = sqlalchemy.create_engine(db_url, future=True)
connection = engine.connect()

metadata = sqlalchemy.MetaData()
customer = sqlalchemy.Table('customer', metadata, autoload_with = engine,schema="delphi")

query = customer.select().where(customer.c.customer_id==5)

result = connection.execute(query)

for i in result:
    print(i)
# for i,j,k,l in result:
#     print(i,j,k,l)
# print(result.first())