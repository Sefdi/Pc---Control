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
import pyautogui
import subprocess
import g4f
from g4f import ChatCompletion
import psutil

#---------------------------------------
# Дизайн

diz1 = '┌'
diz2 = '├'
diz3 = '└'
diz4 = '×'
diz5 = '⠀'

#---------------------------------------

hostname = socket.gethostname()
colorama.init()

# Получаем текущую дату и время
now = datetime.datetime.now()

bot = telebot.TeleBot(config.TOKEN)

message_text = (
    f"{diz1} 🖥 {diz4} Статус компьютера: `Включён`\n"
    f"{diz2} ☄ {diz4} Название ПК: `{hostname}` \n"
    f"{diz3} 📃 {diz4} Тип отправки: `Shell Start Up` \n"
     f"							      ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ \n"
    f"{diz1} ⏰ {diz4} Время включения: `{now.strftime('%H:%M')}`\n"
    f"{diz3} 📅 {diz4} Дата включения: `{now.strftime('%Y-%m-%d')} \n`"
    f"							      ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ \n"
    "        `PCStatus | Sefd1Relax | v5 | ChatGPT-4`"
)



keyboard = telebot.types.InlineKeyboardMarkup()
button = telebot.types.InlineKeyboardButton(text="Выключить компьютер", callback_data="shutdown_computer")
button2 = telebot.types.InlineKeyboardButton(text="Перезагрузить компьютер", callback_data="restart_computer")
status_bt = telebot.types.InlineKeyboardButton(text="Узнать статус", callback_data="status_for_pc")
screen_bt = telebot.types.InlineKeyboardButton(text="Скриншот", callback_data="screen_bt")
menu_bt = telebot.types.InlineKeyboardButton(text="Меню", callback_data="menu_bt")
keyboard.add(button)
keyboard.add(button2)
keyboard.add(status_bt)
keyboard.add(screen_bt)
keyboard.add(menu_bt)

# Обработчик нажатия на кнопку
# Обработчик нажатия на кнопку
@bot.callback_query_handler(func=lambda call: True)
def callback_handler(call):
    if call.data == "shutdown_computer":
        subprocess.run("shutdown /s /t 1", shell=True)
        bot.send_message(call.message.chat.id, f"{diz1} 🖥 {diz4} Статус компьютера: `Выключён`\n"
											   f"{diz2} ☄ {diz4} Название ПК: `{hostname}` \n"
											   f"{diz3} 📃 {diz4} Тип отправки: `Console | Button` \n"
											   f"							      ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ \n"
											   f"{diz1} ⏰ {diz4} Время выключения: `{now.strftime('%H:%M')}`\n"
											   f"{diz3} 📅 {diz4} Дата выключения: `{now.strftime('%Y-%m-%d')} \n`"
											   f"							      ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ \n"
                                               "        `PCStatus | Sefd1Relax | v5 | ChatGPT-4` ", parse_mode="Markdown")
	

    elif call.data == "restart_computer":
        subprocess.run("shutdown /r /t 1", shell=True)
        bot.send_message(call.message.chat.id, f"{diz1} 🖥 {diz4} Статус компьютера: `Перезагрузка`\n"
											   f"{diz2} ☄ {diz4} Название ПК: `{hostname}` \n"
                                                f"{diz3} 📃 {diz4} Тип отправки: `Console | Button` \n"
											   f"							      ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ \n"
											   f"{diz1} ⏰ {diz4} Время перезагрузки: `{now.strftime('%H:%M')}`\n"
											   f"{diz3} 📅 {diz4} Дата перезагрузки: `{now.strftime('%Y-%m-%d')} \n`"
                                               f"							      ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ \n"
                                                "        `PCStatus | Sefd1Relax | v5 | ChatGPT-4` ", parse_mode="Markdown")
    elif call.data == "status_for_pc":
        bot.send_message(call.message.chat.id, f"{diz1} 🖥 {diz4} Статус компьютера: `Включён`\n"
                                               f"{diz2} ☄ {diz4} Название ПК: `{hostname}` \n"
                                               f"{diz3} 📃 {diz4} Тип отправки: `Узнать статус` \n"
                                               f"							      ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ \n"
                                               f"{diz1} ⏰ {diz4} Время включения: `{now.strftime('%H:%M')}`\n"
                                               f"{diz3} 📅 {diz4} Дата включения: `{now.strftime('%Y-%m-%d')} \n`"
                                               f"							      ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ \n"
                                                "        `PCStatus | Sefd1Relax | v5 | ChatGPT-4` ", parse_mode="Markdown")
		
    elif call.data == "screen_bt":
      screenshot_pc_photo(call.message)
      
    elif call.data == "menu_bt":
      bot.send_message(call.message.chat.id, "        `  Список всех команд управления` \n"
                       f"							      ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ \n"
                        "/sct - `Скриншот`     | /pause - `Пауза` \n"
						"`  `\n"
                        "/play - `Запустить` | /shutdown - `Выключить`\n"
						"`  `\n"
						"/restart - `Рестарт` | /status - `Узнать статус`", parse_mode="Markdown")


