from setuptools import setup


long_description = """
# LiteVkApi
Бот в Вк? Легко!

Pypi - https://pypi.org/project/LiteVkApi/

# КРАТКАЯ ДОКУМЕНТАЦИЯ
Привет! Эта библиотека создана для быстрого написания ботов (преимущественно ЛС) в ВК. Мне захотелось, чтобы ботов писать было быстро и легко, поэтому я сделал удобную библиотеку с самыми популярными функциями vk_api. Сейчас я расскажу вам о ней!

P.s. Если вы читаете это в PypI, то у вас могут некорректно отображаться таблички с пояснениями функций. На Гитхабе все хорошо - https://github.com/Ma-Mush/LiteVkApi/

# Внимание! 

### С обновления 2.0 структура библиотеки немного поменялась. 

Боты, написанные на версиях 1.x не будут работать на версиях 2.x. Чтобы они снова работали, достаточно записать в переменную Vk функцию Vk.login, вот так:
```
Vk = Vk.login(параметры)
```

Теперь вы можете регистрировать одновременно сразу несколько ботов и использовать свои переменные в качестве объекта функции (в документации рассмотрена переменная Vk).

Этот код:
```python
from LiteVkApi import Vk
Vk = Vk.login(твой ид, "твой токен")
while True:
    if Vk.check_new_msg():
        event = Vk.get_event()
        Vk.msg(event.text, event.user_id)
```

Будет работать абсолютно так-же, как и этот:
```python
from LiteVkApi import Vk
vk_session = Vk.login(твой ид, "твой токен")
while True:
    if vk_session.check_new_msg():
        event = vk_session.get_event()
        vk_session.msg(event.text, event.user_id)
```

### Обратите внимание, что не все функции должны принимать в качестве объекта Вашу переменную!
Так, функции Vk.login и Vk.give_session ВСЕГДА ДОЛЖНЫ БЫТЬ С "Vk"


## Импорты
Для начала установите vk_api, если он не установлен - pip3 install vk_api

Скрипт библиотеки написан в виде функций и различных переменных в классе, поэтому можно использовать несколько вариантов импорта:
Рекомендую - from LiteVkApi import Vk (будет описана здесь), import LiteVkApi (придется использовать LiteVkApi.Vk._), < один из предыдущих вариантов > as < название > (вместо названия импортированного модуля можно использовать свое имя)

## _.help()
Функция выведет в консоль информацию, которая описывает основное строение билиотеки, как с ней работать, что она может и так далее. Вообщем документация на минималках)

## Vk.Login(id_group, token, userbot=False, chats=False, my_key=0, my_server=0, my_ts=0) *

### Функция ВСЕГДА имеет объект Vk
Функция регистрирует вас на сервере ВКонтакте и с обновления 2.0 возвращает сессию в переменную.
Параметры:
Название  | Что это?
------------- | -------------
id_group | id группы в числовом виде (например 200397283), если используется юзер-бот - любое число
token | Токен сообщества в виде строки (например 'a244f42a676ec65dbod1e713aab88e735e311448868357u545c27cd64802tc8a31ee66e462 8a0a4ca98be')
userbot | Для страницы (а не для группы) вы используете бота? (True/False) По умолчанию False
get_session | Если True - возвращает сессию в переменную (для удобства использования вместе vk_api). По умолчанию False
chat | Для беседы вы используете бота или нет (True / False)? По умолчанию False
ост. | Настройки для беседы, узать тут - https://vk.com/dev/groups.getLongPollServer

p.s. Для бесед не тестировал, возможны ошибки) 

## _.get_session()
Возвращает сессию Вконтакте, т.е. ели вы уже вошли через Vk.login и вам надо пользоваться обычным vk_api, то вы можете использовать эту сессию, чтобы не входить снова. (Тоже самое на vk_api - vk_session = vk_api.VkApi(token = токен))

## Vk.give_session(session) *

#### Функция ВСЕГДА имеет объект Vk
Регистрирует вашу сессию Вк, но только если вы уже входили через другие api и передали ее в параметр session (для vk_api сессия получается через session = vk_api.VkApi(token = токен))
Параметры:
Название  | Что это?
------------- | -------------
session | Сессия в Вк
ост. | Настройки для беседы, узать тут - https://vk.com/dev/groups.getLongPollServer

## _.msg(text, userid chats=False)
Отправляет сообщение пользователю по ID / беседе по ее номеру с заданным текстом
Параметры:
Название  | Что это?
------------- | -------------
text | Текст сообщения 
userid | ID пользователя/беседы для отправкии сообщеия
chat | Для беседы вы используете бота или нет (True / False)? По умолчанию False

## _.check_new_msg()
Используется для проверки новых сообщений (возвращает True / False)
Параметры:
Название  | Что это?
------------- | -------------
chat | Для беседы вы используете бота или нет (True / False)? По умолчанию False

## _.get_event()
Возвращает данные о новом сообщении при его наличии. Основные параметры выданных данных - user_id / chat_id, text. Подробнее в документации vk_api.

## _.send_photo(file_name, userid, msg=None, chats=False)
Отправляет фото с сообщением / без него пользователю/беседе.
Параметры:
Название  | Что это?
------------- | -------------
file_name | имя файла в директории запущенного питон-файла или полный путь к нему
userid | ID пользователя/беседы для отправкии сообщеия
msg | Текст сообщения (по умолчанию без него)
chat | Для беседы вы используете бота или нет (True / False)? По умолчанию False

## _.new_keyboard(dicts, perm=True)
Создание клавиатуры (возвращает данные в переменную для отправки)
Параметры:
Название  | Что это?
------------- | -------------
dicts | Масив со словарями, содержащими данные о кнопках. 
perm | Будет ли сохранятся клавиатура после нажатия (True / False)? По умолчанию True. (Лайфхак - False можно использовать вместо delete_keyboard при поэтапной выдаче клавиатур)

По кнопкам: 

Словарь для обычной кнопки - {Текст:Цвет} (все цвета - ['POSITIVE', '3', 'ЗЕЛЕНЫЙ'], ['NEGATIVE', '2', 'КРАСНЫЙ'], ['SECONDARY', '1', 'БЕЛЫЙ'], ['PRIMARY', '0', 'СИНИЙ']).

Для переноса на новую линию - {"new_line":""}. 

Для открытие перевода в VkPay - {"vk_pay":hash твоего кошелька}. 

Для открытия мини-приложения Вконтакте - {"open_app":[{"app_id":ид приложения}, {"owner_id":owner id приложения}, {"label":текст на кнопке}, {"hash":хэш приложения}]}

Для открытия ссылки на любой ресурс - {"open_link":[{"label":текст кнопки}, {"link":ссылка с http / https / www}]}

## _.send_keyboard(keyboard, userid, msg='Клавиатура!', chats=False)
Отправляем пользователю созданнуб раннее клавиатуру
Параметры:
Название  | Что это?
------------- | -------------
keyboard | Клавиатура, созданная раннее
userid | Ид пользователя / беседы
msg | Сообщение при отправке клавиатуры (по умолчанию 'Клавиатура!')
chats | Для беседы вы используете бота или нет (True / False)? По умолчанию False

## _.delete_keyboard(userid, msg='Клавиатура закрыта!', chats=False)
Удаляет клавиатуру у пользователя. 
Параметры:
Название  | Что это?
------------- | -------------
userid | Ид пользователя / беседы
msg | Сообщение при удалении клавиатуры (по умолчанию 'Клавиатура закрыта!')
chats | Для беседы вы используете бота или нет (True / False)? По умолчанию False

## _.send_file(file_name, userid, msg=None, chats=False)
Отправляет файл с сообщением / без него пользователю/беседе.
Параметры:
Название  | Что это?
------------- | -------------
file_name | имя файла в директории запущенного питон-файла или полный путь к нему
userid | ID пользователя/беседы для отправкии сообщеия
msg | Текст сообщения (по умолчанию без него)
chat | Для беседы вы используете бота или нет (True / False)? По умолчанию False

## _.mailing(text, userids, safe=[], chats=False)
Делает рассылку независимо от других действий (бот будет отвечать во время рассылки).
Параметры:
Название  | Что это?
------------- | -------------
text | Текст сообщения
userids | Массив с ID пользователей / бесед (например - [123456, 1234567, 12345678])
safe | Массив с ID пользователей / бесед, которые отказались от рассылки, по умолчанию таких нет
chat | Для беседы вы используете бота или нет (True / False)? По умолчанию False

## _.get_all_message_data()
Возвращает массив со словарями с данными о последних сообщениях всех чатов, где находился бот (и ЛС, и беседы, и боты). Внимание! Функция достаточно долгая для ботов с большой аудиторией. Может занимать от 0.1 секунды до минуты.

Что находится в словарях:
Название  | Что это?
------------- | -------------
date | Количиство секунд с 01.01.1970 00:00 UTC, также как time.time()
from_id | Id группы или пользователя, кто отправил последнее сообщение (может быть как и бот, так и пользователь)
id | Id этого сообщения
out | 0 / 1, 0 - последнее сообщение присали вам, 1 - последнее сообщение прислали вы
peer_id | Id чата - chat_id если это беседа, user_id если это Лс (ну или id группы если это бот)
random_id | Какой рандомный Id у сообщения (нужен для его отправки, фактически бесполезен)
text | Текст сообщения
attachments | Описание вложений (фото, видео, файлы, стикеры и тд.) последнего сообщения (если это просто текст - [])
admin_author_id | Если out=1 и писал не бот, а человек, то в этот параметр передается id админа, который писал сообщение
update_time | Если сообщение редактировали, то передается время редактирования в формате, как в date
conversation_message_id | Уникальный автоматически увеличивающийся номер для всех сообщений с этим peer
fwd_messages | Массив пересланных сообщений, если они есть (если нет - [])
important | В документации не нашел, скорее всего избарнный (важный) чат или нет (True/False)
is_hidden | В документации не нашел, скорее всего скрытое сообщение (удалено у меня) или нет (но это не точно) (True/False)

## _.get_all_open_id(message_data=None)
Возвращает в переменную массив с Id всех пользоватлей, которые когда-либо писали боту или id бесед, где он находится (куда ему можно писать - для рассылки)
Параметры:
Название  | Что это?
------------- | -------------
message_data | Данные, полученные с помощью get_all_message_data*, по умолчанию None, функция * вызывается автоматически

## _.VkMethod(method_name, arg)
Возвращает в переменную данные, полученные в результате запроса с помощью Вк-метода. Создана для удобства, чтобы не имортировать vk_api и получать сессию)
Параметры:
Название  | Что это?
------------- | -------------
method_name | Назване Вк-метода (все методы тут - https://vk.com/dev/methods )
arg | Параметры для метода в виде словаря

# Примеры
## Отправка сообщения с тем же текстом, тому же пользователю, что и прислали нам:
```python
from LiteVkApi import Vk
vk_session = Vk.login(твой ид, "твой токен")
while True:
    if vk_session.check_new_msg():
        event = vk_session.get_event()
        vk_session.msg(event.text, event.user_id)
```
## Простейший бот:
```python
from LiteVkApi import Vk
vk_session = Vk.login(твой ид, "твой токен")
while True:
    if vk_session.check_new_msg():
        event = vk_session.get_event()
        eventxt, userid = event.text, event.user_id
        if eventxt == 'Привет':
            vk_session.msg(f'Привет, {userid}', userid)
        elif eventxt == 'Как дела?':
            vk_session.msg('Хорошо, а у тебя?', userid)
```
## Создание, отправка и удаление клавиатуры:
```python
from LiteVkApi import Vk
vk_session = Vk.login(твой ид, "твой токен")
while True:
    if vk_session.check_new_msg():
        event = vk_session.get_event()
        if event.text == 'Клавиатура':
            kbrd = [{'Клавиатура':"синий"}, {'new_line':""}, {'Закрыть клавиатуру':'3'}, 
{'new_line':''}, {'open_link':[{'label':'Создатель библиотеки'}, {'link':'https://vk.com/maks.mushtriev2'}]}]
            keyboard = vk_session.new_keyboard(kbrd)
            vk_session.send_keyboard(keyboard, event.user_id, 'А вот и клавиатура!')
        elif event.text == 'Закрыть клавиатуру':
            vk_session.delete_keyboard(event.user_id, 'Теперь клавиатура закрыта!')
```
## Отправка файла и фото:
```python
from LiteVkApi import Vk
vk_session = Vk.login(твой ид, "твой токен")
while True:
    if vk_session.check_new_msg():
        event = vk_session.get_event()
        try:
            vk_session.send_photo(event.text, event.user_id, 'Отправляю фото...')
            vk_session.send_file(event.text, event.user_id, 'Отправляю файл...')
        except:
            vk_session.msg('Не могу найти файл {} или указанный файл не является фотографией'.format(event.text), event.user_id)
```
## Рассылка кому только можно
```python
from LiteVkApi import Vk
vk_session = Vk.login(твой ид, "твой токен")
mass_ids = vk_session.get_all_open_id()
vk_session.mailing('Рассылка!', mass_ids)
```

# Контакты

Что-то не работает, есть вопросы, пожелания? Пиши - vk.com/maks.mushtriev2, t.me/Error_mak25

Мой блог - vk.com/mamush_blog

Донат - vk.cc/az7BQK (Киви)


### Удачи!
"""


with open("requirements.txt") as requirements:
    requirements = requirements.read().split("\n")


setup(
    name="LiteVkApi",
    version="2.1",
    description="Библиотека для лекгого написания ботов ВК!",
    packages=["LiteVkApi"],
    author_email="ma_mush@mail.ru",
    zip_safe=False,
    python_requires=">=3.6",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=requirements
)
