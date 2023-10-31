# Сервис найма на Карьерном трекере Яндекс Практикума - бэкенд

### Авторы
Сервис разработан в рамках хакатона 19-31 октября 2023 года.
Команда NoName

### [Работающий сервис](http://130.193.36.223/)


### Cтэк технологий
- Python 3.11
- Django 4.1
- DjangoRESTframework
- PostgreSQL
- Nginx
- Docker

### Документация
- Правила [разработки](/docs/dev_rules.md) и [кодстайл](/docs/codestyle.md)

- Полная документация по работе с API http://localhost/api/docs/redoc/ и http://localhost/api/docs/swagger/

### Разворачиваем проект локально для разработки
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
3. Обновите субмодуль с фронтом
   ```shell
   git submodule init
   git submodule update --remote
   ```
4. Сделайте миграции
    ```
    python backend/manage.py migrate
    ```
5. Установите pre-commit хуки
    ```shell
    pre-commit install --all
    ```

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
