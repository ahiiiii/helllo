# from telegram import InlineKeyboardMarkup,InlineKeyboardButton,KeyboardButton,ReplyKeyboardMarkup
# from telegram.ext import CommandHandler,CallbackQueryHandler,Updater,Filters,MessageHandler
# import sqlite3
# t = "6771525180:AAEccYqlupjeEEBhP1g1sFKXAFQCtMpWW-0"
#
# def mintaqakeyboard():
#     return [
#         [KeyboardButton(text=f"Mintaqalar")]
#     ]
#
# def start_handler(update,context):
#
#     update.message.reply_text(text=f"Assalomu alaykum {update.message.from_user.first_name} botimizga xush kelibsiz",
#                               reply_markup=ReplyKeyboardMarkup(mintaqakeyboard(),resize_keyboard=True)
#                               )
#
# def mintaqa(update,context):
#     msg = update.message.reply_text
#     if msg=='Mintaqalar':
#         conn = sqlite3.connect('sample-database.db')
#         c = conn.cursor()
#         c.execute("SELECT region_name FROM regions;")
#         a = c.fetchall()
#         buttons = []
#         for i in a:
#             buttons.append([InlineKeyboardButton(text=f"{i[0]}", callback_data=f"{i[0]}")])
#         update.message.reply_text(text=f"Mintaqalarni tanlang",reply_markup=InlineKeyboardMarkup(buttons))
# def main():
#     updater = Updater(token=t)
#     dispatcher = updater.dispatcher
#     dispatcher.add_handler(CommandHandler("start", start_handler))
#     dispatcher.add_handler(MessageHandler(Filters.text,mintaqa))
#     updater.start_polling()
#     updater.idle()
# if __name__ == "__main__":
#     main()

from telegram import InlineKeyboardMarkup,InlineKeyboardButton,CallbackQuery,KeyboardButton,ReplyKeyboardMarkup,BotCommand
from telegram.ext import CommandHandler,CallbackQueryHandler,Updater,Filters,MessageHandler
import sqlite3
t = "6771525180:AAEccYqlupjeEEBhP1g1sFKXAFQCtMpWW-0"

def mintaqalar():
    return [
        [KeyboardButton(text=f"Mintaqalar")]
    ]
def back():
    return [
        [InlineKeyboardButton(text=f'back',callback_data=f'back1')]
    ]
def back2():
    return [
        [InlineKeyboardButton(text=f'back',callback_data=f'back2')]
    ]
def start_handler(update,context):
    commands = [
        BotCommand(command='start', description='Botni ishga tushirish')
    ]
    context.bot.set_my_commands(commands)
    update.message.reply_text(text=f"Assalomu Alaykum {update.message.from_user.first_name} botimizga hush kelibsz :",
                              reply_markup=ReplyKeyboardMarkup(mintaqalar(),resize_keyboard=True,one_time_keyboard=True))

def mintaqa(update,context):
    msg = update.message.text
    if msg =="Mintaqalar":
        global buttonseuro
        conn = sqlite3.connect("sample-database.db")
        c = conn.cursor()
        c.execute("SELECT region_name FROM regions;")
        a = c.fetchall()
        buttonseuro = []
        for i in a:
            buttonseuro.append([InlineKeyboardButton(text=f"{i[0]}",callback_data=f"{i[0]}")])
        update.message.reply_text(text=f"Mintaqani tanlang",reply_markup=InlineKeyboardMarkup(buttonseuro))
