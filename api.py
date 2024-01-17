from telegram.ext import CommandHandler,Filters,MessageHandler,Updater,ConversationHandler,CallbackQueryHandler
from bs4 import BeautifulSoup as BS
from telegram import KeyboardButton,ReplyKeyboardMarkup
from telegram import InlineKeyboardMarkup,InlineKeyboardButton
import requests


tokenn = "6442886640:AAEInghIZw9D8E2uezOtQl8eAvUAa6ftlNo"

api_key = '03431b747b7283c069dc006f080012ae'



def start_hold(update,context):
    update.message.reply_text(text=f"Assalomu aleykum {update.message.from_user.first_name} "
                                   f"{update.message.from_user.last_name} @ahmadjony ning botiga Xush kelibsiz! Shaxringizni tanlang",
                              reply_markup=InlineKeyboardMarkup(menu1()))

def menu1():
    return [
        [InlineKeyboardButton(text="City",callback_data="City")]
    ]
def menu2():
    return [
        [InlineKeyboardButton(text="back",callback_data="City")]
    ]
def menu3():
    return [
        [InlineKeyboardButton(text="back",callback_data="City2")]
    ]
def menu(update,context):
    global data
    global weather_data
    query = update.callback_query
    city = query.data
    base_url = "https://api.openweathermap.org/data/2.5/weather?q={}&appid={}".format(city, api_key)
    response = requests.get(base_url)
    weather_data = response.json()
    tmax1 = weather_data['main']['temp_max']
    tmin1 = weather_data['main']['temp_min']
    tmin = round(tmin1-273.15)
    tmax = round(tmax1-273.15)
    print(tmax, tmin)
    if query.data == "City":
        buttons = [
            [InlineKeyboardButton(text="Farg'ona",callback_data="Farg'ona"),
             InlineKeyboardButton(text="Namangan",callback_data="Namangan")],
            [InlineKeyboardButton(text="Andijon",callback_data="Andijon"),
             InlineKeyboardButton(text="Samarqand",callback_data="Samarqand")],
            [InlineKeyboardButton(text="Buxoro",callback_data="Buxoro"),
             InlineKeyboardButton(text="Surxandaryo",callback_data="Surxandaryo")],
            [InlineKeyboardButton(text="Qashqadaryo",callback_data="Qashqadaryo"),
             InlineKeyboardButton(text="Xorazm",callback_data="Xorazm")],
            [InlineKeyboardButton(text="Toshkent",callback_data="Tashkent"),
             InlineKeyboardButton(text="Jizzax",callback_data="Jizzax")],
            [InlineKeyboardButton(text="Navoiy",callback_data="Navoiy"),
             InlineKeyboardButton(text="Nukus",callback_data="Nukus")],
        ]
        query.message.reply_text(f"Qaysi viloyat haqida malumot kerak bo'lsa Tanlang!!!",
                                 reply_markup=InlineKeyboardMarkup(buttons))
    if query.data == "Farg'ona":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fstatic.wixstatic.com%2Fmedia%2F9bc4fe_b55b6051c93449a1a6279c1ea8ad5b50~mv2.jpg%2Fv1%2Fcrop%2Fx_0%2Cy_20%2Cw_520%2Ch_148%2Ffill%2Fw_620%2Ch_176%2Cal_c%2Clg_1%2Cq_80%2Cenc_auto%2FFarg%27ona%2520hokimligi.jpg&tbnid=UOFw3ce7K6zNKM&vet=12ahUKEwiRvuDO1t2CAxUVJxAIHWygDFUQMygTegQIARBd..i&imgrefurl=https%3A%2F%2Frakhmatillo.wixsite.com%2Ffarsuvoqava&docid=STwsQbwoj1ZXAM&w=620&h=176&q=fargena%20haqida%20malumot&ved=2ahUKEwiRvuDO1t2CAxUVJxAIHWygDFUQMygTegQIARBd",
                                 caption=f"Farg'ona haqida ma'lumot {tmax}°С {tmin}°С",
                                 reply_markup=InlineKeyboardMarkup(menu2()))

    if query.data == "Namangan":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Favatars.mds.yandex.net%2Fget-altay%2F5475658%2F2a0000017d4c31494117fc5c21137eb9bbb5%2FL_height&tbnid=hWNnFo7M9sybdM&vet=12ahUKEwjd4qCMyOGCAxXvEhAIHX3CArYQMygVegQIARBm..i&imgrefurl=https%3A%2F%2Fyandex.uz%2Fmaps%2Forg%2F85187646026%2F&docid=vvUaFINMaQhPpM&w=500&h=375&q=Namangan%20Viloyati%20rasim&ved=2ahUKEwjd4qCMyOGCAxXvEhAIHX3CArYQMygVegQIARBm",
                                  caption=f"Namangan haqida ma'lumot {tmax}°С {tmin}°С ",
                                  reply_markup=InlineKeyboardMarkup(menu2()))
    if query.data == "Andijon":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Flookaside.fbsbx.com%2Flookaside%2Fcrawler%2Fmedia%2F%3Fmedia_id%3D2618523611763301&tbnid=VaLVjNQfLMJ58M&vet=12ahUKEwjjsLjE0-GCAxVtJRAIHUdcDVQQMygIegQIARBZ..i&imgrefurl=https%3A%2F%2Fwww.facebook.com%2FAKTAndijan%2Fphotos%2Fa.1895000420782294%2F2618523611763301%2F%3Ftype%3D3&docid=lZCGmlXJhoHBQM&w=1680&h=1120&q=Andijon%20viloyati%20rasmlari&ved=2ahUKEwjjsLjE0-GCAxVtJRAIHUdcDVQQMygIegQIARBZ",
                                  caption=f"Andijon haqida ma'lumot {tmax}°С {tmin}°С ",
                                  reply_markup=InlineKeyboardMarkup(menu2()))

    if query.data == "Samarqand":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Favatars.mds.yandex.net%2Fget-altay%2F7695774%2F2a000001849ab6e7997da5dc7efe32797fbb%2FL_height&tbnid=Mg5DRv9NUXvefM&vet=12ahUKEwjml7n_1OGCAxVAFhAIHRoPAYcQMygJegQIARBX..i&imgrefurl=https%3A%2F%2Fyandex.uz%2Fmaps%2Forg%2F43093272445%2F&docid=AaDchQcEjzBUEM&w=500&h=333&q=Samarqand%20viloyati%20rasmlari&ved=2ahUKEwjml7n_1OGCAxVAFhAIHRoPAYcQMygJegQIARBX",
                                  caption=f"Samarqand ob-havo haqida ma'lumot {tmax}°С {tmin}°С ",
                                  reply_markup=InlineKeyboardMarkup(menu2()))

    if query.data == "Buxoro":
        query.message.reply_photo(
            f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fuzbekistan.travel%2Fstorage%2Fapp%2Fmedia%2Fnargiza%2Fcropped-images%2Fcropped-images%2Fbuhara-0-0-0-0-1582712008-0-0-0-0-1582712261.jpg&tbnid=GRl6PwWJ4O6HQM&vet=12ahUKEwiSwNrc2OGCAxVoAhAIHSABCMUQMygAegQIARBN..i&imgrefurl=https%3A%2F%2Fuzbekistan.travel%2Fuz%2Fr%2Fbuxoro-viloyati%2F&docid=_MwwmvsIvcCLnM&w=1100&h=824&q=buxoro%20viloyati%20rasmlari&ved=2ahUKEwiSwNrc2OGCAxVoAhAIHSABCMUQMygAegQIARBN",
            caption=f"Buxoro ob-havo haqida ma'lumot {tmax}°С {tmin}°С ",
            reply_markup=InlineKeyboardMarkup(menu2()))
    if query.data == "Surxandaryo":
        query.message.reply_photo(f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fuzbekistan.travel%2Fstorage%2Fapp%2Fmedia%2Fnargiza%2Fcropped-images%2Fcropped-images%2F1-951-190-0-0-1583326384-0-0-0-0-1583326441.jpg&tbnid=8ZZvlEKPUIuNBM&vet=12ahUKEwj73Zn12eGCAxXgERAIHUGRBmMQMygDegQIARBL..i&imgrefurl=https%3A%2F%2Fuzbekistan.travel%2Fuz%2Fr%2Fsurxondaryo-viloyati%2F&docid=2CGQZD3z4KSUEM&w=1100&h=733&q=Surxondaryo%20viloyati%20rasmlari&ved=2ahUKEwj73Zn12eGCAxXgERAIHUGRBmMQMygDegQIARBL",
                                  caption=f"Surxandaryo ob-havo haqida ma'lumot {tmax}°С {tmin}°С ",
                                  reply_markup=InlineKeyboardMarkup(menu2()))
    if query.data == "Qashqadaryo":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fqashqadaryo.uz%2Fimages%2Fgallery%2Fcd229d5eb0c6d4957475a34b11de22c3.jpg&tbnid=wDF-YsG6YQcf7M&vet=12ahUKEwj3_a2e3OGCAxUdPhAIHZlxDVIQMygAegQIARBI..i&imgrefurl=https%3A%2F%2Fqashqadaryo.uz%2Fgallery&docid=vLW6ACOFTfhpyM&w=1280&h=853&q=Qashqadaryo%20viloyati%20rasmlari&ved=2ahUKEwj3_a2e3OGCAxUdPhAIHZlxDVIQMygAegQIARBI",
                                  caption=f"Qashqaqaryo ob-havo haqida ma'lumot {tmax}°С {tmin}°С ",
                                  reply_markup=InlineKeyboardMarkup(menu2()))
    if query.data == "Xorazm":
        query.message.reply_photo(
            photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fi.ytimg.com%2Fvi%2FVM9QuNlGxjA%2Fmaxresdefault.jpg&tbnid=XUy915rmLAdXeM&vet=12ahUKEwiS6ay-3OGCAxVZFBAIHcv-BP0QMygEegQIARBV..i&imgrefurl=https%3A%2F%2Fuzbekistan.travel%2Fuz%2Fr%2Fxorazm-viloyati%2F&docid=FvaueGSmIeH8yM&w=1280&h=720&q=Xoraxm%20viloyati%20rasmlari&ved=2ahUKEwiS6ay-3OGCAxVZFBAIHcv-BP0QMygEegQIARBV",
            caption=f"Xorazm ob-havo haqida ma'lumot {tmax}°С {tmin}°С ",
            reply_markup=InlineKeyboardMarkup(menu1()))

    if query.data == "Toshkent":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fuzbekistan.travel%2Fstorage%2Fapp%2Fuploads%2Fpublic%2F603%2F791%2Fb78%2Fthumb_1590_600_0_0_0_auto.jpg&tbnid=wRYOJj3yv_pMOM&vet=12ahUKEwjqmb7b3OGCAxXJGRAIHUzxAEsQMygJegQIARBP..i&imgrefurl=https%3A%2F%2Fuzbekistan.travel%2Fuz%2Fi%2Ftoshkent%2F&docid=DGtq1lKmwzz2JM&w=600&h=399&q=Toshkent%20viloyati%20rasmlari&ved=2ahUKEwjqmb7b3OGCAxXJGRAIHUzxAEsQMygJegQIARBP",
                                  caption=f"Tashkent ob-havo haqida ma'lumot {tmax}°С {tmin}°С ",
                                  reply_markup=InlineKeyboardMarkup(menu2()))

    if query.data == "Jizzax":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fdaryo.uz%2Fcache%2F2014%2F11%2F6577cfa28640fb57b0ff0e460c506571-660x442.jpg&tbnid=ERZABX0MKxQGCM&vet=12ahUKEwjFjJf33OGCAxVoAhAIHSABCMUQMygGegQIARA5..i&imgrefurl=https%3A%2F%2Fdaryo.uz%2F2014%2F11%2F26%2F2030-yilgacha-jizzax-viloyatidagi-paxtakor-shahri-hududi-kengaytiriladi&docid=oCZF-zolmvBECM&w=660&h=442&q=Jizzax%20viloyati%20rasmlari&ved=2ahUKEwjFjJf33OGCAxVoAhAIHSABCMUQMygGegQIARA5",
                                  caption=f"JIzzax ob-havo haqida ma'lumot {tmax}°С {tmin}°С ",
                                  reply_markup=InlineKeyboardMarkup(menu2()))


    if query.data == "Navoiy":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fyuz.uz%2Fimageproxy%2F1200x%2Fhttps%3A%2F%2Fyuz.uz%2Ffile%2Fnews%2F87a979f0e226b4635e5e5966066ab779.jpg&tbnid=n-LrD4LrUS6mKM&vet=12ahUKEwjAl5md3eGCAxVTQVUIHS0IBk4QMygBegQIARBM..i&imgrefurl=https%3A%2F%2Fyuz.uz%2Fuz%2Fnews%2Fbugun--navoiy-viloyati-tashkil-etilgan-kun&docid=nmqlUCfX4j3_0M&w=1200&h=675&q=Navoiy%20viloyati%20rasmlari&ved=2ahUKEwjAl5md3eGCAxVTQVUIHS0IBk4QMygBegQIARBM",
                                  caption=f"Navoiy ob-havo haqida ma'lumot {tmax}°С {tmin}°С ",
                                  reply_markup=InlineKeyboardMarkup(menu2()))

    if query.data == "Nukus":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fyuz.uz%2Fimageproxy%2F1200x%2Fhttps%3A%2F%2Fyuz.uz%2Ffile%2Fnews%2F8f44a88ef0d6e0f7a14934ebdd20ede2.jpg&tbnid=HEf0_zoaSYCaIM&vet=12ahUKEwilp6TA3eGCAxW2PxAIHZexAAEQMygEegQIARBM..i&imgrefurl=https%3A%2F%2Fyuz.uz%2Fuz%2Fnews%2Fnukus-dala-oquv-maydoni-yangi-qiyofa-kasb-etdi&docid=vFy11kTVAmdOOM&w=1024&h=639&q=Nukus%20viloyati%20rasmlari&ved=2ahUKEwilp6TA3eGCAxW2PxAIHZexAAEQMygEegQIARBM",
                                  caption=f"Nukus ob-havo haqida ma'lumot {tmax}°С {tmin}°С ",
                                  reply_markup=InlineKeyboardMarkup(menu2()))
    # if query.data == "backk":
    #     query.message.reply_text(text=f"Assalomu aleykum {update.message.from_user.first_name} "
    #                                     f"{update.message.from_user.last_name} @ahmadjony ning botiga Xush kelibsiz! Shaxringizni tanlang",
    #                             reply_markup=InlineKeyboardMarkup(menu1()))

def main():
    updater = Updater(token=tokenn)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start", start_hold))
    dispatcher.add_handler(CallbackQueryHandler(menu))
    # dispatcher.add_handler(CallbackQueryHandler())
    updater.start_polling()
    updater.idle()


if __name__ == "__main__":
    main()