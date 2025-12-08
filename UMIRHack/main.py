# импортируем фреймворк и тип значений для дополнительного описания
from fastapi import FastAPI, Query

# импортируем тип значений Optional
from typing import Optional
# импортируем базовый класс объектов
from pydantic import BaseModel

# создаём объект приложения FastAPI
app = FastAPI()

@app.get("/")

async def home():
    return {"First message" : "Hello, World! I started working with FastAPI"}

team = {
       1: {"Cap": "Kamalin Igor Vladimirovich",
         "Age": 21,
         "University": "RSUE",
         "Group": "PI-321"
        },
        2: {
            "Name": "Anna",
         "Surname": "Shevtsova",
         "Age": 18,
         "University": "RSUE",
         "Group": "PI-311"
        },
         3: {
             "Name": "Lyudmila",
          "Surname": "Drugova",
          "Age": 19,
          "University": "RSUE",
          "Group": "IST-321"
         },
          4: {
              "Name": "Margarita",
           "Surname": "Shevlyakova",
           "Age": 18,
           "University": "RSUE",
           "Group": "PI-311"
          }

    }

# создаём ещё один GET-эндпойнт с проверкой типа и получением значения по ключу:
@app.get('/get-human/{human_id}')
# пишем асинхронную обработку запроса и указываем
# тип значения, который ждём от пользователя: целое число
async def get_human(human_id: int):
   # возвращаем информацию о книге с выбранным номером
   return team[human_id]


#создаём POST-запрос

# создаём класс-модель для добавления в нашу команду
class HumanInfo(BaseModel):
   # переменная Name будет строкой
   Name: str
   Surname: str
   # переменная price будет вещественным числом
   Age: int
   University: str
   Group: str
   # переменная author будет опциональной, строкового типа и по умолчанию равной None
   Music: Optional[str] = None

# создаём POST-эндпойнт:
@app.post('/create-human/{human_id}')
# пишем асинхронную обработку запроса и указываем тип значений, который
# ждём от пользователя: целое число и словарь по шаблону HumanInfo
async def create_human(human_id: int, new_human: HumanInfo):
   # проверяем, что в словаре team ещё нет человека с таким номером
   if human_id in team:
       # выводим сообщение об ошибке, которое FastAPI трансформирует в JSON
       return {'Error': 'Human already exists'}

   # если человека с таким номером ещё нет, создаём его под этим номером
   # и с теми же параметрами, которые указали в классе HumanInfo
   team[human_id] = new_human
   # возвращаем данные о новом внесённом человеке
   return team[human_id]

#Создаём PUT-запрос
# создаём класс-модель специально для обновлений участников
class UpdateHuman(BaseModel):
   # переменная book будет строкой
   book: Optional[str] = None
   # переменная price будет вещественным числом
   price: Optional[float] = None
   # переменная author будет опциональной, строкового типа и по умолчанию равной None
   author: Optional[str] = None

# создаём PUT-эндпойнт:
@app.put('/update-human/{human_id}')
# пишем асинхронную обработку запроса и указываем тип значений, который
# ждём от пользователя: целое число и словарь по шаблону UpdateHuman
async def update_human(human_id: int, upd_human: UpdateHuman):
   # проверяем, что в словаре team есть человек с таким номером
   if human_id not in team:
       # если такого человека нет, выводим сообщение об ошибке
       return {'Error': 'Human ID does not exists'}

