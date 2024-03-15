import asyncio
import logging

from aiogram import Bot, Dispatcher, types, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.filters import Command
from aiogram.fsm.state import State, StatesGroup
from keyboards.keyboard import main_menu_keyboard
from get import get_input, get_answers
from states.state import add_tests

bot = Bot(token="6367514984:AAEDe7c8bENFdjYrcnH8bthISh9ulrRKhIM")

dispatcher = Dispatcher()
dp = Router()
dispatcher.include_router(dp)

user_tests = ""

@dp.message(Command("start"))
async def cmd_start(message: types.Message, state: FSMContext):
    await state.clear()
    await message.answer(
        f"Salom, {message.from_user.first_name} 👋\nSiz asosiy menudasiz! 👇",
        reply_markup=main_menu_keyboard,
    )


@dp.message(F.text == "➕ add new tests")
async def add_test(msg: types.Message, state: FSMContext):
    await msg.answer("Testlarni yuboring.")
    await state.set_state(add_tests . get_tests)

@dp.message(add_tests.get_tests)
async def getting(msg: types.Message, state: FSMContext):
    s = msg.text
    s = s.replace('\n', " ")
    await state.update_data(get_tests = s)
    await msg.answer("Testlar muvaffaqiyatli saqlandi.", reply_markup=main_menu_keyboard)
    await state.set_state(add_tests.get_numbers)

@dp.message(F.text == "🎲 get random tests")
async def random_tests(msg: types.Message, state: FSMContext):
    await msg.answer(f"Sizga kerakli bo'lgan testlar sonini kiriting.")
    await state.set_state(add_tests.get_numbers)

@dp.message(add_tests.get_numbers)
async def fsjrogs(msg: types.Message, state: FSMContext):
    await state.update_data(get_numbers = msg.text)
    await msg.answer("Yuqorida berilgan testlaringizning javoblarini kiriting. E'tibor bering javoblar soni va testlar soni teng bo'lishi shart!")
    await state.set_state(add_tests.get_answers)
    
@dp.message(add_tests.get_answers)
async def fbdbdf(msg: types.Message, state: FSMContext):
    k = True
    inp = msg.text
    for i in inp:
        if ord("A") <= ord(i)<=ord("H"):
            continue
        else:
            k = False
    if k:
        await state.update_data(get_answers = msg.text)
        data = await state.get_data()
        
        ans = get_answers(f"{data['get_tests']}", data['get_answers'],len(data['get_tests']),data['get_numbers'])
        if ans[1] != len(data['get_answers']):
            print(ans[1], len(data['get_answers']))
            await msg.answer("Testlar soni va javoblar soni mos kelmadi. Qaytadan urinib ko'ring.")
            await state.set_state(add_tests.get_answers)
        else:
            await msg.answer(ans[0])
    else: 
        await msg.answer("Siz noto'g'ri ma'lumot yubordingiz! Qaytadan urinib ko'ring.")
@dp.message()
async def any_word(msg: types.message):
    await msg.answer(f"Siz noto'g'ri buyruq yubordingiz !")

async def main():
    await dispatcher.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())
