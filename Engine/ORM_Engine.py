import sqlalchemy

db_url = f"postgresql+psycopg2://postgres:postoffice@localhost:5432/delChemy"
engine = sqlalchemy.create_engine(db_url, future=True)
connection = engine.connect()

metadata = sqlalchemy.MetaData()


# customer = sqlalchemy.Table('customer', metadata, autoload_with = connection,
#                             schema="delphi")

#query = customer.select().where(customer.c.customer_id==5)
# query = customer.select()
# result = connection.execute(query)

# for i in result:
#     print(i)


# Doing it class-less for now
def get_customer(id: int):
    customer = sqlalchemy.Table('customer', metadata, autoload_with=connection,
                                schema="delphi")
    query = customer.select().where(customer.c.customer_id==id)
    result = connection.execute(query)
    return result

cus = get_customer(3)
# for i in cus.mappings():
#     print(i)
# a = cus.mappings().columns('opt_in')



def get_menu_item():
    pass


def get_nut_fact(id: int):
    pass


def get_order(id: int):
    pass


def get_order_history(id: int):
    pass


