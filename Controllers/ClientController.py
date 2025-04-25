from Models.Clients import *

class ClientController():
    #CRUD

    # методы над атрибутами класса Clients

    @classmethod
    def add(cls,firstName,lastName,phoneNumber,email,address):
        Clients.create(firstName = firstName,lastName=lastName,
                       phoneNumber=phoneNumber,email=email,
                       address=address,status='Потенциальный')

#     метод вывода всех клиетнов
    @classmethod
    def get(cls):
        return Clients.select()

#     метод вывода одной записи по id клиента
    @classmethod
    def show(cls,id):
        # return Clients.get(Clients.id == id)
        # return Clients.get(id)
        return Clients.get_or_none(id)
        # return Clients.get_by_id(id)

#     Метод обновления записи
    @classmethod
    def update(cls, id, **filds):
        for key, value in filds.items():
            Clients.update({key:value}).where(Clients.id == id).execute()

    # метод удаления клиента
    @classmethod
    def delete(cls,id):
        Clients.delete().where(Clients.id == id).execute()

if __name__ == "__main__":
    # ClientController.add('Petr','Petrov','89080000000', 'ivan@iavn.iv','Salekhard')
    # ClientController.update(30, firstName = "firstname", lastName = "surname", phoneNumber = 8800553536, email = "mail", address = "address")
    for client in ClientController.get():
        print(client.id,client.firstName, client.lastName)
    # ClientController.delete(2)
    # print(ClientController.show(3).firstName)
