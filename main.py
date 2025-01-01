from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message

# токен бота
BOT_TOKEN = '7908331579:AAHlhpRW4Ui_kY_KfSAnT-B3XFVfMhi--Kk'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
@dp.message(Command(commands=["start"]))
async def process_start_command(message: Message):
    await message.answer('Привет\nМеня зовут Эхо-бот!\nПопробуй что-нибудь мне написать!')

# Этот хэндлер будет срабатывать на команду "/help"
@dp.message(Command(commands=["help"]))
async def process_help_command(message: Message):
    await message.answer('Напиши мне любое сообщение, а я отправлю тебе его в ответ!')

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
@dp.message()
async def send_echo(message: Message):
    await message.reply(text=message.text)

if __name__ == '__main__':
    dp.run_polling(bot)