from Models.Interactions import *

class InteractionController:
    #CRUD
    #Создание записи
    @classmethod
    def add(cls, client_id,date,type,result):
        Interactions.create(client_id=client_id,date=date,type=type,result=result)

    # Метод вывод всех записей
    @classmethod
    def get(cls):
        return Interactions.select()

    # Метод вывода одной записи
    @classmethod
    def show(cls,id):
        return Interactions.get_or_none(id)
    # обновление записи
    @classmethod
    def update(cls,id,**filds):
        for key, value in filds.items():
            Interactions.update({key:value}).where(Interactions.id == id).execute()
    #метод удаления
    @classmethod
    def delete(cls,id):
        # Interactions.delete().where(Interactions.id == id).execute()
        Interactions.delete_by_id(id)

if __name__ == "__main__":
    # InteractionController.add(1,'2025-01-16','Звонок','Никакой')
    for row in InteractionController.get():
        print(row.type)

        