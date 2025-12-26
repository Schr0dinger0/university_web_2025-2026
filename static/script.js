let compareList = [];
let currentUser = null;

// Переключение видимости фильтров
function toggleFilters() {
    const sidebar = document.getElementById('filtersSidebar');
    const toggleBtn = document.querySelector('.filter-toggle');

    sidebar.classList.toggle('active');

    if (sidebar.classList.contains('active')) {
        toggleBtn.textContent = '◀';
        toggleBtn.style.left = '360px';
    } else {
        toggleBtn.textContent = '▶';
        toggleBtn.style.left = '0';
    }
}

// Основная функция фильтрации
function filterPhones() {
    const searchName = document.getElementById('searchName').value.toLowerCase();
    const filterBrand = document.getElementById('filterBrand').value;
    const filterOS = document.getElementById('filterOS').value;
    const filterYear = document.getElementById('filterYear').value;
    const priceMin = parseInt(document.getElementById('priceMin').value) || 0;
    const priceMax = parseInt(document.getElementById('priceMax').value) || 200000;
    const screenMin = parseFloat(document.getElementById('screenMin').value) || 0;
    const screenMax = parseFloat(document.getElementById('screenMax').value) || 10;

    const phoneCards = document.querySelectorAll('.phone-card');
    let visibleCount = 0;

    phoneCards.forEach(card => {
        const name = card.getAttribute('data-name');
        const brand = card.getAttribute('data-brand');
        const os = card.getAttribute('data-os');
        const shell = card.getAttribute('data-shell');
        const year = card.getAttribute('data-year');
        const price = parseInt(card.getAttribute('data-price'));
        const screen = parseFloat(card.getAttribute('data-screen'));

        // Проверяем все условия фильтрации
        const nameMatch = !searchName || name.includes(searchName);
        const brandMatch = !filterBrand || brand === filterBrand;
        const osMatch = !filterOS || os.includes(filterOS);
        const yearMatch = !filterYear || year === filterYear;
        const priceMatch = (!priceMin || price >= priceMin) && (!priceMax || price <= priceMax);
        const screenMatch = (!screenMin || screen >= screenMin) && (!screenMax || screen <= screenMax);

        if (nameMatch && brandMatch && osMatch && yearMatch && priceMatch && screenMatch) {
            card.style.display = 'block';
            visibleCount++;
        } else {
            card.style.display = 'none';
        }
    });

    console.log(`Отображено карточек: ${visibleCount}`);
}

// Сброс всех фильтров
function resetFilters() {
    document.getElementById('searchName').value = '';
    document.getElementById('filterBrand').value = '';
    document.getElementById('filterOS').value = '';
    document.getElementById('filterYear').value = '';
    document.getElementById('priceMin').value = '';
    document.getElementById('priceMax').value = '';
    document.getElementById('screenMin').value = '';
    document.getElementById('screenMax').value = '';

    // Показываем все карточки
    const phoneCards = document.querySelectorAll('.phone-card');
    phoneCards.forEach(card => {
        card.style.display = 'block';
    });
}

// Функции для сравнения
function addToCompare(phoneId) {
    if (!compareList.includes(phoneId)) {
        compareList.push(phoneId);
        alert(`Смартфон добавлен в сравнение! Всего для сравнения: ${compareList.length}`);

        if (compareList.length >= 2) {
            showCompareButton();
        }
    } else {
        alert('Этот смартфон уже добавлен для сравнения');
    }
}

function showCompareButton() {
    console.log('Можно сравнивать! ID смартфонов:', compareList);
}

// Функции для работы с модальным окном авторизации
function showAuthModal() {
    document.getElementById('authModal').style.display = 'flex';
    showLoginForm();
}

function hideAuthModal() {
    document.getElementById('authModal').style.display = 'none';
    clearAuthForms();
}

function showLoginForm() {
    document.getElementById('loginForm').style.display = 'block';
    document.getElementById('registerForm').style.display = 'none';
}

function showRegisterForm() {
    document.getElementById('loginForm').style.display = 'none';
    document.getElementById('registerForm').style.display = 'block';
}

