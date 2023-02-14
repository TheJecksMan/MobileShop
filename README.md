# MobileShop
Данный проект предоставляет API используя данные CMS OpenCart


***Запуск и установка:***
### Debug
1. Склонировать репозиторий `git clone <repository>`
2. Перейти в папку с репозиторием `cd <dir>`
3. Создать виртуальное окружение `python -m venv .venv` (Необязательно)
4. Войти в виртуальное окружение
5. Установить зависимости `pip intsall  --no-cache-dir  -r requirements.txt`
6. Перейти в папку с **main.py** `cd app/`
7. Создать файл .env по следующему образцу:
```.env
DATABASE_USERNAME="<имя пользователя базы данных>"
DATABASE_PASSWORD="<пароль пользователя базы данных>"
DATABASE_IP="<ip адрес базы данных>"
DATABASE_NAME="<имя базы данных>"

MAIL_USERNAME="<имя>"
MAIL_PASSWORD="<пароль>"
MAIL_FROM="<имя>@<домен>"
MAIL_PORT=465
MAIL_SERVER="<почтовый сервер>"

DEBUG_MODE="/docs" # Только для отладки!

RECIPIENT_LIST="<почта #1>, <почта #2>"
или 
RECIPIENT_LIST="<почта #1>"
```
8. Запустить `uvicorn main:app --reload`

### Release (Установка на сервер)
1. Склонируйте репозиторий `git clone <repository>`
2. Перейти в папку с репозиторием `cd <dir>`
3. Настройте переменные [docker-compose.yml](https://github.com/TheJecksMan/MobileShop/blob/master/docker-compose.yml) для подключения к основным компонентам сервера:
```Docker
 environment:
      - DATABASE_USERNAME=<имя пользователя базы данных>
      - DATABASE_PASSWORD=<пароль пользователя базы данных>
      - DATABASE_IP=<ip адрес базы данных>
      - DATABASE_NAME=<имя базы данных>
      - MAIL_USERNAME=<имя>
      - MAIL_PASSWORD=<пароль>
      - MAIL_FROM=<имя>@<домен>
      - MAIL_PORT=465
      - MAIL_SERVER=<почтовый сервер>
      - RECIPIENT_LIST=<email#1,email#2>
    labels:
      - "traefik.enable=true"
      - "traefik.http.routers.fastapi.rule=Host(`<domain>`)"
      - "traefik.http.routers.fastapi.tls=true"
      - "traefik.http.routers.fastapi.tls.certresolver=letsencrypt"
```
4. Настроить ACME в [traefik.toml](https://github.com/TheJecksMan/MobileShop/blob/master/traefik.toml)
```toml
[certificatesResolvers.letsencrypt.acme]
  email = "<почта привязанная к домену>"
```
5. Соберите контейнер `docker-compose build`
6. После успешной сборки запустите контейнер `docker-compose up -d` (При перезагрузки сервера, контейнер запуститься автоматически).

> Примечание
>
> Сертификаты SSL Let’s Encrypt автоматически будут продлеваться (**за месяц до окончания**) без необходимости перезагрузки сервера.
