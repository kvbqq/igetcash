import telebot

bot = telebot.TeleBot("1178105570:AAGj75FAaaNzZPHXHDtqMTFKUmuFVOFp6Uk")

@bot.message_handler(commands=['start'])
def first_message(message):
	bot.send_message(message.chat.id, "Witamy w getcash! Aby zacząć zarabiać wpisz /lista żeby wyświetlić listę wszystkich promocji.\nWpisz /komendy żeby wyświetlić listę wszystkich komend.")

@bot.message_handler(commands=['lista'])
def offers_list(message):
	bot.send_message(message.chat.id, "Wybierz jedną z odpowiadających Ci ofert. Wpisz odpowiadającą jej literkę żeby otrzymać instrukcję odebrania pieniędzy ! (np. /A) \n\nA. Trading 212 - od 10 do 100 euro - rejestracja KYC + wpłata 5zł\n\nB. Bitpanda - otrzymujemy ok 70zł (15€) - rejestracja KYC + wpłata 110 zł (25€) KTÓRE OD RAZU MOŻNA WYPŁACIĆ\n\nC. Swissborg wealth app - od 1 do 100 euro - rejestracja KYC + wpłata 50€")

@bot.message_handler(commands=['komendy'])
def commands_info(message):
	bot.send_message(message.chat.id, "/start - wstępna informacja\n/lista - wyświetla listę ofert")

@bot.message_handler(commands=['A', 'a'])
def offer_a(message):
	bot.send_message(message.chat.id, 'Trading 212 powróciło otrzymaj akcję do 100€ za depozyt 5zł\nMakler cyfrowy, regulowanym przez FCA.\n\nOtrzymasz akcje o wartości do 500 zł za rejestracje oraz za każde polecenie również otrzymasz akcję o wartości do 500 zł\n\nInstrukcja:\n1. Utwórz konto Trading 212 po kliknięciu w link (konieczne żeby otrzymać bonus)\n\nwww.trading212.com/invite/GIO3ft83\n\nUWAGA wybierz tylko "Trading 212 Invest" podczas rejestracji!!!\n\n2. Zweryfikuj konto (dowód osobisty, prawo jazdy, paszport.)\n\n3. Dokonaj depozytu o wartości 5 zł.\n\n4. W ciągu 24h dostajesz akcje spółek giełdowych na swoje konto.\n\n5. Polecaj dalej, aby otrzymać kolejne akcje.\n\nAkcje można sprzedać i wypłacić pieniądze')

@bot.message_handler(commands=['B', 'b'])
def offer_b(message):
	bot.send_message(message.chat.id, 'Jak zdobyć 15€?\n\n1. Wchodzimy w LINK\n\nhttps://www.bitpanda.com/?ref=896233009933149521\n\ni podajemy swoje konto podając imię/nazwisko i adres e-mail. Weryfikujemy nasz adres e-mail klikając w link w mailu, wracamy do Bitpanda i zaczynamy proces weryfikacji.\n\n2. Wybieramy light verification - czyli prostą weryfikacje dokumentem. Teraz przekieruje Cie do weryfikacji dowodem, tylko zdjęcie trwa to do 3 minut.Jeżeli masz problemy z aparatem, spróbuj inna przeglądarkę lub apkę na telefon (najlepsza opcja).Aby odebrać bonus musimy zrobić depozyt mimimum €25 i kupić kryptowaluty o minimalnej wartości 25€\n\n3. Jak zrobić depozyt aby oderbać 10€?Klikamy zakładkę "Wallets"Szukamy EURO - klikamy Deposit - podpinamy kartę (w ten sposób najszybciej otrzymamy kase)\n\n-UWAGA - W razie gdybyś zdecydował się na przelew, to  nie przechodzą z Revoluta - polecam BNC10 lub N26 lub z Banku Polskiego wystarczy zrobić przelew zagraniczny SEPA.Kiedy depozyt dojdzie na konto Bitpanda, wchodzimy w portfolio - Szukamy walutę TETHER (zielona ikonka z "T") i klikamy BUY - wybieramy EUR i wartość MAX.Potwierdzamy BUY NOWBonus 10€ powinien już być na naszym koncieteraz możemy sprzedać kryptowalutę na euro.\n\nWchodzimy w link do quizu:\n\nhttps://www.bitpanda.com/academy/en/tests/beginner-test\n\nwykonujemy go i czekamy na otrzymanie 5€. ')


@bot.message_handler(commands=['C', 'c'])
def offer_c(message):
	bot.send_message(message.chat.id, 'Swissborg wealth app – aplikacja ta służy do inwestowania w kryptowaluty. Ta giełda kryptowalut nie posiada żadnych ukrytych prowizji.\nW pełni bezpieczna, działa w świetle prawa.\n\nJak otrzymać bonus od 1€ do 100€?\n\nInstrukcja w kilku krokach:\n\n1. Rejestrujemy się z linku (tylko z nim otrzymamy bonus).\nLink: https://join.swissborg.com/r/mikoajIFTB\n\n2. Ściągamy i instalujemy aplikację.\n\n3. Dokonujemy weryfikacji KYC. Standardowo – dane, dowód / prawo jazdy + selfie.\n\n4. Dokonujemy depozyt 50€.\n\nPo tym dostaniemy kupon, który doda nam do konta Bitcoin o wartości od 1 do 100€.\n\nBONUS Z DEPOZYTEM MOŻEMY WYPŁACIĆ NATYCHMIASTOWO!!!')

bot.polling()