bot.send_message(config.CHAT_ID, text=message_text, reply_markup=keyboard, parse_mode="Markdown")



@bot.message_handler(func=lambda message: True)
def reply_to_user(message):
    question = message.text

    response = ChatCompletion.create(
        model="gpt-4",
        temperature=0.9,
        max_tokens=1000,
        top_p=1.0,
        frequency_penalty=0.0,
        presence_penalty=0.6,
        stop=["You:"],
        messages=[{"role": "system", "content": ("Ты должен помогать пользователям и отвечать на все вопросы", "Твоё имя - Артем, ты искусственный интелект от Дмитрий Нелова", "Ты должен помогать пользователям")}, {"role": "user", "content": question}]
    )

    bot.reply_to(message, response)



@bot.message_handler(commands=["sct", "screenshot"])
def screenshot_pc_photo(message):
	filename = f"{time.time()}.jpg"
	pyautogui.screenshot(filename)

	with open(filename, "rb") as img:
		bot.send_photo(message.chat.id, img)
	os.remove(filename)

@bot.message_handler(commands =["pause", "play"])
def pause_video(message):
	bot.delete_message(message.chat.id, message.message_id)
	pyautogui.hotkey('space')
     
@bot.message_handler(commands =["next"])
def next_video(message):
	bot.delete_message(message.chat.id, message.message_id)
	pyautogui.hotkey('shift', 'n')

@bot.message_handler(commands =["previos"])
def nazad_video(message):
	bot.delete_message(message.chat.id, message.message_id)
	pyautogui.hotkey('shift', 'p')
      
@bot.message_handler(commands =["shutdown"])
def shutdown_pc(message):
	bot.delete_message(message.chat.id, message.message_id)
	subprocess.run("shutdown /s /t 1", shell=True)

@bot.message_handler(commands =["restart"])
def restart_pc(message):
	bot.delete_message(message.chat.id, message.message_id)
	subprocess.run("shutdown /r /t 1", shell=True)
	
# Функция для поиска и завершения процесса Discord
def find_and_stop_discord():
        try: 
            # Перебираем все запущенные процессы
            for process in psutil.process_iter(['pid', 'name']):
                # Проверяем, есть ли среди них Discord
                if 'Discord.exe' in process.info['name'].lower():
                    print(f"Найден процесс Discord с PID {process.info['pid']}. Завершаем...")
                    # Завершаем процесс
                    psutil.Process(process.info['pid']).terminate()
                    break
            else:
                print("Процесс Discord не найден. Ничего не делаем.")

        except Exception as e:
              print(e)


@bot.message_handler(commands = ["panic"])
def panic_fun(message):
	bot.delete_message(message.chat.id, message.message_id)
	find_and_stop_discord()

@bot.message_handler(commands =["status"])
def pc_status(message):
	bot.delete_message(message.chat.id, message.message_id)

	bot.send_message(message.chat.id, f"{diz1} 🖥 {diz4} Статус компьютера: `Включён`\n"
                                               f"{diz2} ☄ {diz4} Название ПК: `{hostname}` \n"
                                               f"{diz3} 📃 {diz4} Тип отправки: `Узнать статус` \n"
                                               f"							      ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ \n"
                                               f"{diz1} ⏰ {diz4} Время включения: `{now.strftime('%H:%M')}`\n"
                                               f"{diz3} 📅 {diz4} Дата включения: `{now.strftime('%Y-%m-%d')} \n`"
                                               f"							      ⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻⎻ \n"
                                                "        `PCStatus | Sefd1Relax | v4`", parse_mode="Markdown")	

if __name__ == '__main__':
	bot.polling()