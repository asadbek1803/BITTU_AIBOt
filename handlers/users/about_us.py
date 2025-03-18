from aiogram import Router, types
from aiogram.enums.parse_mode import ParseMode
from componets.messages import buttons, messages
from loader import db



router = Router()


channel = [
        [types.InlineKeyboardButton(text="📢 Asosiy kanalimiz", url="https://t.me/bitiinfo")],
        [types.InlineKeyboardButton(text="📍 Manzil", url="https://maps.app.goo.gl/sgxieqiap3WgENn58")],
        [types.InlineKeyboardButton(text="📷 Instagram", url="https://www.instagram.com/biti_uz/")],
        [types.InlineKeyboardButton(text="🎥 YouTube", url="https://www.youtube.com/channel/UCTulr3Diu5ic6ay42DdOI1A")]
        
    ]
channel_markup = types.InlineKeyboardMarkup(inline_keyboard=channel)


@router.message(lambda message: message.text == buttons["uz"]["btn_aboutus"] or
                       message.text == buttons["tr"]["btn_aboutus"])
async def handle_about_center(message: types.Message):
    """Handle information requests about Turan Education Center"""
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
