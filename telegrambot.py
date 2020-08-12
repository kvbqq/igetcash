import telebot
import os
from intro_to_flask import app

port = int(os.environ.get("PORT", 5000))
app.run(debug=True, host='0.0.0.0', port=port)

bot = telebot.TeleBot("1178105570:AAGj75FAaaNzZPHXHDtqMTFKUmuFVOFp6Uk")

@bot.message_handler(commands=['start'])
def first_message(message):
	bot.send_message(message.chat.id, "Witamy w getcash! Aby zacząć zarabiać wpisz /lista żeby wyświetlić listę wszystkich promocji.\nWpisz /komendy żeby wyświetlić listę wszystkich komend.")

@bot.message_handler(commands=['lista'])
def offers_list(message):
	bot.send_message(message.chat.id, "Wybierz jedną z odpowiadających Ci ofert. Wpisz odpowiadającą jej literkę żeby otrzymać instrukcję odebrania pieniędzy ! (np. /A) \n\nA. Trading 212 - od 10 do 100 euro - rejestracja KYC + wpłata 5zł")

@bot.message_handler(commands=['komendy'])
def commands_info(message):
	bot.send_message(message.chat.id, "/start - wstępna informacja\n/lista - wyświetla listę ofert")

@bot.message_handler(commands=['A'])
def offer(message):
	bot.send_message(message.chat.id, 'Trading 212 powróciło otrzymaj akcję do 100€ za depozyt 5zł\nMakler cyfrowy, regulowanym przez FCA.\n\nOtrzymasz akcje o wartości do 500 zł za rejestracje oraz za każde polecenie również otrzymasz akcję o wartości do 500 zł\n\nInstrukcja:\n1. Utwórz konto Trading 212 po kliknięciu w link (konieczne żeby otrzymać bonus)\n\nwww.trading212.com/invite/GIO3ft83\n\nUWAGA wybierz tylko "Trading 212 Invest" podczas rejestracji!!!\n\n2. Zweryfikuj konto (dowód osobisty, prawo jazdy, paszport.)\n\n3. Dokonaj depozytu o wartości 5 zł.\n\n4. W ciągu 24h dostajesz akcje spółek giełdowych na swoje konto.\n\n5. Polecaj dalej, aby otrzymać kolejne akcje.\n\nAkcje można sprzedać i wypłacić pieniądze')

bot.polling()
