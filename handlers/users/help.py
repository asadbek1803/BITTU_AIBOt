from aiogram import Router, types
from aiogram.filters.command import Command
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
router = Router()


@router.message(Command('help'))
async def bot_help(message: types.Message):
    channel = [
         [types.InlineKeyboardButton(text="📢 Asosiy kanalimiz", url="https://t.me/bitiinfo")],
        [types.InlineKeyboardButton(text="📍 Manzil", url="https://maps.app.goo.gl/sgxieqiap3WgENn58")],
        [types.InlineKeyboardButton(text="📷 Instagram", url="https://www.instagram.com/biti_uz/")],
        [types.InlineKeyboardButton(text="🎥 YouTube", url="https://www.youtube.com/channel/UCTulr3Diu5ic6ay42DdOI1A")]
    ]
    channel_markup = InlineKeyboardMarkup(inline_keyboard=channel)
    text = ("Bot haqida: ",
            "Ushbu bot BITTU <b> Universitedi </b> uchun maxsus yaratilgan AI Suniy Intelekt botidir. Bunda siz o'qish uchun ham ro'yxatdan o'tishingiz mumkin, hamda universitet haqida ma'lumot olishingiz mumkin. ",
            "Bot kommandalari: ",
            "/start - 🔄️ Botni ishga tushirish",
            "/change_language - 🌐 Tilni o'zgartirish",
            "/chat - 🤖 Yangi chat", 
            "/chat - ❌ Chatni to'xtatish",
            "Bizning ijtimoiy tarmoqlarga obuna bo'lishni unutmang ;) "
            )
    await message.answer(text="\n".join(text), reply_markup=channel_markup)
