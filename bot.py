from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton
import os
#import library


bot = Bot(token='') #token bot
dp = Dispatcher(bot)

shutdown_button = KeyboardButton('shutdown') #shutdown button
reboot_button = KeyboardButton('reboot') #reboot button
disconnect_button = KeyboardButton('disconnect') #disconnect button

keyboard = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True).add(shutdown_button).add(reboot_button).add(disconnect_button)

authorized = None #set authorization

@dp.message_handler(commands=['start']) #if message == /start
async def welcome(message: types.Message):
    global authorized
    if str(message.from_id) == "": #write self telegram id, so you can only use it
        authorized = True #set authorization on True
        await message.reply("hi!", reply_markup=keyboard) #reply_markup=keyboard is for making the button appear
    else:
        authorized = False #set authorization on False if other person try to use this bot

    

@dp.message_handler()
async def response(message: types.Message):

    if authorized: 

        if message.text.lower() == "shutdown":  #command for shutdown pc
                try:
                    os.system("shutdown /p")
                except:
                    await message.reply("error during process")
            
        elif message.text.lower() == "reboot":  #command for reboot pc
                try:
                    os.system("shutdown /r")
                except:
                    await message.reply("error during process")

        elif message.text.lower() == "disconnect":  #command for disconnect pc
            try:
                os.system("shutdown /f")
            except:
                await message.reply("error during process")

    else:
        await message.reply("you are not authorized")

try:
    executor.start_polling(dp)
except:
    print("[ERROR] error during start-up bot")

