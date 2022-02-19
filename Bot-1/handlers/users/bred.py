from aiogram import types

from aiogram.types import CallbackQuery, InputFile
from loader import dp, bot


# Echo bot



@dp.callback_query_handler(text='b1')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id

    await bot.send_photo(chat_id=user_id, photo='AgACAgIAAxkBAAIDPmIBRDztqA-hn8_JvjoppvmskitzAALQuDEb8ZIJSCwpl62kZ5OsAQADAgADeAADIwQ')

    await malumot.message.answer(text="""Adobe Inc, dastlab Adobe Systems Incorporated deb nomlangan , Delaver shtatida tashkil etilgan  va shtab -kvartirasi Kaliforniya shtatining San-Xose shahrida joylashgan Amerika koʻp millatli kompyuter dasturiy taʼminoti kompaniyasi . U tarixan grafika, fotografiya, illyustratsiya, animatsiya, multimedia/video, kinofilmlar va bosma nashrlarni o‘z ichiga olgan keng doiradagi kontentni yaratish va nashr etish uchun dasturiy ta’minotga ixtisoslashgan. Uning flagman mahsulotlari Adobe Photoshop tasvirni tahrirlash dasturini o'z ichiga oladi; Adobe Illustratorvektorga asoslangan tasvirlash dasturi; Adobe Acrobat Reader va Portativ hujjat formati (PDF); va asosan audio-vizual tarkibni yaratish, tahrirlash va nashr etish uchun ko'plab vositalar. Adobe o'z mahsulotlarining Adobe Creative Suite deb nomlangan to'plamini taklif qildi , u Adobe Creative Cloud nomli xizmat sifatida obuna dasturiga (SaaS) aylandi . Kompaniya, shuningdek, raqamli marketing dasturini kengaytirdi va 2021 yilda mijozlar tajribasini boshqarish (CXM) bo'yicha eng yaxshi global liderlardan biri hisoblandi.

Adobe kompaniyasi 1982 yil dekabr oyida  Jon Uornok va Charlz Geshke tomonidan asos solingan, ular Xerox PARC -dan chiqib , PostScript sahifa tavsifi tilini ishlab chiqish va sotish uchun kompaniyaga asos solgan . 1985 yilda Apple Computer o'zining LaserWriter printerlarida foydalanish uchun PostScript-ni litsenziyaladi , bu ish stoli nashriyot inqilobini qo'zg'atishga yordam berdi.  Adobe keyinchalik Macromedia -ni sotib olish orqali animatsiya va multimediya ishlab chiqdi, undan Adobe Flash -ni sotib oldi ; Adobe Premiere bilan video tahrirlash va kompozitsiyalash dasturi, keyinchalik Adobe Premiere Pro nomi bilan tanilgan ; Adobe Muse bilan past kodli veb-ishlab chiqish ; va raqamli marketingni boshqarish uchun dasturiy ta'minot to'plami.""")



@dp.callback_query_handler(text='b2')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id

    await bot.send_photo(chat_id=user_id, photo='AgACAgIAAxkBAAIDQmIBRLU3dbcGywfGBlzN6HjJjIRaAALRuDEb8ZIJSMWel3u0ctbsAQADAgADeQADIwQ')

    await malumot.message.answer(text="""Adidas AG (Adidas deb talaffuz qilinadi) – dunyoga mashhur sport mahsulotlari ishlab chiqaruvchi nemis kompaniyasi. Bosh ofisi Germaniyaning Herzogenaurach shahrida joylashgan. Kompaniyaning bosh direktori – Gerbert Hayner.  Hozirgi vaqtda kompaniya Adidas, Reebok, Rockport, Y-3, RBK & CCM Hockey, shuningdek, Taylor-Made Golf kompaniyalari mahsulotlarini mijozlarga yetkazib berish xizmati bilan shugʻullanadi.
Kompaniyaga Adolf Dassler tomonidan onasining uyida asos solingan; 1924-yilda akasi Rudolf bilan birgalikda Aka-uka Dassler oyoq kiyim fabrikasi nomi bilan nomlashgandi. Dasslerlar koʻplab sport turlari uchun moʻjallangan temir tishli oyoq kiyimlar ishlab chiqish va rivojlantirishga hissa qoʻshishdi. Sport oyoq kiyimlari sifatini oshirish maqsadida Adolf oldingi ogʻir boʻlgan temir tishlar oʻrniga qayta ishlanuvchi rezina va charmdan foydalandi. Dassler AQShlik sprentir Jasse Owensni 1936-yilgi Yozgi Olimpiya oʻyinlarida shaxsan oʻzi tayyorlagan butsilardan foydalanishga koʻndirgan. 1949-yilda ikki aka-uka oʻrtasidagi kelishmovchilik tufayli Adolf Adidasni yaratadi, Rudolf esa Adidasga raqobatchi boʻluvchi Pumani.""")



