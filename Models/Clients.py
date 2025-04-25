from peewee import PrimaryKeyField, CharField, TextField
from Connection.Connect import connect
from Models.Base import Base

class Clients(Base):
    id = PrimaryKeyField()
    firstName = CharField(max_length=10)
    lastName = CharField(max_length=15)
    phoneNumber = CharField(max_length=11)
    email = CharField(max_length=100)
    address = TextField()
    status = CharField(max_length=14)

if __name__ == "__main__":
    connect().create_tables([Clients])