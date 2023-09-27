import telebot
from flask import Flask, render_template
app = Flask(__name__)
bot = telebot.TeleBot('6511462995:AAF5UDwGf-maBLDM6EEHQp86IIMPp7fH5J4')
@app.route('/')
def home():
    return render_template('index.html')
@bot.message_handler(commands=['start'])
def start(message):
# ваш код для обработки команды /start
@bot.message_handler(func=lambda message: message.text == 'Открыть веб приложение')
def open_web_app(message):
# ваш код для открытия веб-приложения
if __name__ == '__main__':
    bot.polling(none_stop=True)
    app.run()
