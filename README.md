# Flask REST API
Серверная часть приложения, представляющая собой REST API.
Реализация - Python, Flask.

## Требования
- [Python 3.9.x](https://www.python.org/downloads/)
- [Git](https://git-scm.com)
- [Ngrok](https://ngrok.com/download) - опциально, для деплоя веб-сервера в сети

## Деплой проекта

### 1. Склонировать репозиторий. 
```
git clone https://github.com/bibilka/flask-rest-api.git
```
### 2. Создание виртуальной среды.
Переходим в папку с проектом и выполняем команду:
```
python -m venv venv
```
Активируем виртуальную среду:
```
.\venv\Scripts\activate
```
Подгружаем зависимости проекта (пакеты):
```
pip install -r requirements.txt
```
### 3. Настройка проекта (env, миграции).

Создаем файл под конфигурацию среды приложения. Выполняем команду: ```cp .flaskenv.example .flaskenv```.

Генерируем секретный ключ для JWT.
```
python generate_secret.py
```
Вставляем сгенерированное значение в ```.flaskenv``` файл.
```
SECRET_KEY=secret
```
Для настройки и заполнения базы данных с помощью миграций выполняем команды:
```
flask db upgrade
```

### 4. Запуск.

Запускаем веб-сервер:
```
flask run
```
#### Дополнительно:
- заполнение базы данных значениями:
```
python db_seeder.py
```

- для разработки:
```
# создание базы данных
flask db init

# создание миграции
flask db migrate -m "custom migration message"
```

- для деплоя в сети:
```
./ngrok config add-authtoken <token>
./ngrok http 5000
```
_____
:white_check_mark: <b>Готово!</b> :+1: :tada: 

Проект запущен и доступен по адресу: `http://localhost:5000/` или `http://127.0.0.1:5000/`