@dp.callback_query_handler(text='b3')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id

    await bot.send_photo(chat_id=user_id, photo='AgACAgIAAxkBAAIDSGIBRV0GPAIPgUhp69iqwWOjJE3sAALUuDEb8ZIJSG8xpxLidt4hAQADAgADeAADIwQ')

    await malumot.message.answer(text="""Apple Inc. - maishiy elektronika , dasturiy ta'minot va onlayn xizmatlarga ixtisoslashgan Amerika ko'p millatli texnologiya kompaniyasi . Apple daromadi bo‘yicha eng yirik axborot texnologiyalari kompaniyasi (2021-yilda jami 365,8 milliard AQSh dollari ) va 2021-yil yanvar holatiga ko‘ra u dunyodagi eng qimmat kompaniya , birlik sotuvi bo‘yicha shaxsiy kompyuterlar sotuvchisi bo‘yicha to‘rtinchi va mobil telefon ishlab chiqaruvchisi bo‘yicha ikkinchi o‘rinda turadi. . Bu Alphabet bilan bir qatorda Amerikaning katta beshlik axborot texnologiyalari kompaniyalaridan biri (Google ), Amazon , Meta ( Facebook ) va Microsoft .

Apple 1976 yil 1 aprelda Stiv Jobs , Stiv Voznyak va Ronald Ueyn tomonidan Voznyakning Apple I shaxsiy kompyuterini ishlab chiqish va sotish uchun Apple Kompyuter kompaniyasi sifatida tashkil etilgan . U 1977 yilda Jobs va Voznyak tomonidan Apple Computer, Inc. sifatida birlashtirilgan va kompaniyaning keyingi kompyuteri Apple II eng yaxshi sotuvchiga aylandi. Apple 1980 yilda bir zumda moliyaviy muvaffaqiyatga erishdi. Kompaniya innovatsion grafik foydalanuvchi interfeyslariga ega yangi kompyuterlarni ishlab chiqishga kirishdi , shu jumladan original Macintosh , rejissyor tomonidan e'lon qilingan " 1984 " reklamasida e'lon qilindi.Ridli Skott . 1985 yilga kelib, uning mahsulotlarining yuqori narxi va rahbarlar o'rtasidagi hokimiyat uchun kurash muammolarni keltirib chiqardi. Voznyak Apple'dan do'stona tarzda qaytdi, Jobs esa NeXTni yaratish uchun iste'foga chiqdi va o'zi bilan Apple xodimlarini olib ketdi.

1990-yillar davomida shaxsiy kompyuterlar bozori kengayib, rivojlanib borar ekan, Apple kompaniyasi Intel tomonidan boshqariladigan shaxsiy kompyuterlar klonlarida ( shuningdek, " Wintel " nomi bilan ham tanilgan) Microsoft Windows operatsion tizimining arzon narxlardagi duopoliyasiga bozor ulushini yo'qotdi . 1997 yilda, bankrotlikdan bir necha hafta o'tgach, kompaniya Apple'ning muvaffaqiyatsiz operatsion tizimi strategiyasini hal qilish va Jobsni kompaniyaga qaytarish uchun NeXTni sotib oldi. Keyingi o'n yil ichida Jobs bir qator taktikalar, jumladan iMac , iPod , iPhone va iPad -ni joriy qilish orqali Apple-ni daromadlilikka yo'naltirdi.tanqidchilarning olqishiga sazovor bo'ldi, unutilmas reklama kampaniyalarini boshladi, Apple Store chakana savdo tarmog'ini ochdi va kompaniyaning mahsulot portfelini kengaytirish uchun ko'plab kompaniyalarni sotib oldi . Jobs 2011 yilda sog'lig'i sababli iste'foga chiqdi va ikki oydan keyin vafot etdi. U Tim Kuk bosh direktor lavozimini egalladi .""")


