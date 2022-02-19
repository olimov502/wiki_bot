from aiogram import types

from aiogram.types import CallbackQuery, InputFile
from loader import dp, bot
from keyboards.inline.inline_but import davlatlar_but


# Echo bot
@dp.callback_query_handler(text='d1')
async def bot_echo(malumot:CallbackQuery):
    user_id = malumot.from_user.id
    rasm_manzili = InputFile(path_or_bytesio='photos/file_2.jpg')

    await bot.send_photo(chat_id=user_id, photo=rasm_manzili)

    await malumot.message.answer(text='Amerika Qoʻshma Shtatlari (AQSh; inglizcha: United States of America), '
                                      'Qoʻshma Shtatlar yoki shunchaki Amerika — Shimoliy Amerikadagi mamlakat. '
                                      'Poytaxti — Vashington shahri, BMT aʼzosi. AQSh Sharqdan Atlantika, gʻarbdan '
                                      'Tinch okeani, janubi-sharqdan Meksika qoʻltigʻi bilan oʻralgan. Maʼmuriy jihatdan'
                                      ' 50 shtat va Kolumbiya federal okrugiga boʻlinadi. Alyaska va Gavayi shtatlari mamlakat asosiy '
                                      'hududidan tashqarida joylashgan. Puerto-Riko Hamdoʻstligi, Shimoliy Mariana orollari Hamdoʻstligi, '
                                      'Guam, Virginiya orollari va Sharqiy Samoa ham AQShga qarashli. Maydoni 9 373 000 km², aholisi 333 000 000 kishi (2021).', reply_markup=davlatlar_but)
















@dp.callback_query_handler(text='d2')
async def bot_echo(malumot:CallbackQuery):
    user_id = malumot.from_user.id
    rasm_manzili = InputFile(path_or_bytesio='photos/file_3.jpg')

    await bot.send_photo(chat_id=user_id, photo=rasm_manzili)

    await malumot.message.answer(text='Germaniya (nemischa: Deutschland), Germaniya Federativ Respublikasi (nemischa: Bundesrepublik Deutschland) — Markaziy Yevropadagi davlat. Shimoliy Boltiq dengizlari sohilida joylashadi. Maydoni 357 ming km2. Aholisi 83,149,300 kishi (2019-yilga koʻra). Poytaxti — Berlin shahri. Maʼmuriy jihatdan 16 yer (shtat) ga, yerlar okruglarga, okruglar tumanlarga, tumanlar jamoalarga boʻlinadi.')


@dp.callback_query_handler(text='d3')
async def bot_echo(malumot:CallbackQuery):
    user_id = malumot.from_user.id
    rasm_manzili = InputFile(path_or_bytesio='photos/file_4.jpg')

    await bot.send_photo(chat_id=user_id, photo=rasm_manzili)

    await malumot.message.answer(text='Fransiya (fransuzcha talaffuzi:  [fʁɑ̃s] ), rasmiy nomi Fransiya Respublikasi (fransuzcha: République française) — Gʻarbiy Yevropadagi davlat. Gʻarbda va shimolda Atlantika okeani hamda La-Mansh boʻgʻozi, janubida Oʻrta dengiz bilan oʻralgan. Maydoni 547,03 ming km². Aholisi 67,5 million kishi (2021). Poytaxti — Parij shahri. Maʼmuriy jihatdan 22 region (viloyat), 96 departamentga boʻlingan. Fransiya tarkibida dengiz orti departamentlari (Gvadelupa, Martinika, Gviana, Reyunon), dengiz orti xududlari (Taiti, Yangi Kaledoniya, Fransiya Polineziyasi, Tinch okeandagi Uollis va Futuna orollari va boshqalar), hududiy birliklar (Mayotta va SenPyer va Mikelon) bor.')


