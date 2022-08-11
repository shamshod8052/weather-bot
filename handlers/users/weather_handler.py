from aiogram import types
from aiogram.dispatcher.filters.builtin import CommandStart

from geopy.geocoders import Nominatim
from keyboards.default.menu import menu, viloyat
from loader import dp
from handlers.users.weather import weather

geolocator = Nominatim(user_agent="geoapiExercises")

@dp.message_handler(text="Viloyat")
async def bot_start(message: types.Message):
    await message.answer("Viloyat", reply_markup=viloyat)

@dp.message_handler(content_types='location')
async def bot_start(message: types.Message):
    a = message.location.values
    # Latitude & Longitude input
    Latitude = str(a['latitude'])
    Longitude = str(a['longitude'])

    location = str(geolocator.reverse(Latitude + "," + Longitude))
    location = location[location.find(",")+2:]
    location = location[:location.find(" ")]
    # Display
    try:
        await message.answer(weather(location), reply_markup=menu)
    except:
        await message.answer("Xatolik")

@dp.message_handler(content_types='text')
async def bot_start(message: types.Message):
    try:
        await message.answer(weather(message.text), reply_markup=menu)
    except:
        await message.answer("Xatolik")

