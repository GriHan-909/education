
from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage

api = '**********************************************'
bot = Bot(token=api)
dp = Dispatcher(bot=bot, storage=MemoryStorage())

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user = message.from_user
    print('Привет! Я бот помогающий твоему здоровью.')
    await message.answer(text=f'Привет {user.username}! Я бот помогающий твоему здоровью.')

@dp.message_handler()
async def all_massages(message: types.Message):    
    print('Введите команду /start, чтобы начать общение.')
    await message.answer(text='Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