@dp.callback_query_handler(text='d4')
async def bot_echo(malumot:CallbackQuery):
    user_id = malumot.from_user.id
    rasm_manzili = InputFile(path_or_bytesio='photos/file_5.jpg')

    await bot.send_photo(chat_id=user_id, photo=rasm_manzili)

    await malumot.message.answer(text='Buyuk Britaniya, Britaniya, (inglizcha: Great Britain) yoki Buyuk Britaniya va Shimoliy Irlandiya Birlashgan Qirolligi (inglizcha: United Kingdom of Great Britain and Northern Ireland) — Shimoli-Gʻarbiy Yevropadagi davlat. Buyuk Britaniya oroli (mamlakat hududining 90 %i shu orolda) va Irlandiya orolining shimoli-sharqiy qismida hamda ularga yondosh mayda orollar (Anglsi, Uayt, Normand, Orkney, Gebrid, Shetlend va boshqalar)da joylashgan. Gʻarbdan Atlantika okeani, sharqdan Shimoliy dengiz oʻrab turadi. Buyuk Britaniya mamlakat asosiy qismining nomi bilan koʻpincha Angliya deb ataladi. Maydoni 244,1 ming km2. Aholisi 67.081 million kishi (2020-yil). Poytaxti — London shahri. Tarixan tarkib topgan va milliy jihatdan har xil boʻlgan 4 maʼmuriy siyosiy qism (Angliya, Uels, Shotlandiya va unga yondosh orollar, Shimoliy Irlandiya) dan iborat. Men va Normand orollari mustaqil maʼmuriy hudud hisoblanadi.')


@dp.callback_query_handler(text='d5')
async def bot_echo(malumot:CallbackQuery):
    user_id = malumot.from_user.id
    rasm_manzili = InputFile(path_or_bytesio='photos/file_6.jpg')

    await bot.send_photo(chat_id=user_id, photo=rasm_manzili)

    await malumot.message.answer(text='Kanada poytaxti — Ottava shahri. BMT va NATO aʼzosi hamda AQSh bilan „Erkin iqtisodiy savdo aylanmasi toʻgʻrisida“gi shartnomasi tuzgan. Birlashgan qirollik dominioni. 1931-yilda suveren huquqi berilgan. Biroq, mustaqillik eʼlon qilinmagan. Mamlakatni Birlashgan qirollik qiroli (yoki qirolichasi) tomonidan tayinlangan General-Gubernator boshqaradi. Aholi soni 38,3 mln. kishi (2021-yil)')


@dp.callback_query_handler(text='d6')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id
    rasm_manzili = InputFile(path_or_bytesio='photos/file_7.jpg')

    await bot.send_photo(chat_id=user_id, photo=rasm_manzili)

    await malumot.message.answer(text='Belgiya, Belgiya Qirolligi (flamandcha: Koninkrijk België; frans.: Royaume de Belgique) — Gʻarbiy Yevropadagi davlat. Shimoliy dengiz sohilida joylashgan. Maʼmuriy jihatdan 3 regionga, regionlar viloyat (provinsiya)larga, viloyatlar kommunalarga boʻlingan. Maydoni 30,528 mingkm². Aholisi 10 mln. 113 ming kishi (1996). Poytaxti — Bryussel shahri')


