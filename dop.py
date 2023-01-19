# from aiogram import Bot, Dispatcher, executor, types
#
# TOKEN_API = "5762475748:AAFpOLa2Uki_RhnF_yMyNwcKj1zX0l_T9rk"
#
# bot = Bot(TOKEN_API)
# dp = Dispatcher(bot)
#
#
# @dp.message_handler()
# async def echo(message: types.Message):
#     if message.text.count(" ") >= 1:
#         await message.answer(text=message.text.upper())  # написать сообщение
#
#
# if __name__ == "__main__":
#     executor.start_polling(dp)
# ----------
# from aiogram import Bot, Dispatcher, executor, types
#
# HELP_COMMAND = """
# /help - список команд
# /start - начать работу с ботом
# """
#
#
# TOKEN_API = "5762475748:AAFpOLa2Uki_RhnF_yMyNwcKj1zX0l_T9rk"
#
# bot = Bot(TOKEN_API)
# dp = Dispatcher(bot)
#
#
# @dp.message_handler(commands=["help"])
# async def help_command(message: types.Message):
#     await message.reply(text=HELP_COMMAND)
#
# @dp.message_handler(commands=["start"])
# async def help_command(message: types.Message):
#     await message.answer(text="Добро пожаловать в мой тг Бот")
#     await  message.delete()
#
#
#
#
# if __name__ == "__main__":
#     executor.start_polling(dp)

# from aiogram import Bot, Dispatcher, executor, types
# import string
# import random
#
# HELP_COMMAND = """
# /help - список команд
# /start - начать работу с ботом
# """
#
#
# TOKEN_API = "5762475748:AAFpOLa2Uki_RhnF_yMyNwcKj1zX0l_T9rk"
#
# bot = Bot(TOKEN_API)
# dp = Dispatcher(bot)
#
# count = 0
#
# @dp.message_handler(commands=["descriprion"])
# async def desc_command(message: types.Message):
#     await message.answer("Данный бот умеет отправлять символы латинского алфовита")
#     await message.delete()
#
# @dp.message_handler(commands=["count"])
# async def check_count(message: types.Message):
#     global count
#     await message.answer(f"COUNT: {count}")
#     count += 1
#
#
# @dp.message_handler()
# async def check_zero(message: types.Message):
#     if "0" in message.text:
#         await message.reply("YES")
#     else:
#         await message.reply("NO")
#
#
# if __name__ == "__main__":
#     executor.start_polling(dp)
# ------
# стикеры и смайлики
# from aiogram import Bot, Dispatcher, executor, types
#
# from others.tokenns import TOKEN_API
#
# bot = Bot(TOKEN_API)
# dp = Dispatcher(bot)
#
# async def on_startup(_):
#     print("Бот успешно запущен!")
#
#
# @dp.message_handler(text=["привет"])
# async def start_command(message: types.Message):
#     await message.answer("<em>Привет, <b>добро пожаловаться,</b> это мой котобот!</em>", parse_mode="HTML")
#     await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEHVy5jyVDEkqrulYMBpRF8D9cfXln6_QACVhAAAno-KEjC9YOg8ncweS0E")
#     await message.delete()
# @dp.message_handler(commands=["give"])
# async def start_command(message: types.Message):
#     await bot.send_sticker(message.from_user.id, sticker="CAACAgIAAxkBAAEHVzxjyVHuR4fNjT7VGPYgatn9B_iO8wACJhsAAu6sAAFKlJHRa9KsunQtBA")
#     await message.delete()
#
#
# @dp.message_handler()
# async def send_emoji(message: types.Message):
#     await message.reply(message.text + "❤️")
#
#
# if __name__ == "__main__":
#     executor.start_polling(dp, on_startup=on_startup)
# -------------------------
#
# from aiogram import Bot, Dispatcher, executor, types
#
# from others.tokenns import TOKEN_API
#
# bot = Bot(TOKEN_API)
# dp = Dispatcher(bot)
#
# HELP_COMMAND = """
# <b>/start</b> - <em>начало нашей работы</em>
# <b>/help</b> - <em>начало нашей работы</em>
# <b>/photomeow</b> - <em>начало нашей работы</em>
# <b>/location</b> - <em>начало нашей работы</em>
# """
# @dp.message_handler(commands=["help"])
# async def help_command(message: types.Message):
#     await bot.send_message(chat_id=message.chat.id,text=HELP_COMMAND, parse_mode="HTML")
#     await message.delete()
#
# @dp.message_handler(commands=["photomeow"])
# async def send_image(message: types.Message):
#     await bot.send_photo(chat_id=message.chat.id, photo="https://sun9-west.userapi.com/sun9-67/s/v1/ig2/vyk44mDbAJoJNwP5wYHmHc8Tx4KffNcVoGl8V-PIKqOMozCYyBTqISxw85JuJApEQQxTon_z8KL9F3oTzK0EILGa.jpg?size=1080x772&quality=95&type=album")
#     await message.delete()
#
# @dp.message_handler(commands=['start'])
# async def send_message_start(message: types.Message):
#     await message.answer("<em>Не трогай меня, человек противный!!!</em> ", parse_mode="HTML", )
#     await bot.send_sticker(chat_id=message.chat.id, sticker="CAACAgIAAxkBAAEHWRljyZVXMC98TzPrmJowQKAO1DzEdgACXhYAAot0KUhtLN6g8e7wVy0E")
#     await message.delete()
#
#
# @dp.message_handler(commands=['location'])
# async def send_location_mew(message: types.Message):
#     await message.answer("Что я тут забыл ###@#$$#@ $#%#@$%!")
#     await bot.send_location(chat_id=message.chat.id,latitude=93, longitude=84)
#     await message.delete()
#
#
#
# if __name__ == "__main__":
#     executor.start_polling(dp, skip_updates=True)
# ---------- keyboar ( клавиатура ( кнопки ))