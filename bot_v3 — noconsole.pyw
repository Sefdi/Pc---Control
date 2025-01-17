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
import asyncio
from colorama import Fore, Back, Style
import socket
import subprocess


hostname = socket.gethostname()
colorama.init()

# Получаем текущую дату и время
now = datetime.datetime.now()

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
	"  \n"
    "`PCStatus | Sefd1Relax | V3`"
)




keyboard = telebot.types.InlineKeyboardMarkup()
button = telebot.types.InlineKeyboardButton(text="Выключить компьютер", callback_data="shutdown_computer")
button2 = telebot.types.InlineKeyboardButton(text="Перезагрузить компьютер", callback_data="restart_computer")
status_bt = telebot.types.InlineKeyboardButton(text="Узнать статус", callback_data="status_for_pc")
screen_bt = telebot.types.InlineKeyboardButton(text="Скриншот", callback_data="screen_bt")
keyboard.add(button)
keyboard.add(button2)
keyboard.add(status_bt)
keyboard.add(screen_bt)

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
											   " \n"
                                               "`PCStatus | Sefd1Relax | V3`", parse_mode="Markdown")
	

    elif call.data == "restart_computer":
        subprocess.run("shutdown /r /t 1", shell=True)
        bot.send_message(call.message.chat.id, f"┌ 🖥 × Статус компьютера: `Перезагрузка`\n"
											   f"└ ☄ × Название ПК: `{hostname}` \n"
											   f" \n"
											   f"📃 × Тип отправки: `Console | Button`\n"
											   f"⏰ × Время перезагрузки: `{now.strftime('%H:%M')}`\n"
											   f"📅 × Дата перезагрузки: `{now.strftime('%Y-%m-%d')}`\n"
                                                "`PCStatus | Sefd1Relax | V3`", parse_mode="Markdown")
    elif call.data == "status_for_pc":
        bot.send_message(call.message.chat.id, f"┌ 🖥 × Статус компьютера: `Включён`\n"
                                               f"└ ☄ × Название ПК: `{hostname}` \n"
                                               f" \n"
                                               f"📃 × Тип отправки: `Узнать статус`\n"
                                               f"⏰ × Время статуса: `{now.strftime('%H:%M')}`\n"
                                               f"📅 × Дата статуса: `{now.strftime('%Y-%m-%d')}`\n"
                                                "`PCStatus | Sefd1Relax | V3`", parse_mode="Markdown")
		
    elif call.data == "screen_bt":
      screenshot_pc_photo(call.message)


bot.send_message(config.CHAT_ID, text=message_text, reply_markup=keyboard, parse_mode="Markdown")

@bot.message_handler(commands=["sct", "screenshot"])
def screenshot_pc_photo(message):
	filename = f"{time.time()}.jpg"
	pyautogui.screenshot(filename)

	with open(filename, "rb") as img:
		bot.send_photo(message.chat.id, img)
	os.remove(filename)


if __name__ == '__main__':
	bot.polling()