@dp.callback_query_handler(text='d7')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id
    rasm_manzili = InputFile(path_or_bytesio='photos/file_8.jpg')

    await bot.send_photo(chat_id=user_id, photo=rasm_manzili)

    await malumot.message.answer(text='Rossiya (ruscha: Россия), Rossiya Federatsiyasi (ruscha: Российская Федерация) — Yevropaning sharqida, Osiyoning shimolida joylashgan mamlakat. Maydoni jihatidan dunyoda eng katta mamlakat. Quruqlikdagi chegarasi 22125,3 km, dengiz chegarasi 38807,5 km. Rossiya hududi 3 okean havzasiga qarashli 12 dengiz, jumladan, Boltiq, Qora va Azov (Atlantika okeani), Barens, Oq, Kara, Laptevlar, Sharqiy Sibir va Chukotka (Shim. Muz okeani), Bering, Oxota, Yapon dengizlari (Tinch okean), shuningdek, hech bir okeanga tutashmagan Kaspiy dengizi bilan oʻralgan. Maydoni 17,1 mln. km². Aholisi 145,3 mln. kishi (2002). Poytaxti – Moskva shahri. Maʼmuriy jihatdan 89 subʼyekt: 21 respublika [Adigeya, Boshqirdiston, Buryatiya, Dogʻiston, Ingushiya, Kabarda-Balkariya, Kareliya, Komi, Mariy El, Mordoviya, Oltoy, Saxa (Yakutiya), Tatariston, Tuva, Udmurtiya, Haqasiya, Checheniston, Chuvashiya, Shimoliy Osetiya, Qalmoq, Qorachoy Cherkasiya, 6 oʻlka (Krasnodar, Krasnoyarsk, Oltoy, Primorye, Stavropol, Xabarovsk), 49 viloyat (Amur, Arxangelsk, Astraxon, Belgorod, Bryansk, Vladimir, Volgograd, Vologda, Voronej, Ivanovo, Irkutsk, Kaliningrad, Kaluga, Kamchatka, Kemerovo, Kirov, Kostroma, Kurgan, Kursk, Leningrad, Lipetsk, Magadan, Moskva, Murmansk, Nijniy Novgorod, Novgorod, Novosibirsk, Omsk, Orenburg, Oryol, Penza, Perm, Pskov, Rostov, Ryazan, Samara, Saratov, Saxalin, Sverdlovsk, Smolensk, Tambov, Tver, Tomsk, Tula, Tyumen, Ulyanovsk, Chelyabinsk, Chita, Yaroslavl), 2 federal shahar (Moskva, Sankt-Peterburg), 1 muxtor viloyat (Yahudiylar), 10 muxtor okrug [Aga Buryatlari, KomiPermyaklar, Koryaklar, Nenetslar, Taymir (Dolgan Nenets), Ust Ordinskiy Buryatlari, XantiMansi, Chukotka, Evenklar, YamalNenets]ga boʻlinadi. Rossiyada 1091 shahar, 1922 shaharcha bor. 2000-yil Markaziy, Shimoliy-Gʻarbiy, Janubiy Volga boʻyi, Ural, Sibir, Uzoq Sharq, federal okruglari tashkil etildi.')


@dp.callback_query_handler(text='d8')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id
    rasm_manzili = InputFile(path_or_bytesio='photos/file_9.jpg')

    await bot.send_photo(chat_id=user_id, photo=rasm_manzili)

    await malumot.message.answer(text='Italiya (Italia), Italiya Respublikasi (Repubblica Italiana) – Yevropa janubida, Oʻrta dengiz havzasida joylashgan davlat. Apennin yarim orol, Sitsiliya, Sardiniya va boshqa kichik orollarni oʻz ichiga olgan. Maydon 301,2 ming km2. Aholisi 60,92 mln. kishi (2012). Maʼmuriy jixatdan 20 viloyat (regione)ra boʻlinadi. Poytaxti – Rim shahar.')


@dp.callback_query_handler(text='d9')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id
    rasm_manzili = InputFile(path_or_bytesio='photos/file_10.jpg')

    await bot.send_photo(chat_id=user_id, photo=rasm_manzili)

    await malumot.message.answer(text='Ispaniya (España), Ispaniya Qirolligi (Reino de España) — Yevropaning janubi-gʻarbida, Pireney yarim orolda joylashgan davlat. Oʻrta dengizdagi Balear (shu jumladan Pitius), Atlantika okeanidagi Kanar orollari, Afrikaning shimoliy qirgʻogʻidagi Seuta va Melilya shaharlari va unga yondosh Veles-de-la-Gomera, Alusemas, Chafarinas orollari ham Ispaniyaga qaraydi. Maydon 504,75 ming km2. Aholisi 47,27 mln. kishi (2012). Maʼmuriy jihatdan oʻz hukumati va parlamentiga ega boʻlgan 17 muxtor regionga, ular, oʻz navbatida, 50 viloyat (provincia)ra boʻlinadi. Poytaxti — Madrid sh.')


