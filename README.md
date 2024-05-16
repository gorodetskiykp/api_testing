# Установка

- `git clone https://github.com/gorodetskiykp/api_testing.git`
- `cd api_testing`
- `python -m venv venv` &ndash; Windows  
`python3 -m venv venv` &ndash; Mac / Linux
- `venv\Scripts\activate venv` &ndash; Windows  
`source venv/bin/activate` &ndash; Mac / Linux
- `pip install -r requirements.txt` &ndash; Windows  
`pip3 install -r requirements.txt` &ndash; Mac / Linux

# Настройка Django
`python` для Windows, `python3` для Mac/Linux
- `python manage.py migrate`

# Запуск проекта
`python` для Windows, `python3` для Mac/Linux
- `python manage.py runserver`

# Запросы
### GET
- http://127.0.0.1:8000/some-app/guest - список гостей
- http://127.0.0.1:8000/some-app/hotel - список отелей
- http://127.0.0.1:8000/some-app/room - список комнат
- http://127.0.0.1:8000/some-app/booking - список бронирований

### POST
Указаны только обязательные поля - все поля модели можно посмотреть GET-запросом
- http://127.0.0.1:8000/some-app/guest  
```json
{
    "name": "Tom",
    "phone": "123456",
    "email": "tom@mail.ru"
}
```
- http://127.0.0.1:8000/some-app/hotel  
```json
{
    "name": "Radisson",
    "phone": "1234321",
    "email": "radisson@mail.ru",
    "location": "Moscow"
}
```
- http://127.0.0.1:8000/some-app/room  
```json
{
    "hotel": 1
}
```
- http://127.0.0.1:8000/some-app/booking  
```json
{
    "guest": 1,
    "room": 1,
    "hotel": 1
}
```
# База данных
При выполнении `python manage.py migrate` создается БД SQLite3 - `db.sqlite3`  
Она не запоролена. Можно подключиться к ней и проверить работу POST-запросов.
# WEB-админка
1. Завести админа: `python manage.py createsuperuser`
2. Адрес админки: http://127.0.0.1:8000/admin