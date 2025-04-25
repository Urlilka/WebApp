from crypt import methods

from flask import Flask, render_template, request, url_for
from werkzeug.utils import redirect
from flask_login import LoginManager, login_user, login_required, current_user, logout_user

from Controllers.ClientController import ClientController
from Controllers.UserController import UserController


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)
app.secret_key = "Very Secret Key"


@login_manager.user_loader
def load_user(user_id):
    # Объект пользователь
    return UserController.show(int(user_id))


# маршрут Корень сайта (Главная страница)
# Работа с данными post и get
@app.route("/", methods = ['POST','GET'])
def login():
    title = "Вход"
    # Переменной login передаётся строка из формы
    login = request.form.get('login')
    # Переменной password передаётся строка из формы
    password = request.form.get('password')
    # Проверка метода
    if request.method == "POST":
        if UserController.auth(login, password):
            user = UserController.show_login(login)
            login_user(user)
            if current_user.role == "Administrator":
                return redirect("/admin")
            else:
                return redirect("/manager")
        else:
            print('вы не вошли')
    return render_template("login.html",title=title)


# Маршрут для админ панели
@app.route("/admin", methods=['POST','GET'])
@login_required
def admin():
    title = "Панель администратора"
    if current_user.role == "Administrator":
        users = UserController.get() # Передача списка пользователей
        if request.method == "POST":
            username = request.form.get("username")
            role = request.form.get("role")
            login = request.form.get("login")
            password = request.form.get("password")

            UserController.registration(
                username=username,
                login=login,
                password=password,
                role=role
            )
            return redirect("/admin")
        return render_template(
            "admin.html",
            title=title,
            users = users
        )
    else:
        return redirect("/logout")

# маршрут обновления пользователя (админ панель)
@app.route("/admin/update/<int:id>", methods=['POST','GET'])
@login_required
def update_user(id):
    if current_user.role == "Administrator":
        title = "Изменить пользователя"
        user = UserController.show(id)
        if request.method == "POST":
            username = request.form.get("username")
            role = request.form.get("role")
            UserController.update(
                id,
                username=username,
                role=role
            )
            return redirect(url_for("admin"))
        return render_template(
            "edit_user.html",
            title = title,
            user = user
        )
    else:
        return redirect("/")

# Маршрут удаления пользователя (Админ панель)
@app.route("/admin/delete/<int:id>")
@login_required
def delete_user(id):
    if current_user.role == "Administrator":
        UserController.delete(id)
        return redirect(url_for("admin"))
    else:
        return redirect(url_for("logout"))



# Маршрут для панели менеджера
@app.route("/manager", methods=['POST','GET'])
@login_required
def manager():
    title = "Панель администратора"
    if current_user.role == "Manager":
        clients = ClientController.get()
        if request.method == "POST":
            firstname = request.form.get("firstname")
            surname = request.form.get("lastname")
            number = request.form.get("number")
            mail = request.form.get("mail")
            address = request.form.get("address")

            ClientController.add(
                firstName = firstname,
                lastName = surname,
                phoneNumber = number,
                email = mail,
                address = address
            )
            return redirect("/manager")
        return render_template(
            "manager.html",
            title = title,
            clients = clients
        )
    else:
        return redirect("/logout")

# Маршрут для обновления клиента (панель менеджера)
@app.route("/manager/update/<int:id>", methods=['POST','GET'])
@login_required
def update_client(id):
    if current_user.role == "Manager":
        title = "Изменить клиента"
        client = ClientController.show(id)
        if request.method == "POST":
            firstname = request.form.get("firstname")
            surname = request.form.get("lastname")
            number = request.form.get("number")
            mail = request.form.get("mail")
            address = request.form.get("address")

            ClientController.update(
                id,
                firstName = firstname,
                lastName = surname,
                phoneNumber = number,
                email = mail,
                address = address
            )

            return redirect(url_for("manager"))
        return render_template(
            "edit_client.html",
            title = title,
            client = client
        )
    else:
        return redirect("/")

# Маршрут удаления клиента (Панель менеджера)
@app.route("/manager/delete/<int:id>")
@login_required
def delete_client(id):
    if current_user.role == "Manager":
        ClientController.delete(id)
        return redirect(url_for("manager"))
    else:
        return redirect(url_for("logout"))

# Метод выхода
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

# Перенаправление неавторизованных в корень
@login_manager.unauthorized_handler
def unauthorized():
    if not current_user.is_authenticated:
        return redirect("/")

if __name__ == "__main__":
    # Запуск переменной app вместе с веб-сервером
    app.run(debug=True)