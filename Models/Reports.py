from Models.Base import *

class Reports(Base):
    id = PrimaryKeyField()
    generatedDate = DateField()
    data = CharField()