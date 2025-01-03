from aiogram import Bot, Dispatcher, F
from aiogram.filters import Command
from aiogram.types import Message

#from aiogram.types import ContentType

# токен бота
BOT_TOKEN = '7908331579:AAHlhpRW4Ui_kY_KfSAnT-B3XFVfMhi--Kk'

# Создаем объекты бота и диспетчера
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

# Этот хэндлер будет срабатывать на команду "/start"
async def process_start_command(message: Message):
    await message.answer('Привет\nМеня зовут Эхо-бот!\nПопробуй что-нибудь мне написать!')

# Этот хэндлер будет срабатывать на команду "/help"
async def process_help_command(message: Message):
    await message.answer('Напиши мне любое сообщение, а я отправлю тебе его в ответ!')

# Этот хэндлер будет срабатывать на голосовые сообщения
'''@dp.message(F.voice)
async def process_sent_voice(message: Message):
    #выводим апдейт в терминал
    print(message)
    #отправляем сообщение в чат откуда пришло сообщение
    await message.answer(text="Вы прислали голосовое сообщение")'''

# Этот хэндлер будет срабатывать на отправку боту фото
async def send_photo_echo(message: Message):
    print(message)
    await message.answer('Вы прислали фото!')

# Этот хэндлер будет срабатывать на любые ваши текстовые сообщения,
# кроме команд "/start" и "/help"
async def send_echo(message: Message):
    await message.answer('Вы прислали текстовое сообщение!')



# Регистрируем хэндлеры
dp.message.register(process_start_command, Command(commands='start'))
dp.message.register(process_help_command, Command(commands='help'))
dp.message.register(send_photo_echo, F.photo)
dp.message.register(send_echo)

if __name__ == '__main__':
    dp.run_polling(bot)