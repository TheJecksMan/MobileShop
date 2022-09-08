# MobileShop
Back-end для мобильной версии сайта

Запуск и установка:
1. Склонировать репозиторий `git clone`
2. Перейти в папку
3. Создать виртуальное окружение `python -m venv .venv`
4. Войти в виртуальное окружение
5. Установить зависимости `pip intsall  --no-cache-dir  -r requirements.txt`
6. Перейти в папку с **main.py** `cd app/`
7. Выполнить для локального запуска `uvicorn main:app --workers 3`
8. Или выполнить для локального запуска `uvicorn main:app --workers 3 --host 0.0.0.0 --port 80`
9. Запуск!

### Linux
Для функционнирования нового драйвера требуется зависимости

Выполните `sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`
## ROADMAP

### **back-end**
### Категории

- [x] Получение списка всех доступных категорий
- [x] Получение подкатегории по id категории
- [x] Поиск категории по названию 
- [x] Получение товаров категории

### Товары

- [x] Получение описание товара
- [x] Получение базовой информации
- [x] Получение базовой информации о нескольких товарах
- [x] Поиск по названию товара (Поиск в конкретной категории)
- [x] Получение списка популярных (самых просматриваемых товаров)
- [x] Получение списка доступных комплектаций

### Фильтры
- [x] Доступная комплектация к товару
- [x] Получение параметров для фильтрации

### Почтовый клиент 
- [x] Почтовый клиент
- [ ] Настройка почтового клиента для финальной версии (В процессе)
- [x] Отправка почты (Данные заказа, обращение клиента) на конкретную почту(ы) с клиентского приложения 


### **front-end**
### Главная страница
- [x] Отображение логотипа компании
- [x] Отображение списка популярных и последних просмотренных товаров
- [x] Поиск товара по названию
- [x] Выезжающее меню с дополнительными страницами (О нас, избранное и т.д.)

### Страница товаров
- [x] Отображение списка категорий товаров
- [x] Отображение товаров в зависимости от категории
- [x] Интерфейс для перехода к странице "Избранных" товаров
- [x] Сортировка списка товаров по некоторому набору критериев (Название, цена и пр)

### Страница корзины
- [x] Отображение добавленных в корзину товаров
- [x] Отображение суммарной цены всех товаров, а также выбор количества той или иной единицы товара
- [x] Интерфейс для перехода на страницу "Истории заказов"

### Страница контактов
- [x] Отображение всех доступных способов связи с компанией (все элементы интерфейса кликабельны)
- [x] Форма обратной связи, где пользователь может связаться с компанией

### НЕ основные страницы
- [x] Страница "О нас" (Общая информация о компании)
- [x] Страница "Наши магазины" (Список всех магазинов во всех городах с возможностью просмотра на карте или выбора по конкретному городу)
- [x] Страница "Найти ближайший магазин" (Система автоматически определяет ближайший к клиенту магазин на основе данных с его GPS датчика)
- [x] Страница "Доставка и оплата" (Общая информация о доставке и оплате заказов)
- [x] Страница "Гарантии" (Общая информация о гарантии на продаваемые товары)
- [x] Страница "Избранное" (Список всех товаров, которые пользователь пометил избранными)
- [x] Страница "Результаты поиска" (Если пользователь не нашел в первых 5 предложенных товаров в поиске, нужный для себя, на этой странице он может посмотреть все результаты, удоволетворяющие поисковому запросу)
- [x] Страница "Описание товара" (Вся информация по конкретному товару. Тут же можно добавить товар в корзину и выбрать комплектацию)
- [x] Страницы "Оформить заказ" и "Подтвердите данные" (Страницы с формой отправки заказа и подтверждения введенных клиентом данных)
- [x] Страницы "История заказов" и "Детали заказа" (Основная информация об ранее сделанных заказах в общем виде и по конкретному заказу)

