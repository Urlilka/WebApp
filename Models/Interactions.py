from Models.Base import *
from Models.Clients import Clients


class Interactions(Base):
    id = PrimaryKeyField()
    client_id = ForeignKeyField(Clients)
    date = DateField()
    type = CharField(15)
    result = TextField()

if __name__ == "__main__":
    connect().create_tables([Interactions])