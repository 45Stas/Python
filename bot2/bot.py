import telebot
import config

bot = telebot.TeleBot(config.token)

ingr = ("Картофель ", "лук ", "колбаса", "майонез", "соленные огурцы", "морковь")
gramm = (50, 20, 100, 15, 30, 30)
    
@bot.message_handler(commands = ['olivie'])
def print_olivie(message):
    bot.send_message(message.chat.id, "Введите кол-во человек:")

@bot.message_handler(content_types = ["text"])
def olivie(message):
    print(message)
    try:
        people_count= int(message.text)
        for i in range(0, len(ingr)):
            bot.send_message(message.chat.id,(ingr[i] + " - " + str(gramm[i] * people_count) + "гр."))
    except:
        print("Ошибка")
        
if __name__ =='__main__':
    bot.polling(none_stop=True)
