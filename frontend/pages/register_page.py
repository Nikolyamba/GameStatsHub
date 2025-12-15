from nicegui import ui

from frontend.submits.post_sumbits import register_submit

@ui.page('/register')
def show_register_page():
    with ui.card():
        login = ui.input(placeholder="Введите Login", label="Логин")
        email = ui.input(placeholder="Введите Email", label="Email")
        password = ui.input(placeholder="Введите пароль", password=True,
                            password_toggle_button=True, label="123QWE",
                            validation=lambda value: 'Пароль должен состоять из 8 или больше знаков' if len(value) < 8 else None)
        repeat_password = ui.input(placeholder="Повторите введённый пароль", password=True,
                            password_toggle_button=True, label="123QWE",
                                   validation=lambda v: 'Пароли не совпадают' if v != password.value else None)

        ui.button('Зарегистрироваться', on_click=lambda: ui.run_async(register_submit(url='http://127.0.0.1:8000/api/register', data={login: login.value,
                                                                 email: email.value,
                                                                 password: password.value,
                                                                 repeat_password: repeat_password.value})))




