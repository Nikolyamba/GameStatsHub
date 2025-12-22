const form = document.getElementById('registerForm');
form.addEventListener('submit', function(event) {
    event.preventDefault();
});

const login = document.getElementById('login').value;
const email = document.getElementById('email').value;
const password = document.getElementById('password').value;
const repeatPassword = document.getElementById('repeat_password').value;

fetch('/api/register', {
    method: 'POST',
    headers: {
        'Content-Type': 'application/json'
    },
    body: JSON.stringify({
        login: login,
        email: email,
        password: password,
        repeat_password: repeatPassword
    })
})
.then(response => response.json())
.then(data => {
    if (data.success) {
        alert('Регистрация успешна!');
    } else {
        alert('Ошибка: ' + data.detail);
    }
})
.catch(error => console.error('Ошибка:', error));