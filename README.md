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

### Правила [разработки](/docs/dev_rules.md) и [кодстайл](/docs/codestyle.md)

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

**/////// TO DO !!!! /////**

Доступна команда для наполнения БД данными:
```
python manage.py filldb
```
Команда заполняет базу такими тестовыми данными, как:
- студенты
- вакансии/поиски
- пользователи: админы, HR

Для очистки БД от данных (но не удаления таблиц) можно использовать команду:
```
python manage.py flush
```
