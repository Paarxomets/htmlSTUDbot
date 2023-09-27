import requests
from bs4 import BeautifulSoup
import telebot
TOKEN = '6511462995:AAF5UDwGf-maBLDM6EEHQp86IIMPp7fH5J4'
bot = telebot.TeleBot(TOKEN)
@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Привет! Введи свой логин и пароль для авторизации на сайте.")
@bot.message_handler(func=lambda message: True)
def parse_website(message):
    # Получаем логин и пароль от пользователя
    login, password = message.text.split()
    # Отправляем POST-запрос для авторизации на сайте
    login_url = 'https://portal.sutd.ru'
    login_data = {
        'username': login,
        'password': password
    }
    session = requests.Session()
    session.post(login_url, data=login_data)
    # Парсим информацию с сайта
    website_url = 'https://portal.sutd.ru'
    response = session.get(website_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    # Находим нужные данные на странице и сохраняем их
    data = soup.find('div', {'class': 'data'}).text
    # Отправляем данные в виде сообщения боту
    bot.reply_to(message, f"Информация с сайта: {data}")
bot.polling()
