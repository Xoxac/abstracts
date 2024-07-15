import telebot
import requests
import json


'''Для того, чтобы создать бота необходимо написать @BotFather, дать команду /newbot, чтобы создать нового бота.
Затем необходимо настроить его через меню.
Получить токен (token) - строку вида 110201543:AAHdqTcvCH1vGWJxfSeofSAs0K5PALDsaw.
Установить pyTelegramBotAPI с помощью команды в командной строке: pip3 install pyTelegramBotAPI.'''

# После установки необходимо создать новый файл, импортировать туда модуль telebot и создать объект bot,
# используя токен, полученный при регистрации:
TOKEN = "7375731420:AAG-Y4JjG68CaJ3S3csRGYTCKyv6jApsNgc"
bot = telebot.TeleBot(TOKEN)

# Чтобы запустить бота, нужно воспользоваться методом polling: bot.polling()

# Для того чтобы из обычной функции сделать обработчик сообщений для бота,
# надо воспользоваться декоратором @bot.message_handler:
# @bot.message_handler(filters)
# def function_name(message):
#     bot.reply_to(message, "This is a message handler")

# filters — фильтры, определяющие, следует ли вызывать декорированную функцию для соответствующего сообщения или нет.
# У одного обработчика может быть несколько фильтров:
# Название фильтра	| Аргумент	                          | Условие выполнения функции
# content_types	    | Список строк, по умолчанию ['text'] | Если тип контента, содержащегося в сообщении совпадает с типом указанным в качестве аргумента.
# commands	        | Список строк	                      | Если сообщение начинается с команды, указанной в списке.

# https://core.telegram.org/bots/api#message

# @bot.message_handler()
# def test(message: telebot.types.Message):
#     bot.send_message(message.chat.id, "Hello")

keys = {'доллар': 'USD',
        'рубль': 'RUB',
        'евро': 'EUR'}

class ConvertionException(Exception):
    pass

class CryptoConverter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):

        if quote == base:
            raise ConvertionException(f'невозможно перевести одинаковые валюты {base}')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise ConvertionException(f'не удалось обработать валюту {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise ConvertionException(f'не удалось обработать валюту {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConvertionException(f'не удалось обработать количество {amount}')

        r = requests.get(f'https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}')
        total_base = json.loads(r.content)[keys[base]]

        return total_base


@bot.message_handler(commands=['start', 'help'])
def help(message: telebot.types.Message):
    text = 'Для начала работы введите команду в формате: \n<какую валюту> <в какую валюту перевести> <количество> через пробел \nсписок доступных валют: /values'
    bot.reply_to(message, text)


@bot.message_handler(commands=['values'])
def help(message: telebot.types.Message):
    text = 'Доступные валюты: '
    for key in keys.keys():
        text = '\n'.join((text, key,))
    bot.reply_to(message, text)


@bot.message_handler(content_types=['text'])
def convert(message: telebot.types.Message):

    values = message.text.split(' ')

    if len(values) != 3:
        raise ConvertionException('Слишком много параметров')

    quote, base, amount = values
    total_base = CryptoConverter.convert(quote, base, amount)

    text = f'Цена {amount} {quote} в {base} - {total_base}'
    bot.send_message(message.chat.id, text)


bot.polling()
