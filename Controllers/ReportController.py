from dataclasses import dataclass

from Models.Clients import Clients
from Models.Reports import *
import datetime
class ReportController:
    # Вывод отчётов
    @classmethod
    def get(cls):
        return Reports.select()

    @classmethod
    def show(cls,id):
        return Reports.get_or_none(id)

    #Обновить
    @classmethod
    def update(cls,id,**filds):
        for key, value in filds.items():
            Reports.update({key:value}).where(Reports.id == id).execute()
    #Удалить
    @classmethod
    def delete(cls,*id):
        for report in id:
            Reports.delete_by_id(report)

    # Отчёт - количество клиентов
    @classmethod
    def count_clients(cls):
        # дата добавляется автоматически (текущая дата)
        generatedDate = datetime.datetime.now()
        # Количество клиентов берём из модели Clients
        count = Clients.select().count()
        Reports.create(generatedDate=generatedDate, data = count)

if __name__ == "__main__":
    for row in ReportController.get():
        print(row.generatedDate,row.data)
    ReportController.count_clients()
    print('#############################')
    for row in ReportController.get():
        print(row.generatedDate,row.data)