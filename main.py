from config import TOKEN, APIKEY
import asyncio
from aiogram import Bot, Dispatcher
from aiogram.filters import CommandStart, Command
from aiogram.types import Message
import requests

bot = Bot(token=TOKEN)
dp = Dispatcher()
@dp.message(Command('help'))
async def help(message: Message):
    await message.answer("Этот бот умеет выполнять команды:\n/start\n/help\n/Weather")

@dp.message(Command('Weather'))
async def help(message: Message):
    weather = get_weather('Kursk')
    await message.answer("Погода в городе Курск "+ str(weather['main']['temp'])+"°C\n"+str(weather['weather'][0]['description']))

@dp.message(CommandStart())
async def start(message: Message):
    await message.answer("Приветики, я бот!")

async def main():
    await dp.start_polling(bot)

def get_weather(city):
   api_key = APIKEY
   #адрес, по которомы мы будем отправлять запрос. Не забываем указывать f строку.
   url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&lang=ru&units=metric"
   #для получения результата нам понадобится модуль requests
   response = requests.get(url)
   #прописываем формат возврата результата
   return response.json()

if __name__ == "__main__":
    asyncio.run(main())


    # { % if weather %}
    # < h3 > Погода
    # в
    # {{weather['name']}} < / h3 >
    # < p > Температура: {{weather['main']['temp']}}°C < / p >
    # < p > Погода: {{weather['weather'][0]['description']}} < / p >
