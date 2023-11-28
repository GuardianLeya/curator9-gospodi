import telebot

bot = telebot.TeleBot('6973879046:AAEV0q3CyaJJON6gMIGyvFj5UpJCJUXQDZM')

text_poll = "Расскажи анекдот"
text_button_1 = "Еще один"
text_button_2 = "Хочу узнать, что такое катарсис"
text_button_3 = "Хочу узнать, какой я смешарик"

# кнопки меню
menu_keyboard = telebot.types.ReplyKeyboardMarkup(one_time_keyboard=True, resize_keyboard=True)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_poll,
    )
)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_1,
    )
)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_2,
    )
)
menu_keyboard.add(
    telebot.types.KeyboardButton(
        text_button_3,
    )
)


@bot.message_handler(commands=['start'])
def main(message):
    bot.send_message(message.chat.id, 'Ну и что ты хочешь от меня', reply_markup=menu_keyboard)


@bot.message_handler(commands=['end'])
def main(message):
    bot.send_message(message.chat.id, '*Я тебе сейчас закончу, э*', parse_mode='Markdown')


@bot.message_handler(commands=['farewell'])
def main(message):
    bot.send_message(message.chat.id, 'Я говорю до свидания, а не _прощай..._', parse_mode='Markdown')


# меню
@bot.message_handler(func=lambda message: text_poll == message.text)
def help_command(message):
    bot.send_message(message.chat.id,
                     'После войны. Урок в школе. Учительница задает на дом написать сочинение, кто как помогал солдатам на фронте. \nНа следующий день учительница проверяет домашнее задание: - Ну кто написал. \nМаша поднимает руку и читает свое сочинение:"Я помогала маме, мы вместе шили шинели для солдат!" \n- Молодец, Маша, садись. \nПетя читает свое сочинение:"Я в колхозе работал, солдатам еду отправлял!" \n- Молодец, Петя, садись. Кто еще как помогал? \nВовочка читает:"А я солдатам на фронте патроны подавал!!!" \nУчительница:"И что они тебе говорили?"\n Вовочка: "Зер гуд, Вольдемар, зер гуд!"',
                     reply_markup=menu_keyboard)


@bot.message_handler(func=lambda message: text_button_1 == message.text)
def help_command(message):
    bot.send_message(message.chat.id,
                     "Наркоман устраивается в цирк. \n- Могу прыгнуть из-под купола без страховки прямо на манеж. \n- Ух ты! Покажите! \n- Алееее...! \nПрыгает. Шмяк... Лежит. Тишина... \n- Он разбился! ? Пульс еще есть! Врача!!!\nПрибегает врач. \n- Пульс замедляется. Срочно два кубика морфина! \nДелает укол. Наркоман встает раскинув руки в стороны. \n- Оп!",
                     reply_markup=menu_keyboard)


@bot.message_handler(func=lambda message: text_button_2 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "[Посмотри вот тут](https://youtu.be/TqlCGVrJZeI?si=Q01mKuRd1BAl3-5S)",
                     reply_markup=menu_keyboard)  # Можно менять текст


@bot.message_handler(func=lambda message: text_button_3 == message.text)
def help_command(message):
    bot.send_message(message.chat.id, "[Много хочешь](https://uquiz.com/quiz/nABDfw/Кто-ты-из-Смешариков)",
                     reply_markup=menu_keyboard)


bot.infinity_polling()