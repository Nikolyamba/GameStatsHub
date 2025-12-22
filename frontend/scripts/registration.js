const form = document.getElementById('registerForm');

// 2️⃣ Ловим событие отправки формы
form.addEventListener('submit', async function(event) {
    event.preventDefault(); // ❌ отменяем стандартную отправку браузера

    // 3️⃣ Получаем значения полей
    const login = document.getElementById('login').value;
    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;
    const repeatPassword = document.getElementById('repeat-password').value;

    // 4️⃣ Создаём объект для отправки на бэкенд
    const data = {
        login: login,
        email: email,
        password: password,
        repeat_password: repeatPassword
    };

    try {
        // 5️⃣ Отправляем POST-запрос на сервер
        const response = await fetch('/register', {
            method: 'POST',               // используем POST
            headers: { 'Content-Type': 'application/json' }, // отправка JSON
            body: JSON.stringify(data)     // превращаем объект JS в JSON
        });

        // 6️⃣ Ждём ответ и преобразуем его в объект
        const result = await response.json();

        // 7️⃣ Проверяем, успешна ли регистрация
        if (response.ok) {
            alert('Регистрация успешна! ID: ' + result.user);
            // можно редирект на другую страницу
            window.location.href = '/login';
        } else {
            alert('Ошибка: ' + result.detail);
        }

    } catch (error) {
        // 8️⃣ Если сеть упала или сервер не ответил
        console.error('Ошибка запроса:', error);
        alert('Произошла ошибка при регистрации');
    }
});