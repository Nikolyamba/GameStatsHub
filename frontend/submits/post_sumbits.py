import httpx
from nicegui import ui

async def register_submit(url: str, data: dict) -> dict:
    async with httpx.AsyncClient() as client:
        if data.password.validation:
            ui.notify('Введённый пароль меньше 8 символов')
        if data.password_repeat.validation:
            ui.notify('Введённые пароли не совпадают')

        response = await client.post(url, json=data)
        if response.status_code == 200:
            ui.notify('Регистрация прошла успешно', color='green')
        else:
            detail = response.json().get('detail', 'Ошибка регистрации')
            ui.notify(detail, color='red')

        return response.json()