@dp.callback_query_handler(text='b4')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id

    await bot.send_photo(chat_id=user_id, photo='AgACAgIAAxkBAAIDTmIBRiILxldSZoJbRrc73_f-OXJcAALVuDEb8ZIJSH8O5NMlQ3MJAQADAgADeQADIwQ')

    await malumot.message.answer(text="""Google LLC Amerikaning koʻp millatli texnologiya kompaniyasi boʻlib, u Internet bilan bogʻliq xizmatlar va mahsulotlarga ixtisoslashgan boʻlib , ular orasida onlayn reklama texnologiyalari , qidiruv tizimi , bulutli hisoblash , dasturiy taʼminot va apparat vositalari kiradi. U Amazon , Apple , Meta ( Facebook ) va Microsoft bilan bir qatorda Amerika axborot texnologiyalari sanoatidagi Katta beshlik kompaniyalaridan biri hisoblanadi .

Google kompaniyasiga 1998-yil 4-sentabrda Larri Peyj va Sergey Brinlar tomonidan PhD darajasida asos solingan . Kaliforniyadagi Stenford universiteti talabalari . Birgalikda ular ommaviy ro'yxatga olingan aktsiyalarining taxminan 14% ga egalik qiladilar va aktsiyadorlarning ovoz berish huquqining 56% ni super ovoz beruvchi aktsiyalar orqali nazorat qiladilar. Kompaniya 2004-yilda birlamchi ommaviy taklif (IPO) orqali ommaga chiqdi. 2015-yilda Google Alphabet Inc.ning 100 foizlik sho‘ba korxonasi sifatida qayta tashkil etildi . Google Alphabetning eng yirik sho'ba korxonasi bo'lib, Alphabetning Internet mulki va manfaatlari uchun xolding kompaniyasi hisoblanadi. Sundar Pichai2015-yil 24-oktabrda Alphabet bosh direktoriga aylangan Larri Peyj o‘rniga Google kompaniyasining bosh direktori etib tayinlandi. 2019-yil 3-dekabrda Pichai Alphabet kompaniyasining bosh direktori bo‘ldi.

2021-yilda asosan Google xodimlaridan iborat Alphabet ishchilari uyushmasi tashkil etildi.

Kompaniyaning tashkil etilganidan buyon tez o'sishi Google-ning asosiy qidiruv tizimi ( Google Qidiruv ) dan tashqari mahsulotlar, xaridlar va hamkorliklarni o'z ichiga oldi . U ish va unumdorlikka moʻljallangan xizmatlarni taklif etadi ( Google Docs , Google Sheets va Google Slides ), elektron pochta ( Gmail ), rejalashtirish va vaqtni boshqarish ( Google Calendar ), bulutli saqlash ( Google Drive ), lahzali xabar almashish va video chat ( Google Duo , Google Chat va Google Meet ), til tarjimasi ( Google Translate ), xaritalash va navigatsiya (Google Xaritalar , Waze , Google Earth va Street View ), podkastlarni joylashtirish ( Google Podcasts ), video almashish ( YouTube ), bloglarni nashr qilish ( Blogger ), eslatma olish ( Google Keep va Jamboard ), rasmlarni tartibga solish va tahrirlash ( Google Photos ) ). Kompaniya Android mobil operatsion tizimini, Google Chrome veb-brauzerini va Chrome OS ( bepul va ochiq manbali Chromium OS asosidagi yengil, xususiy operatsion tizim ) ishlab chiqishda yetakchilik qiladi.operatsion tizim). Google tobora ko'proq apparat vositalariga o'tdi; 2010 yildan 2015 yilgacha u Google Nexus qurilmalarini ishlab chiqarishda yirik elektronika ishlab chiqaruvchilari bilan hamkorlik qildi va 2016 yilda Google Pixel smartfonlar liniyasi, Google Home aqlli dinamiki, Google Wifi mesh simsiz routerini o'z ichiga olgan bir nechta apparat mahsulotlarini chiqardi. Google shuningdek, Internet tashuvchisi ( Google Fiber va Google Fi ) bo'lishni sinab ko'rdi.""")




@dp.callback_query_handler(text='b5')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id

    await bot.send_photo(chat_id=user_id, photo='AgACAgIAAxkBAAIDVGIBSFuE76b_1IDYv_gabU0ZnknFAALauDEb8ZIJSJGEism9avpFAQADAgADeAADIwQ')

    await malumot.message.answer(text="""LG korporatsiyasi (yoki LG Group) (koreyscha: 엘지) 1983-yildan 1995-yilgacha Lucky-Goldstar (koreyscha: Leokki Geumseong; koreyscha: 럭키 금성) Janubiy Koreyaning koʻp millatli konglomerat korporatsiyasi. Koo In-hwoi tomonidan tashkil etilgan va avlodlari tomonidan ketma-ket boshqarib kelingan. 
Janubiy Koreyadagi to'rtinchi yirik chaebol hisoblanadi. Uning bosh qarorgohi Seul shahridagi LG Twin Towers binosida joylashgan. LG elektronika, kimyo va telekommunikatsiya mahsulotlarini ishlab chiqaradi va 80 dan ortiq mamlakatda LG Electronics, Zenith, LG Display, LG Uplus, LG Innotek, LG Chem va LG Energy Solution kabi shoʻba korxonalarini boshqaradi. Xodimlari 186 ming kishini tashkil etadi.""")



@dp.callback_query_handler(text='b6')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id

    await bot.send_photo(chat_id=user_id, photo='AgACAgIAAxkBAAIDXGIBSOCP644QswnBvTlfr_b41bYQAALcuDEb8ZIJSNHCFI1FsM5IAQADAgADeAADIwQ')

    await malumot.message.answer(text="""Yahoo - Amerika veb-xizmatlari provayderi. Bu Sunnyvale markazi bo'lgan, Kaliforniya va adash kompaniyasi Yahoo tomonidan boshqariladigan! Inc.Ghilardi, Apollon Global Management va Verizon Communications tomonidan boshqariladigan investitsiya fondlari tomonidan 90% bo'lgan 10%.

Bu veb-portal beradi, qidiruvi Yahoo qidiruv, va tegishli xizmatlar, mening Yahoo, shu jumladan,!, Yahoo Mail, Yahoo Yangiliklar, Yahoo Moliya, Yahoo Sport va uning reklama platformasi, Yahoo! Vatani.

Yahoo yanvar oyida Jerry Yang va David Filo tomonidan tashkil etilgan 1994 va erta Internet davrning kashshoflar biri edi 1990 yilda. ammo, foydalanish Facebook guruhlar va Google bozor ulushi u yo'qolgan deb kech 2000 yilda kamaydi""")




