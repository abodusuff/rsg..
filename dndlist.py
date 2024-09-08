import telebot

API_TOKEN = '7196131491:AAEe3qqLZoNTCk1q8qndiaZ9fumQrP-Rq8s'  # Замените на токен вашего бота
bot = telebot.TeleBot(API_TOKEN)

# Начальное состояние
user_data = {}

@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет! Я бот, который поможет вам рассчитать углеродный след. "
                                       "Сколько километров вы проезжаете на автомобиле в неделю?")
    bot.register_next_step_handler(message, process_mileage)

def process_mileage(message):
    try:
        user_data['mileage'] = float(message.text)
        bot.send_message(message.chat.id, "Теперь, сколько килограммов мяса вы потребляете в неделю?")
        bot.register_next_step_handler(message, process_meat)
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение.")
        bot.register_next_step_handler(message, process_mileage)

def process_meat(message):
    try:
        user_data['meat'] = float(message.text)
        # Расчет углеродного следа (примерные значения)
        carbon_footprint = (user_data['mileage'] * 0.271) + (user_data['meat'] * 7.3)
        bot.send_message(message.chat.id, f"Ваш углеродный след составляет примерно кг CO2 в неделю.")
        bot.send_message(message.chat.id, "Если хотите пересчитать, напишите /start.")
    except ValueError:
        bot.send_message(message.chat.id, "Пожалуйста, введите числовое значение.")
        bot.register_next_step_handler(message, process_meat)
    botper = eval(process_mileage * process_meat / 10000)
    bot.send_message(message.chat_id, botper )
if __name__ == '__main__':
    bot.polling(none_stop=True)