function clearAuthForms() {
    document.getElementById('loginUsername').value = '';
    document.getElementById('loginPassword').value = '';
    document.getElementById('registerUsername').value = '';
    document.getElementById('registerPassword').value = '';
    document.getElementById('registerName').value = '';
}

// Функция входа
async function login(username, password) {
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);

    try {
        const response = await fetch('/check-login', {
            method: 'POST',
            body: formData
        });
        const result = await response.json();

        if (result.success) {
            currentUser = {
                username: result.username,
                name: result.name
            };
            updateUserUI();
            hideAuthModal();
            alert(`Добро пожаловать, ${result.name}!`);
            return true;
        } else {
            alert(result.message || 'Неверный логин или пароль');
            return false;
        }
    } catch (error) {
        console.error('Ошибка входа:', error);
        alert('Ошибка сервера при входе');
        return false;
    }
}

// Функция регистрации
async function register(username, password, name) {
    const formData = new FormData();
    formData.append('username', username);
    formData.append('password', password);
    formData.append('name', name);

    try {
        const response = await fetch('/save-user', {
            method: 'POST',
            body: formData
        });
        const result = await response.json();

        if (result.success) {
            alert('Регистрация успешна! Теперь войдите в аккаунт.');
            showLoginForm();
            return true;
        } else {
            alert(result.message || 'Ошибка при регистрации');
            return false;
        }
    } catch (error) {
        console.error('Ошибка регистрации:', error);
        alert('Ошибка сервера при регистрации');
        return false;
    }
}

// Обновление UI после входа/выхода
function updateUserUI() {
    if (currentUser) {
        document.getElementById('loginBtn').style.display = 'none';
        document.getElementById('userGreeting').style.display = 'block';
        document.getElementById('userNameDisplay').textContent = currentUser.name;
    } else {
        document.getElementById('loginBtn').style.display = 'block';
        document.getElementById('userGreeting').style.display = 'none';
    }
}

// Функция выхода
async function logout() {
    try {
        const response = await fetch('/logout');
        const result = await response.json();

        if (result.success) {
            currentUser = null;
            updateUserUI();
            alert('Вы вышли из аккаунта');
        }
    } catch (error) {
        console.error('Ошибка выхода:', error);
        currentUser = null;
        updateUserUI();
        alert('Вы вышли из аккаунта');
    }
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    console.log('Страница загружена, карточек:', document.querySelectorAll('.phone-card').length);

    // Назначаем обработчики событий
    document.getElementById('loginBtn').addEventListener('click', showAuthModal);
    document.querySelector('.close-modal').addEventListener('click', hideAuthModal);

    // Клик вне модального окна закрывает его
    document.getElementById('authModal').addEventListener('click', function(e) {
        if (e.target === this) hideAuthModal();
    });

    // Переключение между формами - ИСПРАВЛЕНО!
    document.getElementById('switchToRegister').addEventListener('click', function(e) {
        e.preventDefault();
        showRegisterForm();
    });

    document.getElementById('switchToLogin').addEventListener('click', function(e) {
        e.preventDefault();
        showLoginForm();
    });

    // Вход - ИСПРАВЛЕНО!
    document.getElementById('submitLogin').addEventListener('click', async function(e) {
        e.preventDefault();
        const username = document.getElementById('loginUsername').value;
        const password = document.getElementById('loginPassword').value;

        if (username && password) {
            await login(username, password);
        } else {
            alert('Заполните все поля');
        }
    });

    // Регистрация - ИСПРАВЛЕНО!
    document.getElementById('submitRegister').addEventListener('click', async function(e) {
        e.preventDefault();
        const username = document.getElementById('registerUsername').value;
        const password = document.getElementById('registerPassword').value;
        const name = document.getElementById('registerName').value;

        if (username && password && name) {
            await register(username, password, name);
        } else {
            alert('Заполните все поля');
        }
    });

    // Выход
    document.getElementById('logoutBtn').addEventListener('click', function(e) {
        e.preventDefault();
        logout();
    });

    // Проверяем, есть ли сохраненный пользователь в localStorage
    const savedUser = localStorage.getItem('currentUser');
    if (savedUser) {
        currentUser = JSON.parse(savedUser);
        updateUserUI();
    }
});