def davlatlar(update,context):
    query = update.callback_query
    data = query.data
    if data == "Europe":
        global buttonseuro1
        conn = sqlite3.connect("sample-database.db")
        c = conn.cursor()
        c.execute("SELECT country_name FROM countries Where region_id=1;")
        a = c.fetchall()
        buttonseuro1 = []
        for i in a:
            buttonseuro1.append([InlineKeyboardButton(text=f"{i[0]}", callback_data=f"{i[0]}")])
        query.message.reply_text(text=f"Davlatnini tanlang", reply_markup=InlineKeyboardMarkup(buttonseuro1))
    if data == "Americas":
        global buttonsameric
        conn = sqlite3.connect("sample-database.db")
        c = conn.cursor()
        c.execute("SELECT country_name FROM countries Where region_id=2;")
        a = c.fetchall()
        buttonsameric = []
        for i in a:
            buttonsameric.append([InlineKeyboardButton(text=f"{i[0]}", callback_data=f"{i[0]}")])
        query.message.reply_text(text=f"Davlatnini tanlang", reply_markup=InlineKeyboardMarkup(buttonsameric))
    if data == "Asia":
        conn = sqlite3.connect("sample-database.db")
        c = conn.cursor()
        c.execute("SELECT country_name FROM countries Where region_id=3;")
        a = c.fetchall()
        buttons = []
        for i in a:
            buttons.append([InlineKeyboardButton(text=f"{i[0]}", callback_data=f"{i[0]}")])
        query.message.reply_text(text=f"Davlatnini tanlang", reply_markup=InlineKeyboardMarkup(buttons))
    if data == "Middle East and Africa":
        conn = sqlite3.connect("sample-database.db")
        c = conn.cursor()
        c.execute("SELECT country_name FROM countries Where region_id=4;")
        a = c.fetchall()
        buttons = []
        for i in a:
            buttons.append([InlineKeyboardButton(text=f"{i[0]}", callback_data=f"{i[0]}")])
        query.message.reply_text(text=f"Davlatnini tanlang", reply_markup=InlineKeyboardMarkup(buttons))
    if query.data == "Belgium":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fcdn.britannica.com%2F22%2F922-050-6D3067E8%2FGuild-houses-Lys-River-Belgium-Ghent.jpg&tbnid=6k1K-wzSEou_7M&vet=12ahUKEwimx6_fzPqCAxWxIRAIHa9RCoUQMygAegQIARBS..i&imgrefurl=https%3A%2F%2Fwww.britannica.com%2Fplace%2FBelgium&docid=Qbto_6_00ldV5M&w=1082&h=800&q=belgium%20photos&ved=2ahUKEwimx6_fzPqCAxWxIRAIHa9RCoUQMygAegQIARBS",
                                  caption=f"Assalamu alaykum Belgium haqida ma'lumorlar :\n Belgiya, Belgiya Qirolligi (flamandcha: Koninkrijk België; fransuzcha: Royaume de Belgique) — G‘arbiy Yevropadagi davlat. Shimoliy dengiz sohilida joylashgan. Maʼmuriy jihatdan 3 regionga, regionlar viloyat (provinsiya)larga, viloyatlar kommunalarga bo‘lingan. Maydoni 30,528 ming km². Aholisi 12828000 kishi (2023). Poytaxti — Bryussel shahri",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "Switzerland":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fxabar.uz%2Fstatic%2Fcrop%2F3%2F6%2F920__95_369943926.jpg&tbnid=ogZxiDseR-GucM&vet=12ahUKEwjhz9vR3PqCAxVSQVUIHXUAAioQMygAegQIARAz..i&imgrefurl=https%3A%2F%2Fwww.xabar.uz%2Fuz%2Fjamiyat%2Fshveycariya-dunyoning-eng-yaxshi-mamlakati-deya-etirof-etildi&docid=Nw6TgXeSe82p0M&w=640&h=463&q=shvetsariya%20rasmlari&ved=2ahUKEwjhz9vR3PqCAxVSQVUIHXUAAioQMygAegQIARAz",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\n Shveysariya (Switzerland, nem. Schweiz, fransuzcha: Suisse, italyancha: Svizzera), Shveysariya Konfederatsiyasi (nemischa: Schweizerische Eidgenossenschaft, fransuzcha: Conferderation Suisse, italyancha: Confederazione Svizzera) – Markaziy Yevropada joylashgan davlat. Maydoni 41 285km². Aholisi 10 mln. kishi (2023). Yuridik jihatdan Poytaxti yoʻq. Poytaxt sifatida Bern shaxri foydalaniladi. Maʼmuriy jihatdan 23 kanton (ulardan 3 tasi yarim kantonlar)ga boʻlinadi. Dunyodagi kambagʻallik darajasi eng past boʻlgan davlat hisoblanad",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "Germany":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F1152163935%2Fru%2F%25D1%2584%25D0%25BE%25D1%2582%25D0%25BE%2F%25D0%25B7%25D0%25B4%25D0%25B0%25D0%25BD%25D0%25B8%25D0%25B5-%25D1%2580%25D0%25B5%25D0%25B9%25D1%2585%25D1%2581%25D1%2582%25D0%25B0%25D0%25B3%25D0%25B0-%25D0%25BC%25D0%25B5%25D1%2581%25D1%2582%25D0%25BE-%25D0%25BD%25D0%25B0%25D0%25BC%25D0%25B5%25D1%2581%25D1%2582%25D0%25BD%25D0%25B8%25D0%25BA-%25D0%25BD%25D0%25B5%25D0%25BC%25D0%25B5%25D1%2586%25D0%25BA%25D0%25BE%25D0%25B3%25D0%25BE-%25D0%25BF%25D0%25B0%25D1%2580%25D0%25BB%25D0%25B0%25D0%25BC%25D0%25B5%25D0%25BD%25D1%2582%25D0%25B0.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3D1fnJCNy6ER9LBLQf6u6T_7VKlXPj_BEBqCCQ7_yS7ME%3D&tbnid=hIdQLPp0ooONXM&vet=12ahUKEwjgut3j4PqCAxUfFxAIHdEeCowQMygAegQIARBW..i&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fru%2F%25D1%2584%25D0%25BE%25D1%2582%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D1%2584%25D0%25B8%25D0%25B8%2F%25D0%25B3%25D0%25B5%25D1%2580%25D0%25BC%25D0%25B0%25D0%25BD%25D0%25B8%25D1%258F&docid=qUE-6_ogRp8qFM&w=612&h=366&q=Germany%20rasmlari&ved=2ahUKEwjgut3j4PqCAxUfFxAIHdEeCowQMygAegQIARBW",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\nGermaniya yoki Olmoniya (nemischa: Deutschland), Germaniya Federativ Respublikasi (nemischa: Bundesrepublik Deutschland) — Markaziy Yevropadagi davlat. Shimoliy Boltiq dengizlari sohilida joylashadi. Maydoni 357 ming km2. Aholisi 83,149,300 kishi (2019-yilga koʻra).[1] Poytaxti — Berlin shahri. Maʼmuriy jihatdan 16 yer (shtat) ga, yerlar okruglarga, okruglar tumanlarga, tumanlar jamoalarga boʻlinadi. ",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "Denmark":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.shutterstock.com%2Fshutterstock%2Fphotos%2F1476195866%2Fdisplay_1500%2Fstock-photo-copenhagen-iconic-view-famous-old-nyhavn-port-in-the-center-of-copenhagen-denmark-during-summer-1476195866.jpg&tbnid=P4do1J8bj6xG5M&vet=12ahUKEwiE__mW4fqCAxV0PhAIHf4VAEUQMygAegQIARBL..i&imgrefurl=https%3A%2F%2Fwww.shutterstock.com%2Fsearch%2Fdenmark&docid=2uIIs3DM_DZfqM&w=1500&h=1101&q=Denmark%20rasmlari&ved=2ahUKEwiE__mW4fqCAxV0PhAIHf4VAEUQMygAegQIARBL",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\nDaniya (Danmark), Daniya qirolligi (Konqeriqet Danmark) — Yevropaning shimoli-gʻarbidagi davlat, Yutlandiya ya. orolning katta qismini va unga yaqin orollar guruhi (Zelandiya, Fyun, Lollann, Falster va boshqa)ni oʻz ichiga oladi. Maydon 43043 km2 (Grenlandiya va Farer orollaridan tashqari); Aholisi 5,59 mln. kishi (2012). Poytaxti — Kopengagen shahri. ",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "France":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F1145422105%2Fphoto%2Feiffel-tower-aerial-view-paris.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3DsFn6FwTJR0TpX3rP_W4VHrbkTB__6l5kr-lkkqdYrtE%3D&tbnid=U5A1kv6FVJnNHM&vet=12ahUKEwj1p4LT4fqCAxUXFBAIHZafAngQMygBegQIARBa..i&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Ffrance&docid=fstFISjaix6ZLM&w=612&h=408&q=France%20rasmlari&ved=2ahUKEwj1p4LT4fqCAxUXFBAIHZafAngQMygBegQIARBa",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\nFransiya (fransuzcha talaffuzi: [fʁɑ̃s] tingla), rasmiy nomi Fransiya Respublikasi (fransuzcha: République française)[1] — Gʻarbiy Yevropadagi davlat. Gʻarbda va shimolda Atlantika okeani hamda La-Mansh boʻgʻozi, janubida Oʻrta dengiz bilan oʻralgan. Maydoni 674687 ming km². Aholisi 68 088 924 million kishi (2023). Poytaxti — Parij shahri ",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "Italy":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F539115110%2Fphoto%2Fcolosseum-in-rome-and-morning-sun-italy.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3D9NtFxHI3P2IBWRY9t0NrfPZPR4iusHmVLbXg2Cjv9Fs%3D&tbnid=pogn_-7i472NKM&vet=12ahUKEwiBy9OT4vqCAxUQJxAIHQrDCOgQMygAegQIARBK..i&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Fitaly&docid=5Zw3MHpWM_maAM&w=612&h=408&q=Italy%20rasmlari&ved=2ahUKEwiBy9OT4vqCAxUQJxAIHQrDCOgQMygAegQIARBK",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\nItaliya (Italia), Italiya Respublikasi (Repubblica Italiana) – Yevropa janubida, Oʻrta dengiz havzasida joylashgan davlat. Apennin yarim orol, Sitsiliya, Sardiniya va boshqa kichik orollarni oʻz ichiga olgan. Maydon 301,2 ming km2. Aholisi 62234878 mln. kishi (2023). Maʼmuriy jihatdan 20 viloyat (regione)ga boʻlinadi. Poytaxti – Rim shahar. ",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "Netherlands":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F937057490%2Fphoto%2Ftraditional-dutch-windmills-and-houses-near-the-canal-in-zaanstad-village-zaanse-schans.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3DKCX_ueIYeZlqPwJB8gHke2Mvd81eEcuSN_w9KjpG2EI%3D&tbnid=gwKCXAHT71_u0M&vet=12ahUKEwj6oKfc4vqCAxUPExAIHd10CeIQMygAegQIARBT..i&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Fnetherlands&docid=s2lLrpWPH4BzyM&w=612&h=407&q=Netherlands%20rasmlari&ved=2ahUKEwj6oKfc4vqCAxUPExAIHd10CeIQMygAegQIARBT",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\nNiderlandlar (niderlandcha: Nederland), Niderlandlar Qirolligi (Koninkrijk der Nederlanden) (norasmiy nomi — Gollandiya) — Gʻarbiy Yevropada, Shimoliy dengiz sohilida joylashgan davlat. Maydoni 41,5 ming km2. Aholisi 18854788 kishi (2023). Poytaxti — Amsterdam shahri. ",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "United Kingdom":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F616242056%2Fru%2F%25D1%2584%25D0%25BE%25D1%2582%25D0%25BE%2F%25D0%25B1%25D1%2580%25D0%25B8%25D1%2582%25D0%25B0%25D0%25BD%25D1%2581%25D0%25BA%25D0%25B8%25D0%25B9-%25D1%2584%25D0%25BB%25D0%25B0%25D0%25B3-%25D0%25B1%25D0%25B8%25D0%25B3-%25D0%25B1%25D0%25B5%25D0%25BD-%25D0%25B8-%25D0%25B7%25D0%25B4%25D0%25B0%25D0%25BD%25D0%25B8%25D0%25B5-%25D0%25BF%25D0%25B0%25D1%2580%25D0%25BB%25D0%25B0%25D0%25BC%25D0%25B5%25D0%25BD%25D1%2582%25D0%25B0-%25D0%25BB%25D0%25BE%25D0%25BD%25D0%25B4%25D0%25BE%25D0%25BD.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3Dk7TG_H_AVM2V0W47lOaxmML79fg2rhaVItAjMIKdlhM%3D&tbnid=Yn66ObkxRe8lmM&vet=12ahUKEwiHuYCK4_qCAxUwMRAIHfBIDaoQMygDegQIARBX..i&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fru%2F%25D1%2584%25D0%25BE%25D1%2582%25D0%25BE%25D0%25B3%25D1%2580%25D0%25B0%25D1%2584%25D0%25B8%25D0%25B8%2Funited-kingdom-of-great-britain&docid=TnRSsLtW7DlKqM&w=612&h=371&q=United%20Kingdom%20rasmlari&ved=2ahUKEwiHuYCK4_qCAxUwMRAIHfBIDaoQMygDegQIARBX",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\nBuyuk Britaniya, Britaniya, (inglizcha: Great Britain) yoki Buyuk Britaniya va Shimoliy Irlandiya Birlashgan Qirolligi (inglizcha: United Kingdom of Great Britain and Northern Ireland) — Shimoli-Gʻarbiy Yevropadagi davlat. Buyuk Britaniya oroli (mamlakat hududining 90 %i shu orolda) va Irlandiya orolining shimoli-sharqiy qismida hamda ularga yondosh mayda orollar (Anglsi, Uayt, Normand, Orkney, Gebrid, Shetlend va boshqalar)da joylashgan. Gʻarbdan Atlantika okeani, sharqdan Shimoliy dengiz oʻrab turadi. ",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "Argentina":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fas2.ftcdn.net%2Fv2%2Fjpg%2F01%2F56%2F64%2F31%2F1000_F_156643170_o9N6f5bhIHvWvlYoLNhYkKw5cUxIEONt.jpg&tbnid=L9KEp5ozZXBVNM&vet=12ahUKEwiH9f2cuP-CAxUjFBAIHZxWC58QMygfegUIARCaAQ..i&imgrefurl=https%3A%2F%2Fwww.europosters.ch%2Fdie-hauptstadt-von-buenos-aires-in-argentinien-f156643170&docid=SyyWYnXOpPENcM&w=1000&h=667&q=argentina%20rasmlar&ved=2ahUKEwiH9f2cuP-CAxUjFBAIHZxWC58QMygfegUIARCaAQ",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\n Argentina Respublikasi (Ispancha: República Argentina) — Janubiy Amerikadagi davlat. Qitʼaning janubi-sharqiy qismini, Olovli Yer o.ning sharqiy qismini va bir qancha orollarni egallaydi. Atlantika okeani sohilida joylashgan. Maʼmuriy jihatdan 22 viloyat (provinsiya), federal (poytaxt) okrugi va Olovli Yer hududiga boʻlinadi. Maydoni 2767 ming km². Aholisi 36,1 mln. 605kishi (1999). Poytaxti Buenos-Ayres shahri.",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "Brazil":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.shutterstock.com%2Fimage-photo%2Faerial-view-rio-corcovado-mountain-600nw-2181332719.jpg&tbnid=3XHQO0tLhNvD2M&vet=12ahUKEwjajIPkuf-CAxUqHRAIHVCfCGMQMygCegQIARBS..i&imgrefurl=https%3A%2F%2Fwww.shutterstock.com%2Fpt%2Fsearch%2Fbrasil&docid=vxPzzUgeXNZZFM&w=600&h=400&q=Brazil%20rasmlar&ved=2ahUKEwjajIPkuf-CAxUqHRAIHVCfCGMQMygCegQIARBS",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\nBraziliya, rasmiy nomi Braziliya Federativ Respublikasi (par. Brasil yoki República Federativa do Brasil) — Janubiy Amerikadagi eng katta va aholisi eng koʻp boʻlgan mamlakat boʻlib, ham aholi soni, ham maydoni jihatidan dunyoda beshinchi oʻrinni egallaydi. Maydoni 8512 ming km2. Aholisi 192,376,496 kishi (2012). U bilan chegaradosh mamlakatlar: Urugvay, Argentina, Paragvay, Boliviya, Peru, Kolumbiya, Venesuela, Guyana, Suriname va Fransuz Giyanasining fransuz qismi. Aniqrogʻi, u Ekvador va Chilidan tashqari, Janubiy Amerikaning har bir davlati bilan chegaradosh. Maʼmuriy jihatdan 26 shtat va federal (poytaxt) okrugga boʻlinadi",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "Canada":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.booktelemark.no%2Fsites%2Fcb_booktelemark%2Ffiles%2Fstyles%2Fslide_large%2Fpublic%2FMS%2520Victoria%2520p%25C3%25A5%2520vei%2520inn%2520mot%2520Ulefoss%2520sluse%25203%2520Foto%2520Janne%2520Lindgren.jpg%3Fh%3D0c1a8d24%26itok%3DkHrsiILM&tbnid=nBtFERvWy9wIAM&vet=12ahUKEwjl652juv-CAxUuLBAIHfMhB8IQMygIegQIARBE..i&imgrefurl=https%3A%2F%2Fwww.booktelemark.no%2Fen&docid=kIMTgoJCEzcTdM&w=1440&h=810&q=canadal%20rasmlar&ved=2ahUKEwjl652juv-CAxUuLBAIHfMhB8IQMygIegQIARBE",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\n Kanada poytaxti — Ottava shahri. BMT va NATO aʼzosi hamda AQSh bilan „Erkin iqtisodiy savdo aylanmasi to‘g‘risida“gi shartnomasi tuzgan.Birlashgan qirollik dominioni hisoblanadi. 1931-yilda suveren huquqi berilgan. Biroq, mustaqillik eʼlon qilinmagan. Mamlakatni Birlashgan qirollik qiroli (yoki qirolichasi) tomonidan tayinlangan General-Gubernator boshqaradi. Aholi soni 40 238 468 mln. kishi (2023-yil) Maydoni:9984840 km2.",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "Mexico":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.gettyimages.com%2Fid%2F638921947%2Fit%2Ffoto%2Fmexico-city-mexico.jpg%3Fs%3D612x612%26w%3Dgi%26k%3D20%26c%3Daeeyyxi6-s47duNYVllKoV3T3R9Zjk1EHe6YCjYn8Eg%3D&tbnid=58uK-5VMWEOhPM&vet=12ahUKEwiz24a-uv-CAxWpLBAIHU0_B7EQMygCegQIARBN..i&imgrefurl=https%3A%2F%2Fwww.gettyimages.it%2Fimmagine%2Fmexico&docid=y1X0P2wMjS_fSM&w=612&h=416&q=Mexico%20rasmlar&ved=2ahUKEwiz24a-uv-CAxWpLBAIHU0_B7EQMygCegQIARBN",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\nMexico AQShning Pennsylvania shtatida joylashgan shahardir. Juniata County okrugi tarkibiga kiradi",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "United States of America":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.unsplash.com%2Fphoto-1508433957232-3107f5fd5995%3Fq%3D80%26w%3D1000%26auto%3Dformat%26fit%3Dcrop%26ixlib%3Drb-4.0.3%26ixid%3DM3wxMjA3fDB8MHxzZWFyY2h8MTZ8fHVuaXRlZCUyMHN0YXRlc3xlbnwwfHwwfHx8MA%253D%253D&tbnid=NUYTmfLC5QYwGM&vet=12ahUKEwiUk9-Ju_-CAxXjJhAIHTRNBgsQMygBegQIARBJ..i&imgrefurl=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Funited-states&docid=EIOCW9kaOrlweM&w=1000&h=655&q=United%20States%20of%20America%20rasmlar&ved=2ahUKEwiUk9-Ju_-CAxXjJhAIHTRNBgsQMygBegQIARBJ",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\nAmerika Qoʻshma Shtatlari (AQSh; inglizcha: United States of America, USA), Qoʻshma Shtatlar (inglizcha: United States) yoki shunchaki Amerika (inglizcha: America) Shimoliy Amerikadagi mamlakatdir. Poytaxti — Vashington shahri, Birlashgan Millatlar Tashkiloti aʼzosi. AQSh sharqdan Atlantika, gʻarbdan Tinch okeani, janubi-sharqdan Meksika qoʻltigʻi bilan oʻralgan. Maʼmuriy jihatdan 50 shtat va bir federal okrugga boʻlinadi. Alyaska va Gavayi shtatlari mamlakat asosiy hududidan tashqarida joylashgan. Puerto-Riko Hamdoʻstligi, Shimoliy Mariana orollari Hamdoʻstligi, Guam, Virginiya orollari va Amerika Samoasi ham AQShga qarashli. Maydoni — 9.8 million km2. Aholisi 332 million kishidan oshiq boʻlib, aholi soni boʻyicha jahonda uchinchi oʻrinda turadi. ",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "Australia":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.unsplash.com%2Fphoto-1523482580672-f109ba8cb9be%3Fq%3D80%26w%3D1000%26auto%3Dformat%26fit%3Dcrop%26ixlib%3Drb-4.0.3%26ixid%3DM3wxMjA3fDB8MHxzZWFyY2h8Mnx8YXVzdHJhbGlhfGVufDB8fDB8fHww&tbnid=isUap4cqEnUEPM&vet=12ahUKEwj9x--3vf-CAxXuLRAIHbkhC2cQMygAegQIARBM..i&imgrefurl=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Faustralia&docid=gHbOS3QK_UrGfM&w=1000&h=472&q=Australia%20rasmlar&ved=2ahUKEwj9x--3vf-CAxXuLRAIHbkhC2cQMygAegQIARBM",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\nAvstraliya Ittifoqi (Commonwealth of Australia) Avstraliya materigini qoplovchi davlat. Maydoni — 7 million 692 ming 024 km². Aholisi — 25,8 million kishi (2021). Poytaxti — Kanberra shahri. Avstraliyani gʻarbda Hind okeani, sharq, janub va shimoldan esa Tinch okeani suvlari yuvib turadi. Hududi kattaligi boʻyicha Avstraliya jahonda 6-oʻrinda turadi. ",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "China":
        query.message.reply_photo(photo=f"https://google.com/imgres?imgurl=https%3A%2F%2Fmedia.gettyimages.com%2Fid%2F825079852%2Fit%2Ffoto%2Fpudong-skyline-from-the-bund-shanghai-china-asia.jpg%3Fs%3D612x612%26w%3Dgi%26k%3D20%26c%3DLBJ8k3Z2_J7kmDpDDP3hWVATxjJXv4pV_-cJrEfCEe8%3D&tbnid=XT2S85kr2fmOHM&vet=12ahUKEwiLn6rbvf-CAxXOPxAIHbeoCacQMygBegQIARBN..i&imgrefurl=https%3A%2F%2Fwww.gettyimages.it%2Fimmagine%2Fmainland-china&docid=Pf218huOgnMQ8M&w=612&h=408&q=China%20rasmlar&ved=2ahUKEwiLn6rbvf-CAxXOPxAIHbeoCacQMygBegQIARBN",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\nXitoy, Xitoy Xalq Respublikasi (xitoycha 中華人民共和國 — 中华人民共和国 — Zhōnghuá Rénmín Gònghéguó), XXR — Markaziy va Sharqiy Osiyoda joylashgan davlat. Dunyoda aholisi eng koʻp va maydoni jihatidan eng yirik davlatlardan biri. Sharqda Tinch okeanning Sariq, Sharqiy Xitoy va Janubiy Xitoy dengizlari bilan oʻralgan. Maydoni 9,6 mln. km². Aholisi 1 mlrd. 394mln. kishi (2003). Poytaxti — Pekin shahri",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "HongKong":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.shutterstock.com%2Fimage-photo%2Fhong-kong-night-view-260nw-1066838393.jpg&tbnid=GvHS5B6KOqPtPM&vet=12ahUKEwjHr-iAvv-CAxXOPxAIHbeoCacQMygBegQIARA1..i&imgrefurl=https%3A%2F%2Fwww.shutterstock.com%2Fsearch%2Fhong-kong&docid=bEYmc2x7-UveBM&w=419&h=280&q=HongKong%20rasmlar&ved=2ahUKEwjHr-iAvv-CAxXOPxAIHbeoCacQMygBegQIARA1",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\nHong kong bayrogʻi, rasman Xitoy Xalq Respublikasining Gonkong maxsus maʼmuriy hududining mintaqaviy bayrogʻidir. Xitoy milliy qizil rangining markazida oq stiliz qilingan besh bargli Hong Kong Bauhinia blakeana gulini tasvirlangan. Uning asl dizayni 1990-yil 4-aprelda Butunxitoy xalq vakillari kongressining uchinchi sessiyasida taqdim etilgan.[1] Joriy dizayn 1996-yil 10-avgustda Hong Kong maxsus maʼmuriy hududi tayyorgarlik qoʻmitasining toʻrtinchi Plenumida tasdiqlangan.",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "India":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fadu.uz%2Frasmlar%2Fyangilik%2F2018%2F3%2Fmain_photo-2018-03-23_14-47-59-m.jpg&tbnid=pzskdq1PtZmamM&vet=12ahUKEwj8nMWbvv-CAxX7KhAIHfOnCJEQMygCegQIARBQ..i&imgrefurl=https%3A%2F%2Fadu.uz%2Fen%2Fnews%2Farticle%2F151&docid=Pq5xfhq7-0qvIM&w=600&h=400&itg=1&q=India%20rasmlar&ved=2ahUKEwj8nMWbvv-CAxX7KhAIHfOnCJEQMygCegQIARBQ",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\nHindiston (rasman: Hindiston Respublikasi (Bhārat Gaṇarājya[1])) – Janubiy Osiyodagi davlat. Hududi shimoldan janubga 3 214 km, gʻarbdan sharqqa 2 933 km choʻzilgan. Shimolida Himolay togʻlari, gʻarbda Arabiston dengizi, sharqda Bengaliya qoʻltigʻi bilan oʻralgan. Hindiston tarkibiga Arabiston dengizidagi Lakkadiv va Amindiv orollari, Bengaliya qoʻltigʻidagi Andaman va Nikobar orollari ham kiradi. Maydoni – 3,3 million km2. Aholisi – 1 428 627 663 kishi (2023). Poytaxti – Nyu-Dehli. Maʼmuriy jihatdan 28 ta shtat va 8 ta ittifoq hududga boʻlinadi.",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "Japan":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.pexels.com%2Fphotos%2F402028%2Fpexels-photo-402028.jpeg&tbnid=vI44r4O9g3aF6M&vet=12ahUKEwi4p_q_vv-CAxXBAxAIHf7MBlUQMygAegQIARBP..i&imgrefurl=https%3A%2F%2Fwww.pexels.com%2Fsearch%2Fjapan%2F&docid=VseHbOY16-zdcM&w=3456&h=2304&q=japan%20rasmlar&ved=2ahUKEwi4p_q_vv-CAxXBAxAIHf7MBlUQMygAegQIARBP",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\nYaponiya (yaponcha 日本 Nippon, Nihon) — Sharqiy Osiyoning Tinch okean sohilidan sharqda , kun chiqish tomondagi orollarda joylashgan davlat. Yaponiya hududida 6,8 mingga yaqin orol boʻlib, shimoli-sharqdan janubi-gʻarbga qariyb 9.13 ming km²ga choʻzilgan; Yaponiyaning eng yirik 4 ta orollari: Xokkaydo, Xonsyu, Sikoku va Kyusyu.",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "Singapore":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F590050726%2Fit%2Ffoto%2Fsingapore-incandescente-di-notte.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3DtqhRRbJcGKYtKvim7GR_X7jqN1jkqTPPoJ8bR1Cd_D8%3D&tbnid=QWuibylRRHGPJM&vet=12ahUKEwjJ45DZvv-CAxWdMRAIHbOzBmMQMygAegQIARBK..i&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fit%2Fimmagine%2Fsingapore&docid=1tgyAkYsSInrfM&w=612&h=408&q=Singapore%20rasmlar&ved=2ahUKEwjJ45DZvv-CAxWdMRAIHbOzBmMQMygAegQIARBK",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\nSingapur (Singapore) Singapur Respublikasi (inglizcha - Republic of Singapore, malaycha Repablic Singapura) — Janubiy Sharqiy Osiyodagi davlat. Singapur oroli va unga tutash mayda orollar hamda Malakka yarim orolning janubiy chekkasida joylashgan. Maydoni-640 km². Aholisi-5.637 million kishi (2022). Poytaxti — Singapur shahri",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "Egypt":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F177047347%2Fphoto%2Fthe-pyramids-of-giza.jpg%3Fs%3D612x612%26w%3D0%26k%3D20%26c%3DsNOn3ruKWcJD1bqi4AVgU7yNt7nChIA30oLfUfsZ4Ro%3D&tbnid=ILOKG7Qy4en-cM&vet=12ahUKEwjel-CHwP-CAxX3JxAIHSvRC_sQMygAegQIARBX..i&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fphotos%2Fegypt&docid=F2yjgHr6WFiXTM&w=612&h=408&q=Egypt%20rasmlar&ved=2ahUKEwjel-CHwP-CAxX3JxAIHSvRC_sQMygAegQIARBX",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\n EgyptAir (Egyptair ) – aviakompaniya, Misrning avia tashuvchisi va Star Alliance a'zosi. Aviakompaniyaning asosiy markazi Qohira xalqaro aeroporti hisoblanadi. Aviakompaniya toʻliq Misr hukumatiga tegishli boʻlib , Yevropa, Afrika, Yaqin va Uzoq Sharq, Amerika Qoʻshma Shtatlari va Kanadadagi 70 dan ortiq aeroportlarga rejali yoʻlovchi va yuk tashish xizmatlarini koʻrsatadi va ichki aviasayohat bozorida faol ishtirok etadi.",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "Israel":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Flookaside.fbsbx.com%2Flookaside%2Fcrawler%2Fmedia%2F%3Fmedia_id%3D100057136275683&tbnid=jxwbHadN2x3pUM&vet=12ahUKEwiQ1LbhwP-CAxX1GxAIHarPA1IQMygEegQIARBZ..i&imgrefurl=https%3A%2F%2Fwww.facebook.com%2FBoqofficialthailand%2F&docid=fAnVjKSQrm6ieM&w=1363&h=1363&q=bo%27q&ved=2ahUKEwiQ1LbhwP-CAxX1GxAIHarPA1IQMygEegQIARBZ",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\n Juda yoqimsz davlat Xristianlar davlati ",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "Kuwait":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fimages.unsplash.com%2Fphoto-1567074994308-df304d5611db%3Fq%3D80%26w%3D1000%26auto%3Dformat%26fit%3Dcrop%26ixlib%3Drb-4.0.3%26ixid%3DM3wxMjA3fDB8MHxzZWFyY2h8Mnx8a3V3YWl0fGVufDB8fDB8fHww&tbnid=X2svgeMKd5bldM&vet=12ahUKEwj50NKPwf-CAxV-DRAIHcePA0sQMygAegQIARBA..i&imgrefurl=https%3A%2F%2Funsplash.com%2Fs%2Fphotos%2Fkuwait&docid=0wjeakQmMNd4kM&w=1000&h=1482&q=Kuwait%20rasmlar&ved=2ahUKEwj50NKPwf-CAxV-DRAIHcePA0sQMygAegQIARBA",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\nKuvayt,[1] Kuvayt Davlati baʼzan Quvayt (Davlat al-Kuvayt) — Arabiston yarimorolida, Fors qoʻltigʻining shimoli-gʻarbiy sohilidagi davlat. Maydoni 17,8 ming km². Aholisi 2,04 mln. kishi (2001). Poytaxti — Al-Kuvayt shahri. Maʼmuriy jihatdan 3 viloyatga boʻlinadi",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "Nigeria":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fc8.alamy.com%2Fcompes%2F2b7272w%2Forgullosamente-nigeria-foto-de-un-joven-africano-que-sostiene-la-bandera-de-su-pais-diciendo-que-estoy-orgulloso-de-ser-nigeriano-republica-federal-de-nigeria-2b7272w.jpg&tbnid=s1HLdihl9Q-kTM&vet=12ahUKEwjb0La6wf-CAxVmFhAIHev1B2UQMygBegQIARBU..i&imgrefurl=https%3A%2F%2Fwww.alamy.es%2Forgullosamente-nigeria-foto-de-un-joven-africano-que-sostiene-la-bandera-de-su-pais-diciendo-que-estoy-orgulloso-de-ser-nigeriano-republica-federal-de-nigeria-image348559425.html&docid=n6DbcIUsr9ZvKM&w=866&h=1390&q=Nigeria%20rasmlar&ved=2ahUKEwjb0La6wf-CAxVmFhAIHev1B2UQMygBegQIARBU",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\nNigeriya (inglizcha: Nigeria), Nigeriya Federativ Respublikasi (inglizcha: Federal Republic of Nigeria) — Gʻarbiy Afrikada Gvineya qoʻltigʻi sohilida joylashgan davlat. Maydoni 923,8 ming km². Aholisi 129,93 mln. kishi (2002). Poytaxti — Abuja shahri Maʼmuriy jihatdan 36 shtat (state) va poytaxt okrugiga boʻlinadi.",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "Zambia":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fmedia.istockphoto.com%2Fid%2F1135788525%2Fid%2Ffoto%2Fpemandangan-udara-di-atas-sungai-zambezi-zambia.jpg%3Fs%3D1024x1024%26w%3Dis%26k%3D20%26c%3DxX20Yz7s9wcZxbZEo2sFfLOugi5ET2ev9pcSNdxJCBw%3D&tbnid=A0OY5VaI9JY4uM&vet=12ahUKEwjPi_7owf-CAxUSFhAIHbpzBDMQMygAegQIARBJ..i&imgrefurl=https%3A%2F%2Fwww.istockphoto.com%2Fid%2Ffoto%2Fpemandangan-udara-di-atas-sungai-zambezi-zambia-gm1135788525-302282130&docid=2BteCtkxKEt2aM&w=1024&h=682&itg=1&q=Zambia%20rasmlar&ved=2ahUKEwjPi_7owf-CAxUSFhAIHbpzBDMQMygAegQIARBJ",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\nZambiya (inglizcha: Zambia [ˈzæmbiə] Zambiya Respublikasi (Republic of Zambia) — Markaziy Afrikadagi davlat. Maydoni 752,614 km2. Aholisi 14,222,233 kishi (2013). Poytaxti — Lusaka shahri. Maʼmuriy jihatdan 9 viloyat (provinsiya)ga boʻlinadi.",
                                  reply_markup=InlineKeyboardMarkup(back()))
    if query.data == "Zimbabwe":
        query.message.reply_photo(photo=f"https://www.google.com/imgres?imgurl=https%3A%2F%2Fwww.shutterstock.com%2Fimage-photo%2Fman-sitting-on-top-rock-260nw-2370557389.jpg&tbnid=MkjkRyPU35ArSM&vet=12ahUKEwjaqLiiwv-CAxVBKRAIHa6sBgkQMygAegQIARBD..i&imgrefurl=https%3A%2F%2Fwww.shutterstock.com%2Fpt%2Fsearch%2Fzimbabwe&docid=yNNO1xWTn_INZM&w=392&h=280&q=Zimbabwe%20rasmlar&ved=2ahUKEwjaqLiiwv-CAxVBKRAIHa6sBgkQMygAegQIARBD",
                                  caption=f"Assalamu alaykum {data} haqida ma'lumorlar :\nZimbabve (Zimbabwe), Zimbabve Respublikasi (Republic of Zimbabwe) — Afrika janubdagi davlat. BMT aʼzosi. Mayd. 390,76 ming km2. Aholisi 11,5 mln. kishi (2001). Poytaxti Harare shahri. Maʼmuriy jihatdan 8 viloyat (province)ra boʻlinadi.",
                                  reply_markup=InlineKeyboardMarkup(back()))


    if data == "back1":
        query.message.reply_text(text=f"Mintaqani tanlang", reply_markup=InlineKeyboardMarkup(buttonseuro))
    # if data == "back2":
    #     query.message.reply_text(text=f"Mintaqani tanlang", reply_markup=InlineKeyboardMarkup(buttonsameric))
def main():
    updater = Updater(token=t)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler("start",start_handler))
    dispatcher.add_handler(MessageHandler(Filters.text,mintaqa))
    dispatcher.add_handler(CallbackQueryHandler(davlatlar))
    updater.start_polling()
    updater.idle()
if __name__ == "__main__":
    main()