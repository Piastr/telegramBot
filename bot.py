import telebot
import random
from telebot import types
from main import *
#from main import goroscope, get_recipe, get_sinonims
import urllib.request
import xlrd

token = '5150145944:AAE2j-SV4bgFj_LU5spM48hQZQsqGyrTlaY'

global list_of_pain
list_of_pain = []



# Создаем бота
bot = telebot.TeleBot(token)


# Команда start
@bot.message_handler(commands=["start"])
def start(m, res=False):

    # Добавляем кнопку
    markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
    markup.add(types.KeyboardButton(":P"))
    markup.add(types.KeyboardButton("Гороскоп"))
    markup.add(types.KeyboardButton("Рецептики"))
    markup.add(types.KeyboardButton("Расписание"))
    markup.add(types.KeyboardButton("Дневник"))
    markup.add(types.KeyboardButton("Синонимы"))
    bot.send_message(m.chat.id, 'Нажми: \n:Р для получения интересного факта о себе', reply_markup=markup)


# Получение сообщений от юзера
@bot.message_handler(content_types=["text"])
def handle_text(message):

    if message.text.strip() == ':P':
        answer = random.choice(y)
        bot.send_message(message.chat.id, answer)

    if message.text.strip() == "Гороскоп":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Водолей"))
        markup.add(types.KeyboardButton("Стрелец"))
        markup.add(types.KeyboardButton("Назад"))
        bot.send_message(message.chat.id, 'Так так, и шо у нас там', reply_markup=markup)
# Назад
    if message.text.strip() == "Назад":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton(":P"))
        markup.add(types.KeyboardButton("Гороскоп"))
        markup.add(types.KeyboardButton("Рецептики"))
        markup.add(types.KeyboardButton("Расписание"))
        markup.add(types.KeyboardButton("Дневник"))
        markup.add(types.KeyboardButton("Синонимы"))
        bot.send_message(message.chat.id, 'Нажми: \n:Р для получения интересного факта о себе', reply_markup=markup)
# Меню рецептов
    if message.text.strip() == "Рецептики":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("Суп"))
        markup.add(types.KeyboardButton("Второе"))
        markup.add(types.KeyboardButton("Салат"))
        markup.add(types.KeyboardButton("Завтрак"))
        markup.add(types.KeyboardButton("Назад"))
        bot.send_message(message.chat.id, 'Кушать захотелось?)', reply_markup=markup)

# Возврат ссылки на рецепт
    if message.text.strip() == "Суп":
        keyboard = types.InlineKeyboardMarkup()
        x = get_recipe(2)
        url_but = types.InlineKeyboardButton(text=x[0], url=f"https://www.russianfood.com{x[1]}")
        keyboard.add(url_but)
        bot.send_message(message.chat.id, "Приятного аппетита:):", reply_markup=keyboard)
    if message.text.strip() == "Второе":
        keyboard = types.InlineKeyboardMarkup()
        x = get_recipe(3)
        url_but = types.InlineKeyboardButton(text=x[0], url=f"https://www.russianfood.com{x[1]}")
        keyboard.add(url_but)
        bot.send_message(message.chat.id, "Приятного аппетита:)", reply_markup=keyboard)
    if message.text.strip() == "Салат":
        keyboard = types.InlineKeyboardMarkup()
        x = get_recipe(35)
        url_but = types.InlineKeyboardButton(text=x[0], url=f"https://www.russianfood.com{x[1]}")
        keyboard.add(url_but)
        bot.send_message(message.chat.id, "Приятного аппетита:):", reply_markup=keyboard)
    if message.text.strip() == "Завтрак":
        keyboard = types.InlineKeyboardMarkup()
        x = get_recipe(926)
        url_but = types.InlineKeyboardButton(text=x[0], url=f"https://www.russianfood.com{x[1]}")
        keyboard.add(url_but)
        bot.send_message(message.chat.id, "Приятного аппетита:)", reply_markup=keyboard)

# Возврат гороскопа
    if message.text.strip() == "Стрелец":
        answer = goroscope('https://horo.mail.ru/prediction/sagittarius/today/')
        bot.send_message(message.chat.id, answer)
    if message.text.strip() == "Водолей":
        answer = goroscope('https://horo.mail.ru/prediction/aquarius/today/')
        bot.send_message(message.chat.id, answer)