@dp.callback_query_handler(text='b7')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id

    await bot.send_photo(chat_id=user_id, photo=' AgACAgIAAxkBAAIDYmIBSkttuinp-eoDXmX9MDmgK4_fAALmuDEb8ZIJSFWsYXshEMvLAQADAgADeQADIwQ')

    await malumot.message.answer(text="""Nokia korporatsiyasi - Finlyandiyaning ko'p millatli telekommunikatsiya, axborot texnologiyalariva maishiy elektronika kompaniyasi, 1865-yilda tashkil etilgan. Nokia asosiy qarorgohi Espoobor, Finlyandiya, katta Xelsinki metropolitan sohasida,lekin kompaniyaning haqiqiy ildizlari Pirkanmaa Tampere viloyatida mavjud. yilda 2020, Nokia taxminan ish bilan 92,000 odamlar ustidan bo'ylab 100 mamlakatlar, ko'proq biznes qildim 130 mamlakatlar, va atrofida yillik daromad xabar $ 23 milliard.Nokia ro davlat cheklangan kompaniya Xelsinki Fond birjasi va Nyu-York Fond birjasi. bu bilan o'lchanadi dunyodagi 415th-yirik kompaniya hisoblanadi 2016 Fortune Global ko'ra daromadi 500, yilda 85th joyda avj olgan 2009. evro Stoxx 50 fond bozori indeksining tarkibiy qismihisoblanadi.

Kompaniya so'nggi 150 yil ichida turli sohalarda faoliyat ko'rsatdi. Bu pulpa tegirmon sifatida tashkil etilgan va uzoq rezina va kabellar bilan bog'liqedi, lekin 1990 yildan buyon keng ko'lamli telekommunikatsiya infratuzilmasini, texnologiyalar ishlab chiqish va litsenziyalash qaratilgan. Nokia mobil telefoniya sanoati uchun muhim hissa, GSM rivojlantirishda yordam, 3G, va LTE standartlari. 1998da boshlangan o'n yil mobaynida Nokia dunyodagi eng yirik mobil telefonlar va smartfonlar sotuvchisi edi. Keyinchalik 2000-yilda esa, Nokia yomon boshqaruv qarorlari bir qator jabrlangan, va tez orada mobil telefon bozorida o'z ulushi keskin tomchi ko'rdim. Microsoft va Nokia-ning keyingi bozor kurashlari bilan hamkorlikdan so'ng, Microsoft o'z mobil telefon biznes sotib, uning vorisi sifatida Microsoft Mobile yaratish 2014. sotish so'ng, Nokia uning Bell Labs, shu jumladan, uning bu erda xaritalash bo'linish va Alcatel-Lucent sotib tomonidan belgilangan, uning telekommunikatsiya infratuzilmasi biznes va things texnologiyalari Internetda ko'proq e'tibor boshladi tadqiqot tashkiloti keyinchalik kompaniya virtual haqiqat va raqamli sog'liq bilan tajribao'tkazdi, ikkinchisi esa sotib olish yo'libilan.Nokia brendi HMD Global bilan litsenziyalash tartibi orqali 2016-da mobil va smartfon bozoriga qaytdi. Nokia eng katta mobil telefon sotuvchisi uchun katta patent litsenziya bo'lishi davom etmoqda. sifatida 2018, Nokia dunyodagi uchinchi yirik tarmoq uskunalari ishlab chiqaruvchi hisoblanadi.""")


@dp.callback_query_handler(text='b8')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id

    await bot.send_photo(chat_id=user_id, photo='AgACAgIAAxkBAAIDaGIBS4MTh-t1z-2S42fVzOXfVzKyAAICuTEb8ZIJSDSwv6UGK0sqAQADAgADeQADIwQ')

    await malumot.message.answer(text="""Nike, Inc. (talaffuzi: nayki) - sport mahsulotlari ishlab chiqaruvchi Amerika xalqaro kompaniyasi. Bosh ofisi Beaverton shahri, Oregon shtatida joylashgan.
Kompaniya 1972-yil Oregon Universiteti qisqa masofaga chopish boʻyicha komanda tarkibiga kiruvchi talaba Phil Knight va uning murabbiyi Bill Bowerman tomonidan asos solingan. Kompaniya shiori etib “Just Do It” (shunchaki epla) iborasini tanlashdi. Kompaniya nomi yunon xudosi Nika ismidan olingan.
Direktorlar kengashi raisi – Phil Knight. Prezident – Mark Parker.""")


