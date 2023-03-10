## Решение ДЗ №3 по теме "django, djangoORM, views". TODO - list. 

### Задание:  

Список дел - это приложение в котором пожно просматривать, создавать, изменять и удалять записи, которые являются описанием задач. Например "помыть посуду", "вынести мусор" или "приготовить суп" - могут быть такими задачами. Ваша цель - написать приложение для управления таким списком.  

В каждой задаче есть название, говорящее о том что нужно сделать, например "купить в магазине новый утюг". В каждой задаче есть отметка выполнена она или нет (по умолчанию не выполнена). У каждой задачи есть дата и время создания, дата и время завершения. Время завершения задачи проставляется в момент проставления галочки о завершении задачи. Время завершения задачи убирается (становится null) в момент снятия галочки о завершении задачи.  

Через админ сайт можно создавать, изменять и удалять задачи. Через админ сайт можно найти задачу по названию.  

В браузере можно открыть страницу со списком всех незавершенных задач. В браузере можно открыть страницу с формой на добавление новой задачи и добавить ее. В браузере можно через форму изменить задачу. В браузере по кнопке можно удалить задачу.  


*    Написать приложение используя фреймворк django. Самостоятельно составьте модель под требования.
*    должно быть доступно управление задачами из админки
*    должно быть доступно управление задачами из страниц, обслуживаемых с помошью TemplatedViews (ListView, CreateView, DetailView и другие)
*    используйте requirements.txt для указания сторонних зависимостей и их версий
*    используйте реляционную субд
*    Форматирование учитывается. Используйте black
---
  
### Инструкция по запуску:
1. Установить пакеты `"pip install -r requirements.txt"`
2. Запуск из корня программы: `python3 manage.py runserver`
3. Приложение доступно по адресу `http://127.0.0.1:8000/`  
            для admin (admin/admin)
---
  
### Решение:  
##### Структура навигации приложения:  
Главная страница (http://127.0.0.1:8000/):  
`ADMIN PANEL` - переходв в панель администратора;  
`Домой` - Статистика дел (всего и незавершенных) с активными областями перехода (цифры кликабельны);  
`Добавить задачу` - переход на форму регистрации новой задачи. Ожидает заполнения поля "Задача";  
`Все дела` - содержит список всех дел. Зеленые - выполненные, красные - на выполнение. Все задачи кликабельны и ведут к переходу на форму конкретной задачи;  
`Все незавершенные дела` - содержит список всех незавершенных дел. Все задачи кликабельны и ведут к переходу на форму конкретной задачи;  
  
Форма конкретной задачи:  
`Стаус выполнения` - состояние задачи;  
`Дата создания` - записывается в момент регистрации задачи;  
`Дата выполнения` - проставляется в момент выполнения задачи;  
`URL Post` - slug строка, заполняется автоматически и служит для индивидуализации задачи в url парадигме;  
Кнопка `РЕДАКТИРОВАТЬ` - переход на форму редактирования задачи;  
Кнопка `УДАЛИТЬ` - переход на форму удаления задачи.  
  
Форма редактирования задачи:  
`Status` - изменение статуса выполнения задачи;  
`Задача` - редактирование название задачи;  
`URL Post` - slug строка, заполняется автоматически;  
Кнопка `UPDATE` - применение изменений.  
  
Форма удаления задачи:  
Кнопка `DELETE` - подтверждение удаления задачи.  
  
##### Структура ADMIN PANEL:  
`ID задачи` - номер задачи;  
`Status` - состояние задачи;  
`Задача` - имя задачи. Можно редактировать на месте;  
`date create` - записывается в момент регистрации задачи;  
`date complite` - проставляется в момент выполнения задачи;  
`URL Post` - slug строка, заполняется автоматически и служит для индивидуализации задачи в url парадигме;  
Кнопка `Add to list` - создание новой задачи с аналогичным функционалом;  
События `Action` содержит пункты удаления задачи, перевод в статусы выполнено и не выполнено.  
Реализован `поиск` по "name" и "id", есть `фильтр` по статусу.  

##### Структура DB:  
Вся информация сохраняется в `sqlite3` в таблицу вида:  
```python
Table nouts {
    status = models.BooleanField(default=False, help_text="Статус выполнения")
    name = models.CharField(max_length=64, verbose_name="Задача")
    slug = models.SlugField(null=False, unique=True, blank=True, db_index=True, verbose_name="URL Post")    
    date_complite = models.DateTimeField(auto_now=False, null=True, blank=True, default=None)
    date_create = models.DateTimeField(auto_now_add=True)
}
```  
Код отформатирован средствами `BLACK`.  

##### Структура папок и файлов:  
```python
----django-todolist\
    |----todo_list\
    |    |----README.md
    |    |----db.sqlite3
    |    |----manage.py
    |    |----todo_list\
    |    |    |----asgi.py
    |    |    |----__init__.py
    |    |    |----urls.py
    |    |    |----settings.py
    |    |    |----wsgi.py
    |    |----mylist\
    |    |    |----models.py
    |    |    |----apps.py
    |    |    |----admin.py
    |    |    |----views.py
    |    |    |----templates\
    |    |    |    |----todolist.html
    |    |    |    |----item_delete.html
    |    |    |    |----item_detail.html
    |    |    |    |----item_create.html
    |    |    |    |----todolist_full.html
    |    |    |    |----index.html
    |    |    |    |----item_update.html
    |    |    |    |----base.html
    |    |    |    |----base__.html
    |    |    |----migrations\
    |    |    |    |----__init__.py
    |    |    |----__init__.py
    |    |    |----urls.py
    |    |    |----tests.py
    |    |    |----static\
    |    |    |    |----css\
    |    |    |    |    |----styles.css  
```  
---  
