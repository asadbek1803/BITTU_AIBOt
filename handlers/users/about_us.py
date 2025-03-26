from aiogram import Router, types
from aiogram.enums.parse_mode import ParseMode
from componets.messages import buttons, messages
from loader import db



router = Router()


menu_about = [
        [types.InlineKeyboardButton(text="💰 GRANT-GPA", callback_data="grant")],
        [types.InlineKeyboardButton(text="👉 Yo'nalishlar", callback_data="directions")],
        [types.InlineKeyboardButton(text="👉 Abituryentlar uchun", callback_data="for_students")],
        [types.InlineKeyboardButton(text="📚 BITUning afzalliklari", callback_data="advantages")],
        [types.InlineKeyboardButton(text="📌Manzil📌", callback_data="address")],
        [types.InlineKeyboardButton(text="📞Aloqa📞", callback_data="contact")],
        [types.InlineKeyboardButton(text="↩️Qaytish↩️", callback_data="to_home")],
        ]

channel_markup = types.InlineKeyboardMarkup(inline_keyboard=menu_about)


@router.message(lambda message: message.text == buttons["uz"]["btn_aboutus"] or
                       message.text == buttons["tr"]["btn_aboutus"])
async def handle_about_center(message: types.Message):
    """Handle information requests about BITU"""
    telegram_id = message.from_user.id
    user = await db.select_user(telegram_id=telegram_id)
    language = user["language"] if user else "uz"
    
    about_text = {
        "uz": (
            "<b>BUXORO INNOVATSION TEXNOLOGIYALAR UNIVERSITETI</b>\n\n"
            "<b>📚 BITUning afzalliklari:</b>\n"
            "✅ A'lochi bitiruvchilarni ish bilan ta'minlashga ko'maklashamiz\n"
            "✅ Buxorodagi eng yirik sig'imli (1000 kishilik) Faollar zali mavjud\n"
            "✅ Dars jarayonida simulyatorlardan foydalaniladi\n"
            "✅ Yangicha o'quv tizimi yo'lga qo'yilgan bo'lib darslar Koreya, Hindiston, Rossiya, Germaniya kabi davlatlarda tajriba orttirib kelgan mutaxassislar tomonidan olib boriladi\n"
            "✅ O'quv mashg'ulotlari haftada 5 kunlik rejim asosida o'tkaziladi\n"
            "✅ Davlat namunasidagi diplom bilan ta'minlanadi\n"
            "✅ 1-Kursdanoq ishlash imkoniyati mavjud\n"
            "✅ Shifokorlarning farzandlariga kirish imtihonlarida imtiyozlar mavjud\n\n"
            "📞 <b>Murojaat uchun:</b> +998652205545\n"
            "🌐 <b>Web-sayt:</b> www.bimu.uz\n"
            "📍 <b>Manzil:</b> Buxoro shahri, Namozgoh ko'chasi, 112"
        ),
        "tr": (
            "<b>BUHARA YENİLİKÇİ TEKNOLOJİLER ÜNİVERSİTESİ</b>\n\n"
            "<b>📚 BITU'nun avantajları:</b>\n"
            "✅ Başarılı mezunların istihdamına yardımcı oluyoruz\n"
            "✅ Buhara'daki en büyük (1000 kişilik) Konferans Salonu\n"
            "✅ Derslerde simülatörler kullanılmaktadır\n"
            "✅ Kore, Hindistan, Rusya, Almanya gibi ülkelerde deneyim kazanmış uzmanlar tarafından yeni eğitim sistemi uygulanmaktadır\n"
            "✅ Dersler haftada 5 gün yapılmaktadır\n"
            "✅ Devlet onaylı diploma verilmektedir\n"
            "✅ 1. sınıftan itibaren çalışma imkanı\n"
            "✅ Doktor çocuklarına giriş sınavlarında ayrıcalıklar\n\n"
            "📞 <b>İletişim:</b> +998652205545\n"
            "🌐 <b>Web sitesi:</b> www.bimu.uz\n"
            "📍 <b>Adres:</b> Buhara şehri, Namozgoh caddesi, 112"
        )
    }
    video_url = "https://t.me/bitiinfo/1607"
    await message.answer_photo(
        photo=video_url,
        caption=about_text.get(language, about_text["uz"]),
        parse_mode=ParseMode.HTML,
        reply_markup=channel_markup
    )

