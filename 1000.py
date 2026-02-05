from aiogram import Bot, Dispatcher, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
import asyncio


# 1. Инициализация
TOKEN = "8515542601:AAGJ2esKq5F1Kf12bZKOC96P07GtwD6xHqg"  #

bot = Bot(token=TOKEN)
dp = Dispatcher()
router = Router()


# 2. Обработчик команды /start
@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(
        " Добро пожаловать в школу борьбы!\n\n"
        "Я помогу вам записаться на пробное занятие.\n\n"
        " Для регистрации напишите:\n"
        "1. Ваше ФИО (полностью)\n"
        "2. Время ( 10:00, 12:00, 14:00, 16:00, 20:00, 21:30)\n\n"
        "Пример сообщения:\n"
        "Иванов Иван Иванович, 14:00")
# 3. Обработчик всех сообщений
@router.message()
async def handle_message(message: Message):
    user_text = message.text.strip()
    if "," in user_text:

        parts = user_text.split(",", 1)
        if len(parts) == 2:
            fio = parts[0].strip()
            time = parts[1].strip()
            if len(fio) < 5:
                await message.answer(
                    " ФИО слишком короткое. Пожалуйста, напишите полное ФИО.\n"
                    "Пример: Иванов Иван Иванович, 14:00")
                return
            valid_times = ["09:00", "12:00", "14:00", "16:00", "20:00", "21:30"]
            if time not in valid_times:
                await message.answer(
                    f" Неверное время, Доступные варианты:\n"
                    f"{', '.join(valid_times)}\n\n"
                    f"Пример: {fio}, 14:00"
                )
                return
            confirmation_text = (
                f" Вы успешно записались на пробное занятие!\n\n"
                f" ФИО: {fio}\n"
                f" Время: {time}\n"
                f" Занятие: Пробное занятие по борьбе\n\n"
                f" Адрес: ул. Спортивная, 15\n"
                f" Дата: завтра\n\n"
                f"Пожалуйста, не опаздывайте!\n"
                f"Приходите за 10-15 минут до начала.\n\n"
                f" По вопросам: +7 000 000 00 00\n\n"
                f"Для новой записи напишите /start")
            await message.answer(confirmation_text)
            print(f" Новая запись: {fio} на {time}")
        else:
            await message.answer(
                " Неверный формат. Используйте запятую для разделения.\n"
                "Пример: Иванов Иван Иванович, 14:00")

    else:
        await message.answer(
            "Для записи на пробное занятие напишите:\n"
            "1. Ваше ФИО\n"
            "2. Удобное время\n\n"
            "Формат: ФИО, время\n"
            "Пример: Иванов Иван Иванович, 14:00\n\n"
            "Доступные времена: 10:00, 12:00, 14:00, 16:00, 18:00, 20:00\n\n"
            "Для начала напишите /start"
        )

# 4. Запуск бота
async def main():
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    print("Бот школы борьбы запущен...")
    asyncio.run(main())