@dp.callback_query_handler(text='b9')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id

    await bot.send_photo(chat_id=user_id, photo='AgACAgIAAxkBAAIDcmIBTHG8ER9XObga4nIwPOj9oMNIAAIEuTEb8ZIJSKKOzEA5iOwhAQADAgADeQADIwQ')

    await malumot.message.answer(text="""Tesla, Inc. Amerikalik elektr avtomobil va toza energiya kompaniyasi asoslangan Ostin, Texas. Tesla elektr avtomobillarini, uydan grid o'lchovi, quyosh paneli va quyosh tomini saqlash uchun batareya energiyasini saqlashniva tegishli mahsulot va xizmatlarni ishlab chiqaradi va ishlab chiqaradi. Tesla dunyodagi eng qimmat kompaniyalardan biri hisoblanadi va deyarli AQSh$1 trillion bir bozor kapitallashuvi bilan dunyodagi eng qimmat avtomobil qoladi. Kompaniya butun dunyo bo'ylab akkumulyatorli elektr transport vositalari va plagin elektr transport vositalarini sotishgan, batareya 23% qo'lga-elektr (sof elektr) bozor va 16 yilda (plagini duragaylar o'z ichiga oladi) plagini bozorining 2020%. Tesla Energy kompaniyasining filiali orqalikompaniya qo'shma Shtatlardagi fotovoltaik tizimlarning asosiy o'rnatuvchisi hisoblanadi. Tesla Energy 3.99 da o'rnatilgan 2021 gigavatt-soat (Gvh) bilan batareya energiyasini saqlash tizimlarining eng yirik global etkazib beruvchilardan biri hisoblanadi.

Iyul oyida 2003da Martin Eberhard va Mark Tarpenning Tesla Motors tomonidan asos solingan, kompaniyaning nomi ixtirochi va elektr muhandisi Nikola Teslaga bag'ishlangan. Fevral oyida 2004, a orqali $6.5 million investitsiya, X.com asoschilaridan biri Elon Musk kompaniyaning eng yirik aktsiyadori va uning raisi bo'ldi. U beri bosh direktori sifatida xizmat qildi 2008. Muskning so'zlariga ko'ra, Teslaning maqsadi elektr transport vositalari va quyosh energiyasi orqali olingan barqaror transport va energiyaga o'tishni tezlashtirishga yordam berishdir. Tesla birinchi avtomobil modelini ishlab chiqarishni boshladi, Roadster sport avtomobil, yilda 2009. Bu ortidan 2012 yilda Model s sedan, 2015 yilda Model X SUV, 2017 yilda Model 3 sedan va 2020 yilda Model Y krossover. Model 3 butun dunyo bo'ylab eng ko'p sotilgan plagini elektr mashina hamma vaqt, va, iyun oyida 2021, global 1 million dona sotish birinchi elektr mashina bo'ldi. Tesla global savdo 936,222 avtomobil edi 2021, o'tgan yilga nisbatan 87% o'sish,va kumulyativ savdo 2,3 oxirida 2021 million avtomobil tashkil etdi.2021 yilning oktyabr oyida, Tesla bozor kapitallashuvi $1 trillion, AQSh tarixida buning uchun oltinchi kompaniya etdi.""")



@dp.callback_query_handler(text='b10')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id

    await bot.send_photo(chat_id=user_id, photo='AgACAgIAAxkBAAIDeGIBTNGYolmSFfyMDE2gF2uQ03UzAAIFuTEb8ZIJSO0kfXl6RrGYAQADAgADeQADIwQ')

    await malumot.message.answer(text="""Canon — Tokioda (Yaponiya) joylashgan transmilliy mashinasozlik kompaniyasi. U tasvirlarni aniqlash, qayta ishlash va chop etish, tibbiy diagnostika uskunalari uchun optik-mexanik va elektron qurilmalar ishlab chiqarish bilan shug'ullanadi, shuningdek, axborot texnologiyalari va teleko'rsatuvlarda echimlarni ishlab chiqadi. 2016-yil oxirida Canon kompaniyalari guruhi 367 jamlama sho'ba o'z ichiga oladi, butun dunyo bo'ylab 198 ming kishi ishlaydi. O'z markasi ostida mahsulot sotishdan tashqari, Canon HP Inc. uchun lazer printerlarini ishlab chiqaradi., HP LaserJet Printers markasi ostida sotilgan.

Canon xalqaro qizil Xoch va Jahon yovvoyi tabiat jamg'armasi kabi qator xalqaro jamoat tashkilotlarining faoliyatiga homiylik qiladi. Shuningdek, kompaniya jahon Press Photo tanlovi va UEFA Evropa Ligasi kabi madaniy va sport tadbirlarini o'tkazishda ishtiroketadi.""")