@router.callback_query(lambda c: c.data == "grant")
async def grant_handler(callback: types.CallbackQuery):
    user = await db.select_user(telegram_id=callback.from_user.id)
    language = user["language"] if user else "uz"
    video_url = "https://t.me/turan_mediafiles/8"
    grant_text = {
        "uz": "888 ta GRANTDAN 1tasi sizniki bo'lishi mumkin!\nImkoniyatni qo'ldan boy bermang!\n\n"
              "✅ Davolash ishi — 192 ta GRANT\n"
              "✅ Stomatologiya — 72 ta GRANT\n"
              "✅ Psixologiya/Iqtisodiyot/Boshlang'ich ta'lim — 360 ta GRANT\n"
              "✅ Ingliz/Rus/O'zbek Tili — 264 ta GRANT",
        "tr": "888 BURS'tan 1'i sizin olabilir!\nBu fırsatı kaçırmayın!\n\n"
              "✅ Tıp — 192 BURS\n"
              "✅ Diş Hekimliği — 72 BURS\n"
              "✅ Psikoloji/Ekonomi/İlköğretim — 360 BURS\n"
              "✅ İngilizce/Rusça/Özbekçe — 264 BURS"
    }
    await callback.message.answer_video(
        video=video_url,
        caption = grant_text[language], 
        reply_markup=channel_markup)
    
@router.callback_query(lambda c: c.data == "directions")
async def directions_handler(callback: types.CallbackQuery):
    user = await db.select_user(telegram_id=callback.from_user.id)
    language = user["language"] if user else "uz"
    
    directions_buttons = [
        [types.InlineKeyboardButton(text="Davolash ishi", callback_data="med")],
        [types.InlineKeyboardButton(text="Stomatologiya", callback_data="stom")],
        [types.InlineKeyboardButton(text="Sirtqi yo'nalishlar", callback_data="distance")],
        [types.InlineKeyboardButton(text="Kunduzgi yo'nalishlar", callback_data="daytime")],
        [types.InlineKeyboardButton(text="Filologiya yo'nalishlar", callback_data="filology")],
        [types.InlineKeyboardButton(text="↩️Qaytish↩️", callback_data="to_home")]
    ]
    directions_markup = types.InlineKeyboardMarkup(inline_keyboard=directions_buttons)
    
    directions_text = {
        "uz": "BITUdagi mavjud yo'nalishlar bilan tanishing:",
        "tr": "BITU'daki mevcut bölümleri inceleyin:"
    }
    await callback.message.answer(directions_text[language], reply_markup=directions_markup)

@router.callback_query(lambda c: c.data == "med")
async def med_handler(callback: types.CallbackQuery):
    text = ("Davolash ishi\n\n"
            "O'qish muddati: 6 yil\n\n"
            "O'qish to'lovi: 32 340 000 so'm\n"
            "Bo'lib to'lash imkoniyati mavjud\n\n"
            "100 % to'lov qilib BONUS oling!\n\n"
            "1-Avgustgacha to'lov qilsangiz: 22 340 000 so'm\n\n"
            "1-Sentabrgacha to'lov qilsangiz: 25 340 000 so'm\n\n" 
            "1-Oktabrgacha to'lov qilsangiz: 27 340 000 so'm\n\n"
            "Shoshiling o'rinlar soni cheklangan!")
    await callback.message.answer(text, reply_markup=channel_markup)

