# -*- coding: utf-8 -*-
import telebot
import requests
from bs4 import BeautifulSoup


# Initialized bot
bot = telebot.TeleBot('278758102:AAENnsnUdlaLTklqCaoj0F8hSckxoR-_t10')

# Start description
@bot.message_handler(commands=['start'])
def default_test(message):
    bot.send_message(message.from_user.id, 'Please input audio track title or performer\'s name.')

# Get request
@bot.message_handler(content_types=["text"])
def handle(message):
    # Parsing website
    url = 'https://downloadmusicvk.ru/audio/search?q=' + parser(message.text)
    source_code = requests.get(url)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    for link in soup.findAll('div', {'class' : 'row audio'}, limit=5):
        name_of_song = link.find('div', {'class' : 'col-lg-9 col-md-8 col-sm-7 col-xs-5'}).text
        # Getting download page
	    # go to 3rd block
        link_to_download = link.find('div', {'class' : 'col-lg-2 col-md-3 col-sm-4 col-xs-5'})
            # go to download button
        link_to_download = link_to_download.find('a', {'class' : 'btn btn-primary btn-xs download'})
        
        # Page to download
        main_link = 'https://downloadmusicvk.ru' + link_to_download.get('href')
        # Get final link to download
        source = handle_song(main_link)
        
        code = '<a href=\"' + source + '\">' + str(counter) + '. ' + name_of_song.strip() + '</a>'
        bot.send_message(message.from_user.id, parse_mode='HTML', text = code)


# Get final link to download
def handle_song(main_link):
    source_code = requests.get(main_link)
    plain_text = source_code.text
    soup = BeautifulSoup(plain_text, "html.parser")
    button = soup.find('a', {'class' : 'btn btn-success btn-lg btn-block download'})
    return 'https://downloadmusicvk.ru' + button.get('href')


# Make request right
def parser(message):
    message = message.strip()
    answer = ""
    for letter in message:
        if letter != " ":
            answer += c
        else:
            answer += '+'
    return answer

# Non stop our bot
if __name__ == '__main__':
    bot.polling(none_stop=True)