@dp.callback_query_handler(text='b11')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id

    await bot.send_photo(chat_id=user_id, photo='AgACAgIAAxkBAAIDfGIBTqNnWumt_MT1isTFhCDJp44vAAILuTEb8ZIJSH95RQrn0zbPAQADAgADeQADIwQ')

    await malumot.message.answer(text="""Bu Samsung Group hisoblanadi Janubiy koreya ko'p millatli ishlab chiqarish conglomerate firma markazi-yilda Samsung Shahar, Seul, Janubiy Koreya. bu ko'p affillangan biznes o'z ichiga oladi, ularning ko'plari Samsung brendi ostida Birlashgan, va eng yirik Janubiy Koreya chaebol bo'ladi (biznes konglomerat). Sifatida 2020, Samsung 8 eng yuqori global tovar qiymatibor.

Samsung kompaniyasi 1938-yilda Li Byung-chul tomonidan savdo kompaniyasi sifatida tashkiletilgan. Keyingi uch o'n yilliklar davomida, guruh oziq-ovqat, shu jumladan, sohalarda ichiga diversifikatsiya, to'qimachilik, sug'urta, qimmatli qog'ozlar, va chakana. Samsung 1960 yillar oxirida elektronika sanoati va o'rta-1970 yilda qurilish va kemasozlik sanoati kirdi; bu sohalarda uning keyingi o'sishini haydovchi edi. 1987-yilda Lining o'limidan so'ng Samsung beshta biznes – guruhga-Samsung Group, Shinsegae Group, CJ Group va Hansol Group hamda Joongang Group guruhlariga ajratildi.

Buyuk Samsung sanoat filiallari o'z ichiga oladi Samsung Electronics (dunyodagi eng yirik axborot texnologiyalari kompaniyasi, maishiy elektronika maker va chipmaker o'lchanadi tomonidan 2017 daromadi), Samsung Og'ir Sanoati (dunyoda 2-yirik shipbuilder o'lchanadi tomonidan 2010 daromadi), va Samsung Muhandislik va Samsung C&T Korporatsiyasi (mos ravishda dunyodagi 13 va 36th yirik qurilish korxonalari).Boshqa mashhur sho'ba Samsung Life Insurance o'z ichiga oladi (dunyodagi 14-eng yirik hayot sug'urta kompaniyasi), Samsung Everland (Everland Resort operatori, eng qadimgi Janubiy Koreyada theme park) va Cheil dunyo bo'ylab (dunyodagi 15 yirik reklama agentligi, bilan o'lchanadi, deb 2012 daromadlar).""")




@dp.callback_query_handler(text='b12')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id

    await bot.send_photo(chat_id=user_id, photo='AgACAgIAAxkBAAIDhWIBT3hzTckKDrEQPcHV2WGwy2kRAAIYuTEb8ZIJSPdFeXlT-YiUAQADAgADeQADIwQ')

    await malumot.message.answer(text="""Toyota Motor Corporation (yaponcha: トヨタ自動車株式会社, Toyota Jidōsha Kabushiki-gaisha) — Yaponiyaning multinatsional korporatsiyasi. 2007-yil birinchi choragi natijalariga koʻra oʻzining subsidiar kompaniyasi Daihatsu bilan birgalikda dunyoning eng katta mashina ishlab chiqaruvchisi deb tan olingan. Toyota Korporatsiyasi savdo daromadi (179 milliard dollar) boʻyicha dunyoning uchinchi katta Avto kompaniyasi va sof daromadi boʻyicha dunyoning sakkizinchi eng katta kompaniyalaridan hisoblanadi.
Jahonda AQShning „General Motors“ va „Ford Motor Company“ kompaniyalaridan keyin 3-oʻrinda turadi. Bosh idorasi Toyota shahrida. Toyota avtomobil kompaniyasi dastlab 1935-yilda toʻqimachilik mashinalari ishlab chiqariladigan zavodning bir boʻlinmasi sifatida sanoatchi Kipchiro Toyoda tomonidan tashkil etilgan. 1937-yildan „Toyota Motors“ kompaniyasi. 1947-yildan Toyota yengil avtomobili ishlab chiqarildi.
1950-yildan yangi konstruksiyadagi avtomobillarning turi va soni yil sayin ortib bordi. Shuningdek, old va orqa oʻkdari orqali harakatlanadigan, har qanday yoʻlda yura oladigan „Land Kryuzer“ modelini ishlab chiqarish yoʻlga qoʻyildi.
1954-yilda Toyota avtomobillari Braziliya va Avstraliyada ishlab chiqarila boshladi, Janubiy Afrika, Tailandda shoʻba kompaniyalar tashkil etildi, boshqa mamlakatlarda Toyota avtomobillarini sotish bilan shugʻullanuvchi vakolatxonalari koʻpaytirildi. 1957-yilda Toyota avtomobillari AQShga eksport qilina boshlandi.
Toyotaning 1962-yilda jami 1 million, 1972-yilda 10 million, 1986-yilda 50 million, 1996-yilda 90 million va 1999-yilda 100 million yengil avtomobili konveyerdan chiqdi. 1966-yilda „Korolla“, 1970-yilda „Kerika“, „Sprinter“, „Karina“, 1978-yilda „Terkel“ modellari yaratildi. 1989-yildan AQShning „General Motors“ kompaniyasi bilan hamkorlik qiladi. 1992-yildan Birlashgan Qirollik, 1996-yildan Rossiyada oʻz korxonalarini ochgan. 1997-yilda Toshkentfa Toyotaning vakolatxonasi ochilib, kompaniya avtomobillari sotila boshladi.
Toyota avtomobillar va koʻplab boshqa mahsulotlar ishlab chiqaradi, oʻz tizimiga juda koʻp kompaniyalarni olgan, eng zamonaviy texnika, texnologiya bilan jihozlangan. Avtomobillarni yigʻish jarayoni 98 % robotlashtirilgan, ishlab chiqarish. jarayonlari kompyuter yordamida boshqariladigan eng yirik korporatsiya hisoblanadi.""")