@dp.callback_query_handler(text='d10')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id
    rasm_manzili = InputFile(path_or_bytesio='photos/file_11.jpg')

    await bot.send_photo(chat_id=user_id, photo=rasm_manzili)

    await malumot.message.answer(text='Portugaliya (Portugal), Portugaliya Respublikasi (República Portuguesa) — Yevropaning janubiy -gʻarbida, Pirenei yarim orolda joylashgan davlat. Atlantika okeanidagi Azor orollari va Madeyra arxipelagini oʻz ichiga oladi. Maydoni 92,3 ming km². Aholisi 10,53 mln. kishi (2012). Poytaxti — Lissabon shahri Maʼmuriy jihatdan 2 muxtor viloyat, 22 okrug (distrito)ra boʻlingan, shundan 18 tasi materikda joylashgan boʻlib, 11 tarixiy viloyatga birlashgan.')


@dp.callback_query_handler(text='d11')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id
    rasm_manzili = InputFile(path_or_bytesio='photos/file_12.jpg')

    await bot.send_photo(chat_id=user_id, photo=rasm_manzili)

    await malumot.message.answer(text='Braziliya, rasmiy nomi Braziliya Federativ Respublikasi (par. Brasil yoki República Federativa do Brasil) — Janubiy Amerikadagi eng katta va aholisi eng koʻp boʻlgan mamlakat boʻlib, ham aholi soni, ham maydoni jihatidan dunyoda beshinchi oʻrinni egallaydi. Maydoni 8512 ming km2. Aholisi 192,376,496 kishi (2012). U Janubiy Amerika markazidan to Atlantika okeaniga qadar yoyilgan hududni egallab Amerikalarning „eng sharqiy“ mamlakatidir. U bilan chegaradosh mamlakatlar: Urugvay, Argentina, Paragvay, Boliviya, Peru, Kolumbiya, Venesuela, Guyana, Suriname va Fransuz Giyanasining fransuz qismi. Aniqrogʻi, u Ekvador va Chilidan tashqari, Janubiy Amerikaning har bir davlati bilan chegaradosh. Nomi, dastlabki kolonistlar tomonidan juda qadrlangan, Braziliya daraxtidan (pau-brasil) kelib chiqqan. Hududida ham ekin maydonlari, ham tropik oʻrmonzorlar juda katta joyni egallaydi. Tabiiy resurslar va katta miqdordagi ishchi kuchiga boy boʻlgan Braziliya, Janubiy Amerika iqtisodiyotining yetakchisidir. Dastlab Portugaliyaning sobiq koloniyasi boʻlganidan, uning davlat tili Portugal tilidir. Poytaxti – Brazilia shahri. BMT aʼzosi. Maʼmuriy jihatdan 26 shtat va federal (poytaxt) okrugga boʻlinadi')



@dp.callback_query_handler(text='d12')
async def bot_echo(malumot: CallbackQuery):
    user_id = malumot.from_user.id
    rasm_manzili = InputFile(path_or_bytesio='photos/file_13.jpg')

    await bot.send_photo(chat_id=user_id, photo=rasm_manzili)

    await malumot.message.answer(text='Argentina Respublikasi (Ispancha: República Argentina) – Janubiy Amerikadagi davlat. Qit’aning janubi-sharqiy qismini, Olovli Yer o.ning sharqiy qismini va bir qancha orollarni egallaydi. Atlantika okeani sohilida joylashgan. Ma’muriy jihatdan 22 viloyat (provinsiya), federal (poytaxt) okrugi va Olovli Yer hududiga boʻlinadi. Maydoni 2767 ming km². Aholisi 36,1 mln. 605kishi (1999). Poytaxti Buenos-Ayres shahri.')






