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

Выполнить для локального запуска `uvicorn main:app --workers 3 --host 0.0.0.0 --port 80`
8. Запуск!

### Linux
Для функционнирования нового драйвера требуется зависимости

Выполните `sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`
## ROADMAP

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

### Фильтры
- [ ] Фильтр по доступным параметрам товаров
