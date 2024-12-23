# Транзакция Библиотек
Описанное ниже рассчитано, что вы знаете как клонировать данные из репозитория, \
легко устанавливаете зависимости, у вас настроен `radis` и знаете , \
что такое `сельдерей` .

## Примечание ("прочитать перед употреблением")
Приложение имеет полноценную базу данных (БД).\
БД содержит таблицы:
- [Автор книг](project/models_some/model_autors.py);
- [Клиент библиотеки](project/models_some/model_client.py);
- [Книги](project/models_some/model_book.py);
- [Выдача книг](project/models_some/model_borrow.py);
- [Несколько](project/models_some/model_person.py) [базовых](project/models_some/model_init.py) таблиц.

Есть сценарии [для транзакции](project/transaction_some) с таблицами, \
построенные на ООП. 
### Динамические классы
1. При этом [Library_Person](project/transaction_some/transaction_person.py)
ДИНАМИЧЕСКИЙ класс.  
Для работы с клиентами и/или авторами используется единый класс. На входе \ 
указываем лишь образ модели с которой работаем. 

2. При этом класс [Library_basis](project/transaction_some/transaction_basic.py),\
работает напрямую с БД. Единый сценарий обработки данных от `Library_basis`\
для всех 4-ёх объектов/образов (book, author, client, borrow).

### Логирование
Сценарии [имеют логирование](project/logs.py). Результат видно в консоли и в файле `log_putout.log`. \
![loger](/img/text_of_loger.png)


### База данных
![db](/img/db.png)\
Сама БД:
- написана на `sqlalchemy`;
- создавалась на момент разработки в `postgraSQL`.

Первичный и каждые последующие запуски автоматически запускают \
файл `project/models.py` и проверку на наличие базы и таблиц. \
Сама связь c `postgreSQL` реализована через `project/models_more/postcresbase.py`.

Вам достаточно лишь переписать соединение под свой тип БД в строках\
```text
 connection = psycopg2.connect(
        user=f"{APP_POSTGRES_LOGIN}",
        password=f"{APP_POSTGRES_PASS}",
        host=f"{APP_POSTGRES_HOST}",
        port=f"{APP_POSTGRES_PORT}",
    )
```
из файла `project/models_more/postcresbase.py`.

Всё остальное через `sqlalchemy`. \
При запуске отрабатываются файлы `project/models.py` и `project/models_some`.

### FastAPI
Раннее предполагал, что `FastAPI` есть аналог OpenAPI и спокойно работал с  \
асинхронным кодом на базе `Flask`. Изучив `FastAPI` было уже поздно переписывать, поэтому \
вся логика написана на `Flask`.

### OpenAPI
OpenAPI так же изучил в рабочем режиме и создан [YAML-файл](swagger/swagger.yml).


## Stack
```text
[tool.poetry.dependencies]
python = "^3.10"
python-dotenv = "^1.0.1"
pytest-cov = "^6.0.0"
pytest-asyncio = "^0.24.0"
flower = "^2.0.1"


[tool.poetry.group.dev.dependencies]
asyncio = "^3.4.3"
autohooks = "^24.2.0"
flake8 = "^7.1.1"
pre-commit = "^3.8.0"
markdown = "^3.7"
pylint = "^3.3.1"
isort = "^5.13.2"
black = "^24.8.0"
postgres = "^4.0"
psycopg2-binary = "^2.9.10"
sqlalchemy = "2.0.36"
pytest = "^8.3.3"
flask = {extras = ["async"], version = "^3.1.0"}
wtforms = "^3.2.1"
flask-sqlalchemy = "^3.1.1"
flask-login = "^0.6.3"
flask-bootstrap = "^3.3.7.1"
flask-jwt-extended = "^4.7.1"
flask-wtf = "^1.2.2"
flask-admin = {extras = ["export", "images", "s3", "sqlalchemy", "translation"], version = "^1.6.1"}
flask-swagger-ui = "^4.11.1"
flask-bcrypt = "^1.0.1"
flasgger = "^0.9.7.1"
```
Тестирование не проводилось.

## .env
```text
APP_POSTGRES_DBNAME=< dbname_for_your_db >
APP_POSTGRES_LOGIN=< login_for_your_db >
APP_POSTGRES_PASS=< password_for_your_db >
APP_POSTGRES_HOST=localhost
APP_POSTGRES_PORT=5432
SECRET_KEY= < secret_key_of_your_app >

```
## Команды
Вы знаете, что такое `pip` & `poetry` и умеете их устанавливать.
В создании проекта использовался `poetry`.

## requirements.txt
`requirements.txt` это результат авто-генерации от `poetry`.

### Установка зависимостей
```text
poetry install
# or
pip install requirements.txt
```

### Старт приложения
```text
python main.py

// or
Shift+F9
```

#### Для работы через PyCharm
```text
Env. Var.: PYTHONUNBUFFERED=1,  PYTHONTRACEMALLOC=1, PWDEBUG=1
```
![pycharm](./img/pycharm.png)


### API
API в файле `project/views*.py` и [swagger.yml](swagger/swagger.yml). 



