# MobileShop
Back-end для мобильной версии сайта


***Запуск и установка:***
### Debug
1. Склонировать репозиторий `git clone <repository>`
2. Перейти в папку с репозиторием
3. Создать виртуальное окружение `python -m venv .venv` (Необязательно)
4. Войти в виртуальное окружение
5. Установить зависимости `pip intsall  --no-cache-dir  -r requirements.txt`
6. Перейти в папку с **main.py** `cd app/`
7. Выполнить для локального запуска `uvicorn main:app --reload`

***Настройка проекта:***

Создайте файл `.env` в app, используя следующий шаблон:

```.env
DATABASE_USERNAME="<имя пользователя базы данных>"
DATABASE_PASSWORD="<пароль пользователя базы данных>"
DATABASE_IP="<ip адрес базы данных>"
DATABASE_NAME="<имя базы данных>"

MAIL_USERNAME="<имя>"
MAIL_PASSWORD="<gfhjkm>"
MAIL_FROM="<имя>@<домен>"
MAIL_PORT=<smtp порт>
MAIL_SERVER="<домен почтового сервера>"

RECIPIENT_LIST="<почта #1>, почта #2"
или 
RECIPIENT_LIST="<почта #1>"
```

### Release (Установка на сервер)
1. Склонируйте репозиторий `git clone <repository>`
2. Перейти в папку с репозиторием
3. Настройте переменные [docker-compose.yml](https://github.com/TheJecksMan/MobileShop/blob/master/docker-compose.yml) для подключения к основным компонентам сервера:
```Docker
 environment:
      - DATABASE_USERNAME=
      - DATABASE_PASSWORD=
      - DATABASE_IP=
      - DATABASE_NAME=
      - MAIL_USERNAME=
      - MAIL_PASSWORD=
      - MAIL_FROM=
      - MAIL_PORT=465
      - MAIL_SERVER=
      - RECIPIENT_LIST=
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
6. После успешной сборки запустите контейнер `docker-compose up -d`, Пре перезагрузки сервера контенер сам запуститься.

> Примечание
>
> Сертификаты SSL letsencrypt автоматически будут продлеваться **за месяц до окончания** без необходимости перезагрузки сервера


## Возможные проблемы
Некоторые зависимости (драйвер MySQL) требуют дополнительный пакетов, установите их (Необязательно, всё сделвет Docker):
`sudo apt-get install python3-dev default-libmysqlclient-dev build-essential`
