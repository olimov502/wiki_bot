from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup

# bolimlar_buttons = InlineKeyboardMarkup(
#     inline_keyboard=[
#         [
#             InlineKeyboardButton(text='Davlatlar🌏', callback_data='n1'),
#             InlineKeyboardButton(text='Mashhur shaxslar👨🏼‍💼', callback_data='n2'),
#             InlineKeyboardButton(text='Dunyo Brendlari💼', callback_data='n3')
#         ],
#         [
#             InlineKeyboardButton(text='Hayvonot olami🦅', callback_data='n4'),
#             InlineKeyboardButton(text='Ulashish📲', switch_inline_query="🤖Eng yaxshi wikipedia bot!"),
#             InlineKeyboardButton(text='Hamkorlik uchun👨🏻‍💻', url='https://t.me/a1mnl')
#         ]
#     ]
#
# )
davlatlar_but = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='AQSH🇺🇸', callback_data='d1'),
            InlineKeyboardButton(text='Germaniya🇩🇪', callback_data='d2'),
            InlineKeyboardButton(text='Fransiya🇫🇷', callback_data='d3'),
            InlineKeyboardButton(text='Buyuk Britaniya', callback_data='d4')
        ],
        [
            InlineKeyboardButton(text='Canada🇨🇦', callback_data='d5'),
            InlineKeyboardButton(text='Belgiya🇧🇪', callback_data='d6'),
            InlineKeyboardButton(text='Rossiya🇷🇺', callback_data='d7'),
            InlineKeyboardButton(text='Italya🇮🇹', callback_data='d8')
        ],
        [
            InlineKeyboardButton(text='Ispaniya🇪🇸', callback_data='d9'),
            InlineKeyboardButton(text='Portugaliya🇵🇹', callback_data='d10'),
            InlineKeyboardButton(text='Braziliya🇧🇷', callback_data='d11'),
            InlineKeyboardButton(text='Argantina🇦🇷', callback_data='d12')
        ]
    ]
)
shaxslar_but = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Steven Jobs', callback_data='s1'),
            InlineKeyboardButton(text='Jeff Bezos', callback_data='s2'),
            InlineKeyboardButton(text='Ilon Mask', callback_data='s3'),
            InlineKeyboardButton(text='Mark Zuckerberg', callback_data='s4')
        ],
        [
            InlineKeyboardButton(text='Bill Gates', callback_data='s5'),
            InlineKeyboardButton(text='Angela Merkel', callback_data='s6'),
            InlineKeyboardButton(text='Teylor Svift', callback_data='s7'),
            InlineKeyboardButton(text='Selena Gomes', callback_data='s8')
        ],
        [
            InlineKeyboardButton(text='Lionel Messi', callback_data='s9'),
            InlineKeyboardButton(text='Tom Hanks', callback_data='s10'),
            InlineKeyboardButton(text='Jennifer Lopez', callback_data='s11'),
            InlineKeyboardButton(text='Lyudvig van Betxoven', callback_data='s12')
        ],
        [
            InlineKeyboardButton(text='Artur Konan Doyl', callback_data='s13'),
            InlineKeyboardButton(text='Jo Bayden', callback_data='s14'),
            InlineKeyboardButton(text='Mark Tven', callback_data='s15'),
            InlineKeyboardButton(text='Agatha Christie', callback_data='s16')
        ]

    ]
)
brendlar_but = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Adobe', callback_data='b1'),
            InlineKeyboardButton(text='Adidas', callback_data='b2'),
            InlineKeyboardButton(text='Apple', callback_data='b3'),
            InlineKeyboardButton(text='Google', callback_data='b4'),
        ],
        [
            InlineKeyboardButton(text='LG', callback_data='b5'),
            InlineKeyboardButton(text='Yahoo', callback_data='b6'),
            InlineKeyboardButton(text='Nokia', callback_data='b7'),
            InlineKeyboardButton(text='Nike', callback_data='b8')
        ],
        [
            InlineKeyboardButton(text='Tesla', callback_data='b9'),
            InlineKeyboardButton(text='Canon', callback_data='b10'),
            InlineKeyboardButton(text='Samsung', callback_data='b11'),
            InlineKeyboardButton(text='Tayota', callback_data='b12')
        ],
        [
            InlineKeyboardButton(text='Honda', callback_data='b13'),
            InlineKeyboardButton(text='Disney', callback_data='b14'),
            InlineKeyboardButton(text='Amazon', callback_data='b15'),
            InlineKeyboardButton(text='Mercedes Benz', callback_data='b16')
        ]
    ]
)
hayvonlar_but = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text="Yo'lbars", callback_data='h1'),
            InlineKeyboardButton(text="Bo'ri", callback_data='h2'),
            InlineKeyboardButton(text='Ayiq', callback_data='h3'),
            InlineKeyboardButton(text='Mushuk', callback_data='h4')
        ],
        [
            InlineKeyboardButton(text='Oq ayiq', callback_data='h5'),
            InlineKeyboardButton(text='Baliq', callback_data='h6'),
            InlineKeyboardButton(text='Burgut', callback_data='h7'),
            InlineKeyboardButton(text='Fillar', callback_data='h8')
        ],
        [
            InlineKeyboardButton(text="Laylak", callback_data='h9'),
            InlineKeyboardButton(text="Morj", callback_data='h10'),
            InlineKeyboardButton(text='Ilonlar', callback_data='h11'),
            InlineKeyboardButton(text='Sichqonlar', callback_data='h12')
        ],
        [
            InlineKeyboardButton(text='Lochin', callback_data='h13'),
            InlineKeyboardButton(text="Ko'k kit", callback_data='h14'),
            InlineKeyboardButton(text='Akulalar', callback_data='h15'),
            InlineKeyboardButton(text="Qarg'alar", callback_data='h16')
        ]
    ]
)
shaxarlar_but=InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='London', callback_data='x1'),
            InlineKeyboardButton(text='Seul', callback_data='x2'),
            InlineKeyboardButton(text='Nyu York', callback_data='x3'),
            InlineKeyboardButton(text='Moskva', callback_data='x4')
        ],
        [
            InlineKeyboardButton(text='Washington', callback_data='x5'),
            InlineKeyboardButton(text='Manchester', callback_data='x6'),
            InlineKeyboardButton(text='Torronto', callback_data='x7'),
            InlineKeyboardButton(text='Istanbul', callback_data='x8')
        ],
        [
            InlineKeyboardButton(text='Tokio', callback_data='x9'),
            InlineKeyboardButton(text='Dubai', callback_data='x10'),
            InlineKeyboardButton(text='Berlin', callback_data='x11'),
            InlineKeyboardButton(text='Rio-de-Janeyro', callback_data='x12')
        ],
        [
            InlineKeyboardButton(text='Parij', callback_data='x13'),
            InlineKeyboardButton(text="Rim", callback_data='x14'),
            InlineKeyboardButton(text='Amsterdam', callback_data='x15'),
            InlineKeyboardButton(text='Anqara', callback_data='x16')
        ]
    ]
)









