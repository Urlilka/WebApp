from peewee import *

# функция подключения к базе данных

def connect():
    mysql_db = MySQLDatabase('rybin_clients21',
                             user='rybin_rybin',
                             password='111111',
                             host='10.11.13.118',
                             port=3306)
    return mysql_db

if __name__ == "__main__":
    try:
        connect().connect()
    except:
        print('error')