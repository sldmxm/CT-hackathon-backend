# Сервис найма на Карьерном трекере Яндекс Практикума - бэкенд

### Авторы
Сервис разработан в рамках хакатона 19-31 октября 2023 года.
Команда NoName:

ФИО, ссылки и роли

**/////// TO DO !!!! /////**

### Работающий сервис
**/////// TO DO !!!! /////**

### Cтэк технологий
- Python 3.11
- Django 4.1
- DjangoRESTframework
- PostgreSQL
- Nginx
- Docker
**/////// TO DO !!!! /////**

### Документация
- Правила [разработки](/docs/dev_rules.md) и [кодстайл](/docs/codestyle.md)

- Полная документация по работе с API http://localhost/api/docs/redoc/ и http://localhost/api/docs/swagger/

### Разворачиваем проект локально:
1. Склонируйте проект, перейдите в папку `/backend`
    ```shell
    git clone git@github.com:sldmxm/CT-hackathon-backend.git
    cd CT-hackathon-backend
    ```
2. Убедитесь что poetry установлен. Активируйте виртуальное окружение. Установите зависимости
    ```shell
    poetry shell
    poetry install
    ```
3. **/////// TO DO !!!! /////**
Обновите субмодуль с фронтом
   ```shell
   git submodule init
   git submodule update --remote
   ```
Разверните и запустите базу данных, используя postgres-local.yaml и docker compose.
    ```shell
    docker compose -f postgres-local.yaml up -d
    ```
4. Дополнительно: остановка и удаление и т.д. как с любым контейнером docker, например:
    ```shell
    docker compose -f postgres-local.yaml down  # остановить
    docker compose -f postgres-local.yaml down --volumes  # остановить и удалить базу
    ```
5. Сделайте миграции
    ```
    python backend/manage.py migrate
    ```
6. Установите pre-commit хуки
    ```shell
    pre-commit install --all
    ```
7. Убедитесь, что при запуске ваш IDE использует правильное виртуальное окружение. В противном случае - самостоятельно укажите путь к виртуальному окружению. Посмотреть путь можно следующей командой:
    ```shell
    poetry env info --path
    ```
8. **/////// TO DO !!!! /////**

Файл `.env` должен находиться в корневой папке проекта. Если вы решите не создавать свой `.env` файл - в проекте предусмотрен файл `.env_local`, обеспечивающий переменные для базовой работы на локальном уровне.

### Заполнение БД тестовыми данными
Доступна команда для наполнения БД данными:
```
python manage.py filldb
```
Команда заполняет базу тестовыми данными, справочники берет из директории /backend/data/
В ней лежат csv названия которых совпадают с названиями моделей, в которые они будут загружены.
```
python manage.py superuser
```
Команда создает администратора из параметров в .env файле, по умолчанию admin/admin.

Для очистки БД от данных (но не удаления таблиц) можно использовать команду:
```
python manage.py flush
```