@dp.callback_query_handler(text='b13')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id

    await bot.send_photo(chat_id=user_id, photo='AgACAgIAAxkBAAIDjWIBUBi56Or09FGXsloHjwc-c0AmAAIeuTEb8ZIJSAeI7ND5vd2RAQADAgADeQADIwQ')

    await malumot.message.answer(text="""Honda Motor Co., Ltd. — yaponiyaning yetakchi mototsikl ishlab chiqaruvchi xalqaro sanoat kompaniyasi, shuningdek, avtomobil ishlab chiqaruvchilari orasida dunyodagi birinchi oʻntalikka kiradi. Asosiy ishlab chiqarish quvvati Yaponiya, AQSh, Hindiston va Braziliyada joylashgan boʻlib, asosiy savdo bozorlari AQSh va janubi-sharqiy Osiyoda joylashgan. Honda 1948-yilda ixtirochi va tadbirkor Soitiro Honda va moliyachi Takeo Fujisava tomonidan tashkil etilgan. Kompaniya shiori — „orzular kuchi“.""")



@dp.callback_query_handler(text='b14')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id

    await bot.send_photo(chat_id=user_id, photo='AgACAgIAAxkBAAIDk2IBUZV-OTVuo5TO96TPTQqjO4mDAAI0uTEb8ZIJSPPPko7PIRpcAQADAgADeQADIwQ')

    await malumot.message.answer(text="""Uolt Disney kompaniyasi, - Burbank (Kaliforniya) shahridagi Uolt Disney Studios majmuasida joylashgan Amerika ko'p millatli ko'ngilochar va media konglomerati.

Disney kompaniyasi dastlab 16 yil 1923 oktyabrda aka-uka Uolt va Roy O. Disney tomonidan "Disney Brothers multfilm studiyasi"sifatida tashkil etilgan; u 1986 yilda Uolt Disney kompaniyasiga nomini rasman o'zgartirishdan oldin "Uolt Disney studiyasi" va "Uolt Disney Productions" nomlari bilan faoliyat ko'rsatgan. Kompaniya jonli kino ishlab chiqarish, televizor va tematik parklarni diversifikatsiya qilishdan oldin Amerika animatsiya sanoatida etakchi sifatida o'zini namoyon qildi.

1980 yildan boshlab, Disney yaratgan va odatda uning flagmani oila yo'naltirilgan brendlar bilan bog'liq ko'proq etuk mazmunini bozor uchun korporativ bo'linmalarini sotib oldi. Kinostudiya bo'limi, Uolt Disney Studios, Uolt Disney Pictures, Uolt Disney Animation Studios, Pixar, Marvel Studios, Lucasfilm, 20-asr studiyalari, 20-asr animatsiyasiva qidiruv yoritgichlari. Disneyning boshqa asosiy ish birliklari orasida televidenie, radioeshittirish, oqim ommaviy axborot vositalari, mavzu parki kurortlari, iste'mol mahsulotlari, nashriyot va xalqaro operatsiyalar bo'linmalari mavjud. Orqali bu turli segmentlarini, Disney egalik qiladi va ABC adabiyot tarmoq; kabel televideniesi tarmoqlarini kabi Disney Channel, ESPN, Freeform, FX, va national geographic; nashriyoti, m'rchandayzing, musiqa va teatr bo'linmalari; to'g'ridan-to'g'ri-uchun-iste'mol oqim xizmatlari kabi Disney+, Yulduz+, ESPN+, Hulu, va Hotstar; va Disney Bog'lar, Tajriba va Mahsulotlar, butun dunyo bo'ylab 14 mavzu qadriyatlari, kurort mehmonxonalar va tomosha bosqichlari bir guruh. 1928-yilda Uolt Disney va Ub Iverks tomonidan yaratilgan karikaturachi Mikki Maus kompaniyaning tumori bo'lib xizmat qiladi.""")