@router.callback_query(lambda c: c.data == "stom") 
async def stom_handler(callback: types.CallbackQuery):
    text = ("Stomatologiya\n\n"
            "O'qish muddati: 5 yil\n\n"
            "O'qish to'lovi: 32 340 000 so'm\n"
            "Bo'lib to'lash imkoniyati mavjud\n\n"
            "100 % to'lov qilib BONUS oling!\n\n"
            "1-Avgustgacha to'lov qilsangiz: 22 340 000 so'm\n\n"
            "1-Sentabrgacha to'lov qilsangiz: 25 340 000 so'm\n\n"
            "1-Oktabrgacha to'lov qilsangiz: 27 340 000 so'm")
    await callback.message.answer(text, reply_markup=channel_markup)

@router.callback_query(lambda c: c.data == "distance")
async def distance_handler(callback: types.CallbackQuery):
    text = ("SIRTQI Yo'nalishlar\n\n"
            "- IQTISODIYOT\n"
            "- PSIXOLOGIYA\n" 
            "- BOSHLANG'ICH Ta'lim\n\n"
            "O'qish Muddati: 5 yil\n"
            "O'qish narxi: 6 000 000 so'm")
    await callback.message.answer(text, reply_markup=channel_markup)

@router.callback_query(lambda c: c.data == "filology")
async def filology_handler(callback: types.CallbackQuery):
    text = ("Tillar Yo'nalishi\n\n"
            "- Ingliz Tili Filologiyasi\n"
            "- Nemis Tili Filologiyasi\n"
            "- Rus tili Filologiyasi\n"
            "- O'zbek tili Filologiyasi\n\n"
            "O'qish Muddati: 4 yil\n\n"
            "O'qish narxi: 12 000 000 so'm\n\n"
            "Bo'lib to'lash imkoniyati mavjud")
    await callback.message.answer(text, reply_markup=channel_markup)

@router.callback_query(lambda c: c.data == "for_students")
async def students_handler(callback: types.CallbackQuery):
    user = await db.select_user(telegram_id=callback.from_user.id)
    language = user["language"] if user else "uz"
    
    students_text = {
        "uz": "Bu bo'lim xali tamirda ⚠️.",
        "tr": "Bu bo'lim xali tamirda ⚠️."
    }
    await callback.message.answer(students_text[language], reply_markup=channel_markup)

@router.callback_query(lambda c: c.data == "advantages")
async def advantages_handler(callback: types.CallbackQuery):
    user = await db.select_user(telegram_id=callback.from_user.id)
    language = user["language"] if user else "uz"
    
    advantages_text = {
        "uz": "Bu bo'lim xali tamirda ⚠️..",
        "tr": "Bu bo'lim xali tamirda ⚠️."
    }
    await callback.message.answer(advantages_text[language], reply_markup=channel_markup)

@router.callback_query(lambda c: c.data == "address")
async def address_handler(callback: types.CallbackQuery):
    user = await db.select_user(telegram_id=callback.from_user.id)
    language = user["language"] if user else "uz"
    
    address_text = {
        "uz": "Manzil: Buxoro shahri, Namozgoh ko'chasi, 112",
        "tr": "Adres: Buhara şehri, Namozgoh caddesi, 112"
    }
    await callback.message.answer(address_text[language], reply_markup=channel_markup)

@router.callback_query(lambda c: c.data == "contact")
async def contact_handler(callback: types.CallbackQuery):
    user = await db.select_user(telegram_id=callback.from_user.id)
    language = user["language"] if user else "uz"
    
    contact_text = {
        "uz": "Telefon: +998652205545\nWeb-sayt: www.bimu.uz",
        "tr": "Telefon: +998652205545\nWeb sitesi: www.bimu.uz"
    }
    await callback.message.answer(contact_text[language], reply_markup=channel_markup)

@router.callback_query(lambda c: c.data == "to_home")
async def home_handler(callback: types.CallbackQuery):
    user = await db.select_user(telegram_id=callback.from_user.id)
    language = user["language"] if user else "uz"
    
    home_text = {
        "uz": "Asosiy menyu",
        "tr": "Ana menü"
    }
    await callback.message.answer(home_text[language], reply_markup=channel_markup)
