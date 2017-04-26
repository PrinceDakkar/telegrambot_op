import telebot as t
import constant
import os

token = "374165457:AAFeMZcirstwPhIDBEAuwFT8NP0yVl0X76c"
bot = t.TeleBot(token)

@bot.message_handler(commands=['start'])
def handle_start(message):
    user_markup = t.types.ReplyKeyboardMarkup()
    user_markup.row('Команды', '/Информация')
    user_markup.row('F.A.Q')
    bot.send_message(message.from_user.id, 'СТРИМЫ ВЕБКАМЕР ХАКЕРА С ДВАЧА. '
                                           'Если не хочешь потерять стримы подпишись,'
                                           ' на этот паблик - https://vk.com/kanalodnogoantona,'
                                           ' так как на каналы прилетают баны через'
                                           ' 1-2 стрима(из-за митспинов и наготы).', reply_markup=user_markup)

@bot.message_handler(commands=['Информация'])
def handle_start(message):
    user_markup_info = t.types.ReplyKeyboardMarkup()
    user_markup_info.row('Слитые файлы', '/start')
    user_markup_info.row('Годные выпуски')
    bot.send_message(message.from_user.id, 'Что тебя интересует?', reply_markup=user_markup_info)


@bot.message_handler(content_types=['text'])
def handle_text(message):
    if message.text == 'Слитые файлы':
        received_info = open("info.txt")
        information = received_info.read()
        bot.send_message(message.from_user.id, information)
        received_info.close()

    elif message.text == 'Годные выпуски':
        vipuski = open("vipuski.txt")
        vipusk = vipuski.read()
        bot.send_message(message.from_user.id, vipusk)
        vipuski.close()

    elif message.text == 'F.A.Q':
        bot.send_message(message.from_user.id, 'Тут пока нихуя нету, поэтому соси')
    elif message.text == 'Команды':
        bot.send_message(message.from_user.id, 'Ты охуел? какие тебе команды?')
    else:
        bot.send_message(message.from_user.id, 'Что ты несешь?')


bot.polling(none_stop=True, interval=0)

