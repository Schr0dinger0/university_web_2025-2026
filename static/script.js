let compareList = [];

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

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    console.log('Страница загружена, карточек:', document.querySelectorAll('.phone-card').length);
});