from aiogram import Bot, Dispatcher, executor, types
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, ReplyKeyboardRemove, InlineKeyboardButton,InlineKeyboardMarkup

from others.tokenns import TOKEN_API

bot = Bot(TOKEN_API)
dp = Dispatcher(bot)

kb = ReplyKeyboardMarkup(resize_keyboard=True, one_time_keyboard=True) # !

button_1 = KeyboardButton('/help')
button_2 = KeyboardButton('/photomeow')
button_3 = KeyboardButton('/location')
button_4 = KeyboardButton("❤️💋❤️")
button_5 = KeyboardButton("/usemeplease")
kb.add(button_1).add(button_2).add(button_3).add(button_4).add(button_5)


ikb = InlineKeyboardMarkup(row_width=2)
ib_1 = InlineKeyboardButton(text="Button 1", url="https://wotpack.ru/slivy-genshin-impact-3-5-data-vyhoda-bannery-i-personazhi/")
ib_2 = InlineKeyboardButton(text="Button 2", url="https://dtf.ru/s/gachahell/801821-statistika-vypadeniya-garantov-v-genshin-impact-na-osnove-bolee-24-millionov-rollov")
ikb.add(ib_1, ib_2)


HELP_COMMAND = """
<b>/help</b> - <em>список команд</em>
<b>/start</b> - <em>старт бота</em>
<b>/photomeow</b> - <em>фото</em>
<b>/location</b> - <em>локация бота</em>
<b>/ucantrustme</b> - <em> геншин ворлд </em>
"""

@dp.message_handler(commands=["help"])
async def help_command(message: types.Message):
    await bot.send_message(chat_id=message.chat.id,text=HELP_COMMAND, parse_mode="HTML")
    await message.delete()

@dp.message_handler(commands=["photomeow"])
async def send_image(message: types.Message):
    await bot.send_photo(chat_id=message.chat.id, photo="https://sun9-west.userapi.com/sun9-67/s/v1/ig2/vyk44mDbAJoJNwP5wYHmHc8Tx4KffNcVoGl8V-PIKqOMozCYyBTqISxw85JuJApEQQxTon_z8KL9F3oTzK0EILGa.jpg?size=1080x772&quality=95&type=album")
    await message.delete()

@dp.message_handler(commands=['start'])
async def send_message_start(message: types.Message):
    await message.answer("<em>Не трогай меня, человек противный!!!</em> ", parse_mode="HTML", )
    await bot.send_sticker(chat_id=message.chat.id, sticker="CAACAgIAAxkBAAEHWRljyZVXMC98TzPrmJowQKAO1DzEdgACXhYAAot0KUhtLN6g8e7wVy0E", reply_markup=kb)
    await message.delete()


@dp.message_handler(commands=['location'])
async def send_location_mew(message: types.Message):
    await message.answer("Что я тут забыл ###@#$$#@ $#%#@$%!?")
    await bot.send_location(chat_id=message.chat.id,latitude=45, longitude=60)
    await message.delete()

@dp.message_handler()
async def send_cat(message: types.Message):
    if message.text == "❤️💋❤️":
        await bot.send_sticker(chat_id=message.chat.id, sticker="CAACAgIAAxkBAAEHWThjyaOznayhb3hZovWiGNqp_F7L9wACegADXy9bEUMl6MSh12h7LQQ")


@dp.message_handler(commands=["usemeplease"])
async def send_u_cant_trust(message: types.Message):
    await bot.send_message(chat_id=message.chat.id, text="Genshin World", reply_markup=ikb)
    await message.delete()

if __name__ == "__main__":
    executor.start_polling(dp, skip_updates=True)



