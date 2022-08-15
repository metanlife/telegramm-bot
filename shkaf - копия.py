from aiogram.utils import executor
from aiogram.dispatcher.filters  import Text
from aiogram import Bot,types
from aiogram.dispatcher import Dispatcher
import df
from kli import klava
from kli import katal
from base import sqlite
from create_bot import bot, dp
from hea import kupe
from hea import tumboc
from hea import comod
from hea import polki
from hea import proche
from kli import zagr
from kli import udal
import kbvab
import os

ID = 1425016250
sqlite.create_connection()
kupe.register_handles_admin(dp)
tumboc.register_handles_ad(dp)
comod.register_handles_ades(dp)
polki.register_handles_adeses(dp)
proche.register_handles_adesesre(dp)
@dp.message_handler(commands = ["start","help"])
async def command_star(message: types.Message):
	
	await bot.send_message(message.from_user.id,"Работаю по Новосибиркой области",reply_markup=klava.kb_clients)
	await message.delete()
@dp.message_handler(Text(equals = "Каталог\U0001F3E0",ignore_case=True),state = "*")
async def command_open(message: types.Message):
	await bot.send_message(message.from_user.id,"Выбирайте",reply_markup=katal.clien)	
@dp.message_handler(Text(equals = "Вернуться\U000025C0",ignore_case=True),state = "*")
async def command_op(message: types.Message):
	await bot.send_message(message.from_user.id,"Вернуться",reply_markup=klava.kb_clients)
@dp.message_handler(Text(equals = "Поддержка\U0000260E",ignore_case=True),state = "*")
async def command_en(message: types.Message):
	await bot.send_message(message.from_user.id,"\U0000250F Тел. 8-950-296-88-59 \U0001F4F1\n\U00002523 Работаю по заказу\U0001F528\n\U00002517 Связь в теллеграмме @SbiitNoo \U0001F58C")
@dp.message_handler(Text(equals = "Стелажи\U0001F5C4",ignore_case=True),state = "*")	
async def pizza_menu_command(message: types.Message):
	await sqlite.sql_read(message)
@dp.message_handler(Text(equals = "Удалить",ignore_case=True),state = "*")	
async def pizza_menu_command(message: types.Message):
	if message.from_user.id ==ID:
		await bot.send_message(message.from_user.id,"Выбирайте Каталог ",reply_markup=udal.clien)

@dp.message_handler(Text(equals = "Загрузить",ignore_case=True),state = "*")	
async def pizza_menu_command(message: types.Message):
	if message.from_user.id ==ID:
		await bot.send_message(message.from_user.id,"Выбирайте Каталог ",reply_markup=kbvab.clien)
@dp.message_handler(commands = ["moderator"])
async def make_changes_comman(message: types.Message):

	if message.from_user.id == ID :

		await bot.send_message(message.from_user.id, "Что хозяин надо???", reply_markup = zagr.button_case_admin)
		await message.delete()
@dp.message_handler(Text(equals = "Тумбочки",ignore_case=True),state = "*")	
async def pizza_menu_comma(message: types.Message):
	await sqlite.sql_rea(message)

@dp.message_handler(Text(equals = "Комод\U0001F45A",ignore_case=True),state = "*")	
async def pizza_menu_comma(message: types.Message):
	await sqlite.sql_reades(message)

@dp.message_handler(Text(equals = "Полки",ignore_case=True),state = "*")	
async def pizza_menu_comma(message: types.Message):
	await sqlite.sql_readeses(message)
@dp.message_handler(Text(equals = "Прочее\U0001F195",ignore_case=True),state = "*")	
async def pizza_menu_comma(message: types.Message):
	await sqlite.sql_readesesre(message)
async def on_startup(dp):
	await bot.set_webhook(df.URL_APP)
async def on_shutdown(dp):
	await bot.delete_webhook()
	sqlite.cur.close()
	sqlite.base.close()
#executor.start_polling(dp,skip_updates=True)
executor.start_webhook(dispatcher =dp, webhook_path ="",on_startup=on_startup,on_shutdown=on_shutdown,skip_updates=True,host="0.0.0.0",port=int(os.environ.get("PORT",5000)))