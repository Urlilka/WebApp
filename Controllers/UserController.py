from Models.Users import *
from bcrypt import hashpw, gensalt, checkpw


class UserController:
    #CRUD
    # У пользователя должны быть методы Аунтификация Регисртация (Пароль должен быть захеширован)
    # метод регистрации
    @classmethod
    def registration(cls,username,login,password,role):
        hash_password = hashpw(password.encode('utf-8'),gensalt())
        Users.create(username = username,login=login,password=hash_password,role=role)

    #метод проверки логина и пароля - аунтификация
    @classmethod
    def auth(cls,login,password):
        #проверить логин
        if Users.get_or_none(Users.login == login) != None:
            hspassword = Users.get_or_none(Users.login == login).password

            # if Users.get_or_none(Users.login == login).password == password:
            if checkpw(password.encode('utf-8'),hspassword.encode('utf-8')):
                return True
        return False

    #вывода записей из таблицы
    @classmethod
    def get(cls):
        return Users.select().order_by(Users.login.asc())

    #Удалить
    @classmethod
    def delete(cls,*id):
        for user in id:
            Users.delete_by_id(user)
    #Обнавить
    @classmethod
    def update(cls,id,**filds):

        for key, value in filds.items():
            if key == 'password':
                value = hashpw(value.encode('utf-8'), gensalt())

            Users.update({key:value}).where(Users.id == id).execute()

    # Пользователя по логину
    @classmethod
    def show_login(cls,login):
        return Users.get_or_none(Users.login == login)

    @classmethod
    def show(cls,id):
        return Users.get_or_none(id)


if __name__ == "__main__":
    # UserController.registration('dontdelete','manager','manager','Manager')
    for row in UserController.get():
        print(row.id,row.login, row.password)
    # print(UserController.auth('admin1','admin1'))
    # UserController.delete(16,7,8,9)
    # UserController.update(4,password='user1')
    # print('#############################################')
    # for row in UserController.get():
    #     print(row.id,row.login, row.password)