# Дневник и его внутренности
    if message.text.strip() == "Дневник":
        markup = types.ReplyKeyboardMarkup(resize_keyboard=True)
        markup.add(types.KeyboardButton("И что у нас?"))
        markup.add(types.KeyboardButton("Удалить запись"))
        markup.add(types.KeyboardButton("Очистить всё"))
        markup.add(types.KeyboardButton("Назад"))
        bot.send_message(message.chat.id, 'Опять гадости наговорила?)', reply_markup=markup)
    if message.text.strip().startswith("Дорогой дневник, "):
        bot.send_message(message.chat.id, "Запомним")
        x = str(message.text[17:])
        if not(x[0].istitle()):
            x = x.capitalize()
        list_of_pain.append(x)
    if message.text.strip() == "И что у нас?":
        for i in range(len(list_of_pain)):
            x = str(i+1) + '. ' + list_of_pain[i]
            bot.send_message(message.chat.id, x)
    if message.text.strip() == "Удалить запись":
        send = bot.send_message(message.chat.id, "Введи номер записи:")
        bot.register_next_step_handler(send, delete_pain)
    if message.text.strip() == "Очистить всё":
        list_of_pain.clear()
        bot.send_message(message.chat.id, "Готово")

# Расписание
    if message.text.strip() == "Расписание":
        book = xlrd.open_workbook("lessons.xls")
        sheet = book.sheet_by_index(2)
        list_lessons = []
        for i in range(30):

            if i == 0:
                list_lessons.append('Понедельник')
            if i == 6:
                list_lessons.append('Вторник')
            if i == 12:
                list_lessons.append('Среда')
            if i == 18:
                list_lessons.append('Четверг')
            if i == 24:
                list_lessons.append('Пятница')
            time = sheet.cell_value(rowx=20 + i * 2, colx=2)
            cell = sheet.cell_value(rowx=20 + i * 2, colx=6)
            aud = sheet.cell_value(rowx=21 + i * 2, colx=6)
            aud_corrected = aud[-8::]
            lesson = time + ' ' + cell + ' ' + aud_corrected
            list_lessons.append(lesson)
        monday = '* '
        vtornik = '* '
        sreda = '* '
        chetverg = '* '
        friday = '* '
        for i in list_lessons[0:7]:
            monday += "- " + i + "\n"
        for i in list_lessons[7:14]:
            vtornik += "- " +i + "\n"
        for i in list_lessons[14:21]:
            sreda += "- " +i + "\n"
        for i in list_lessons[21:28]:
            chetverg += "- " +i + "\n"
        for i in list_lessons[28:35]:
            friday += "- " +i + "\n"
        bot.send_message(message.chat.id, monday)
        bot.send_message(message.chat.id, vtornik)
        bot.send_message(message.chat.id, sreda)
        bot.send_message(message.chat.id, chetverg)
        bot.send_message(message.chat.id, friday)

# Синонимы
    if message.text.strip() == "Синонимы":
        send = bot.send_message(message.chat.id, "Введи слово:")
        bot.register_next_step_handler(send, get_sinonims)

def get_sinonims(message):
    list_sinonims = []
    url = f'https://kartaslov.ru/синонимы-к-слову/{message.text}'
    responce = requests.get(url)
    soup = BeautifulSoup(responce.text, 'lxml')
    sinonims = soup.find_all('ul', class_='v2-syn-list')
    dop_sinonims = soup.find_all('ul', class_='v2-syn-list v2-syn-head-list')
    for i in sinonims:
        x = i.find_all('li')
        for k in x:
            y = k.find('a').text
            if y not in list_sinonims:
                list_sinonims.append(y)
    for i in list_sinonims:
        bot.send_message(message.chat.id, i)

def delete_pain(message):
    if message.text.isdigit():
        try:
            number_pain = int(message.text) - 1
            del list_of_pain[number_pain]
            bot.send_message(message.chat.id, "Готово")
        except IndexError:
            bot.send_message(message.chat.id, "Нет такого номера")
    else:
        bot.send_message(message.chat.id, "Это не цифра:(")


@bot.message_handler(content_types=['document'])
def get_document(message):
    file_id = message.document.file_id
    file_info = bot.get_file(file_id)
    #bot.download_file(file_path='/lessons')
    print(f'http://api.telegram.org/file/bot{token}/{file_info.file_path}')
    destination = 'lessons.xls'
    url = f'http://api.telegram.org/file/bot{token}/{file_info.file_path}'
    urllib.request.urlretrieve(url, destination)
# Запускаем бота
bot.polling(none_stop=True, interval=0)