@dp.callback_query_handler(text='b15')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id

    await bot.send_photo(chat_id=user_id, photo='AgACAgIAAxkBAAIDmmIBUka_WV9POiaDUWIrv-mPY5ZwAAJAuTEb8ZIJSLBS0QPWvWKIAQADAgADeQADIwQ')

    await malumot.message.answer(text="""Amazonka – Janubiy Amerikadagi daryo, sersuvligi va havzasi maydonining kattaligi jihatidan dunyoda birinchi oʻrinda, uzunligi jihatidan (6,4 ming km, Ukayali irmogʻi bilan taxminan 7 ming km) Nil daryosidan keyin ikkinchi oʻrinda turadi. A. 7180 ming km² maydondan suv yigʻadi. Asosiy irmogʻi – Maranon. Sharqiy Kordilera togʻ tizmasini kesib oʻtgandan keyin Amazonka payette-kisligiga chiqadi va Ukayali daryosi bilan qoʻshilib A.ni hosil qiladi. A.ga taxminan 500 irmoq quyiladi, koʻpchiligi yirik daryo hisoblanadi. Oʻng tomondan Ukayali, Jurua, Madeyra, Tapajos, Shingu, chapdan – Isa, Yapura, Riu-Negru daryolari qoʻshilib kengaya boradi, oʻrta oqimida 5 km, dengizga quyilish oldida 80–150 km gacha kengayadi. A.ning chuqurligi oʻrta oqimida taxminan 70 m, quyilish joyida 15–45 m. Dare doim sersuv, may – iyunda toshadi. A. yil davomida oʻz havzasidan 1 mlrd. t loyka oqizib keladi. Oʻrtacha suv sarfi 220 ming m³/sek. Aling irmoqlarida yirik viktoriya-re-giya oʻsimligi oʻsadi, suv hayvonlaridan lamantinlar, delfinlar, suv choʻchqalari yashaydi. 2000 baliq turi bor. A. kemalar qatnay oladigan qismining uz. 4300 km. Manaus shahrigacha (okeandan 1690 km) yirik okean kemalari qatnaydi. Asosiy portlari: Ikitos, Manaus, Obidus, Santa-rel, Belen.""")



@dp.callback_query_handler(text='b16')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id

    await bot.send_photo(chat_id=user_id, photo='AgACAgIAAxkBAAIDomIBU8Tua2fIUnFyUiIXjjCobN22AAJwuTEb8ZIJSN64En9rguj4AQADAgADeQADIwQ')

    await malumot.message.answer(text="""Mercedes-Benz  tez-tez ataladi sifatida faqat Mercedes, bir nemis hashamatli avtomobil marque. Mercedes-Benz va Mercedes-Benz AG (2019 yilda tashkil etilgan Mercedes-Benz Group sho'ba korxonasi) Germaniyaning Shtutgart shahrida joylashgan. Mercedes-Benz iste'mol hashamatli transport vositalari va tijorat transport vositalari ishlab chiqaradi.[eslatma 2] uning birinchi Mercedes-Benz-badged vositalari ishlab chiqarilgan edi 1926. 2018 yilda Mercedes-Benz 2.31 million yo'lovchi avtomobil sotgan, dunyodagi premium transport vositalari eng yirik sotuvchi edi.

Kompaniyaning kelib chiqishi Daimler-Motoren-Gesellschaftning 1901 Mercedes va Karl Benzning1886 Benz patentida joylashgan. Tovar shiori "eng yaxshi yoki hech narsa.
Mercedes - Benz odatda sifat va chidamlilik uchun kuchli obro'ga ega. Ularning maqsadi chora-tadbirlar yo'lovchi transport vositalari qarab, JD kuch tadqiqotlar kabi, 1990 yillar oxirida va 2000-yillar boshida bu mezonlar e'tibor inqiroz ko'rsatdi. o'rta-2005 tomonidan, Mercedes vaqtincha dastlabki sifati uchun sanoat o'rtacha qaytdi, birinchi so'ng muammolar chorasi 90 mulkchilik kun, JD kuch ko'ra. In J. D. birinchi choragi uchun quvvat dastlabki sifat o'rganish 2007, Mercedes 25 dan toqqa tomonidan dramatik takomillashtirish ko'rsatdi 5th joy va daromad bir necha mukofotlar uning yangi modellari uchun. Uchun 2008, Mercedes-Benz dastlabki sifat reyting yana bir belgisi bilan yaxshilandi, 4-o'ringa. bu mukofot ustiga, bu, shuningdek, ularning Mercedes markali Sindelfingen uchun Platinum zavodi sifat mukofotini oldi, Germaniya Kuzov Assambleyasi zavodi. JD quvvat ning 2011 AQSh boshlang'ich sifat va avtomobil ishonchliligi tadqiqotlar ikkala build sifati va ishonchliligi o'rtacha yuqorida Mercedes-Benz vositalari o'rinni egalladi.[ J. D ilda.quvvat ning United Kingdom tadqiqot 2011, Mercedes avtomobil o'rtacha yuqorida baholandi. Bundan tashqari, iSeeCars.com Reuters uchun study 2014 Mercedes raqobatchilar chiqib eng kam avtomobil eslamoq darajasi bor, deb topildi.""")







































