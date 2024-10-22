# api_final

API FINAL

## Описание

Этот проект предоставляет возможность работы с записями, подписками и комментарями.
Он предназначен для создания и управления контентом через API-интерфейс, что позволяет легко интегрироваться с различными приложениями и сайтами.

### Цели проекта

- Предоставить удобный и быстрый способ работы с записями, комментариями и подписками.
- Обеспечить API с понятной документацией и примерами для интеграции.

## Установка

1. Клонируйте репозиторий:
    ```bash
    git clone <URL>
    ```
2. Установите виртуальное окружение:
    ### Windows
    ```bash
    python -m venv venv
    . venv/Scripts/activate
    ```
    ### Linux/MacOS
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```
4. Примените миграции:
    ```bash
    python yatube_api/manage.py migrate
    ```
5. Запустите проект:
    ```bash
    python yatube_api/manage.py runserver
    ```
6. OPTIONAL. После запуска сервера полная версия документации доступна будет доступна [здесь](http://127.0.0.1:8000/redoc/)

## Примеры запросов

### Получение списка постов:

```http
GET /api/v1/posts/
```

### Создание нового поста:

```http
POST /api/v1/posts/
```

## Авторы

- [alanbong](https://github.com/alanbong)
- [yandex-praktikum](https://github.com/yandex-praktikum)