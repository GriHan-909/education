from aiogram import Bot, Dispatcher, executor, types
from aiogram.contrib.fsm_storage.memory import MemoryStorage
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

api = '*********'
bot = Bot(token=api)
dp = Dispatcher(bot=bot, storage=MemoryStorage())


kb = ReplyKeyboardMarkup(resize_keyboard=True)
button = KeyboardButton(text = 'Рассчитать')
button_2 = KeyboardButton(text = 'Информация')
kb.add(button, button_2)

inl_kb = InlineKeyboardMarkup()
inl_button = InlineKeyboardButton(text = 'Рассчитать норму калорий', callback_data='calories')
inl_button_2 = InlineKeyboardButton(text= 'Формулы расчета', callback_data='formulas')
inl_kb.add(inl_button, inl_button_2)

class UserState(StatesGroup):
    age = State()
    growth = State()
    weight = State()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    user = message.from_user
    await message.answer(text=f'Привет {user.username}! Я бот помогающий твоему здоровью.', reply_markup=kb)

@dp.message_handler(text ='Рассчитать')
async def main_menu(message: types.Message):
    await message.answer(text='Выберите опцию:', reply_markup=inl_kb)


@dp.callback_query_handler(text ='calories')
async def set_age(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer(text='Введите свой возраст:')
    await UserState.age.set()


@dp.callback_query_handler(text='formulas')
async def get_formulas(call: types.CallbackQuery):
    await call.answer()
    await call.message.answer('10 х вес (кг) + 6,25 x рост (см) – 5 х возраст (г) + 5')


@dp.message_handler(state = UserState.age)
async def set_growth(message, state):
    await state.update_data(age = message.text)
    await message.answer(text='Введите свой рост:')
    await UserState.growth.set()


@dp.message_handler(state=UserState.growth)
async def set_weight(message, state):
    await state.update_data(growth = message.text)
    await message.answer(text='Введите свой вес:')
    await UserState.weight.set()


@dp.message_handler(state=UserState.weight)
async def send_calories(message, state):
    await state.update_data(weight = message.text)
    data = await state.get_data()
    result = 10 * int(data['weight']) + 6.25 * int(data['growth']) - 5 * int(data['age'])
    await state.finish()
    await message.answer(f'Ваша норма каллорий: {result}')

@dp.message_handler()
async def all_massages(message: types.Message):
    await message.answer(text='Введите команду /start, чтобы начать общение.')


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)