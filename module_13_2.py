
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = '6723713558:AAFU-UHV2KNJNXIc1WTxcwSijS9JmAt2gVI'
bot = Bot(token=api)
dp = Dispatcher(bot=bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user = message.from_user
    print('Привет! Я бот помогающий твоему здоровью.')
    await bot.send_message(chat_id=user.id, text=f'Привет {user.username}! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_massages(message: types.Message):
    user = message.from_user
    print('Введите команду /start, чтобы начать общение.')
    await bot.send_message(chat_id=user.id, text='Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)