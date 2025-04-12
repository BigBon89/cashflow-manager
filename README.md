# Cashflow Manager
Веб-сервис для учета, управления и анализа
поступлений и списаний денежных средств компании или частного лица.

# Возможности
* Учет поступлений и списаний
* Гибкое управление статусами, типами, категориями и подкатегориями
* Удобный интерфейс через Django Admin
* Фильтрация записей по дате, типу, статусу и т.д.

# Установка

```
pip install -r requirements.txt
cd cashflow_manager
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

# Использование
```http://127.0.0.1:8000/admin```

![Image](https://i.imgur.com/5KmRnFb.png)