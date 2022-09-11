# MobileShop
Back-end для мобильной версии сайта

Запуск и установка:
### Debug
**windows**
1. Склонировать репозиторий `git clone <repository>`
2. Перейти в папку с репозиторием
3. Создать виртуальное окружение `python -m venv .venv` (Необязательно)
4. Войти в виртуальное окружение
5. Установить зависимости `pip intsall  --no-cache-dir  -r requirements.txt`
6. Перейти в папку с **main.py** `cd app/`
7. Выполнить для локального запуска `uvicorn main:app`
8. Или выполнить для локального запуска `uvicorn main:app --reload`
9. Запуск!

### Release (Установка на сервер)
**Linux**
1. Склонируйте репозиторий `git clone <repository>`
2. Перейти в папку с репозиторием
3. Настройте переменные для подключения к основным компонентам сервера:
```Docker
environment:
      - database_username=u1346925_mobile # Имя пользователя БД
      - database_password=wO_2iI2pE9d! # Пароль для полключение к БД
      - database_ip=31.31.196.208 # ip сервера, на котором установлена БД
      - database_name=u1346925_mebel # Название таблицы
      - mail_username=info@mobile.massive-mebel.ru # Имя пользователя почты (полное или сокращённое)
      - mail_password=vQ7vR9!oT2e  # Имя пользователя почты
      - mail_from=info@mobile.massive-mebel.ru # Имя пользователя почты (полное)
      - mail_port=465 # Порт SMTP
      - mail_server=mail.mobile.massive-mebel.ru  # Сервер отправки почты
labels:
      - "traefik.enable=true" # Включение компонентов
      - "traefik.http.routers.fastapi.rule=Host(`mobile.massive-mebel.ru`)" # Укажите доменное имя
      - "traefik.http.routers.fastapi.tls=true" # Принудительное включение TLS
      - "traefik.http.routers.fastapi.tls.certresolver=letsencrypt" # Использование letsencrypt для получения сертификатов
```
4. Собирите контейнер `docker-compose build`
5. После успешной сборки запустите контейнер `docker-compose up -d`, Пре перезагрузки сервера контенер сам запуститься.

> Примечание
>> Сертификаты SSL letsencrypt автоматически будут продлеваться **за месяц до окончания** без необходимости перезагрузки сервера


## Возможные проблемы
Некоторые зависимости (драйвер MySQL) требуют дополнительный пакетов, установите их (Необязательно, всё сделвет Docker):
`sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`
