# API для Yatube.
API для проекта YaTube, основанный на Django-Rest-Framework

API позволяет обрабатывает GET, POST, PATCH, PUT и DELETE запросы к базе данных Yatube

Документация к API: http://127.0.0.1:8000/redoc/

### Как запустить проект:

Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/russ044/api_final_yatube.git
```

```
cd api_final_yatube
```

Cоздать и активировать виртуальное окружение:

```
python -m venv env
```

```
source env/Scripts/activate
```

```
python -m pip install --upgrade pip
```

Установить зависимости из файла requirements.txt:

```
pip install -r requirements.txt
```

Выполнить миграции:

```
python manage.py migrate
```

Запустить проект:

```
python manage.py runserver
```

### Примеры запросов

Получение списка всех постов:
```
    GET /api/v1/posts/
```
Создание нового поста:
```
    POST /api/v1/posts/
    body: {"text": "string"}
```
Получение поста по его id
```
    GET /api/v1/posts/{post_id}/
```
