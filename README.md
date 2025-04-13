# api_yatube

## Описание

Этот проект предоставляет возможность работы с записями, подписками и комментарями.
Он предназначен для создания и управления контентом через API-интерфейс, что позволяет легко интегрироваться с различными приложениями и сайтами.

### Цели проекта

- Предоставить удобный и быстрый способ работы с записями, комментариями и подписками.
- Обеспечить API с понятной документацией и примерами для интеграции.

## Установка

1. Клонируйте репозиторий и перейти в него в командной строке:
    ```
    git clone https://github.com/alanbong/api_yatube.git
    ```
    ```
    cd API_FINAL_YATUBE
    ```
2. Установите и активируйте виртуальное окружение:
    ### Windows
    ```
    python -m venv venv
    . venv/Scripts/activate
    ```
    ### Linux/MacOS
    ```
    python3 -m venv venv
    source venv/bin/activate
    ```
3. Установите зависимости из файла requirements.txt:
    ### Windows
    ```
    pip install -r requirements.txt
    ```
    ### Linux/MacOS
    ```
    python3 -m pip install --upgrade pip
    ```
4. Примените миграции:
    ```
    python yatube_api/manage.py migrate
    ```
5. Запустите проект:
    ```
    python yatube_api/manage.py runserver
    ```
6. Опционально. После запуска сервера полная версия документации доступна будет доступна [здесь](http://127.0.0.1:8000/redoc/)

## Примеры запросов

### Получение списка постов:

```
GET /api/v1/posts/
```

### Создание нового поста:

```
POST /api/v1/posts/
```

## Авторы

- [alanbong](https://github.com/alanbong)
- [yandex-praktikum](https://github.com/yandex-praktikum)
