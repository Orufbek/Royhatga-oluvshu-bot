import telebot
from telebot import types


token = "6438756547:AAHumlSX9effyXla3cuILV2LUQ1Ix1aSCuo"
admin=6340752378
bot = telebot.TeleBot(token)


button1 = types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
button1 = button1.add(types.KeyboardButton("Universitedlarni tanlash👩‍🏫" ))

button2=types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
button2 = button2.add(types.KeyboardButton("O'zbekiston milliy universiteti"),
                      types.KeyboardButton("Toshkent davlat texnika universiteti"),
                      types.KeyboardButton("Toshkent davlat iqtisodiyot universiteti"),
                      types.KeyboardButton("O'zbekiston davlat jahon tillari universiteti"),
                      types.KeyboardButton("🔙orqag") )


button3=types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
button3 = button3.add(types.KeyboardButton("Telefon raqam",request_contact=True),
                     types.KeyboardButton("🔙orqag") )

button4=types.ReplyKeyboardMarkup(row_width=1,resize_keyboard=True)
button4 = button4.add(types.KeyboardButton("manzilni kiritish",request_location=True),
                     types.KeyboardButton("🔙orqag") )


orqaga=types.ReplyKeyboardMarkup(row_width=2,resize_keyboard=True)
orqaga=orqaga.add(types.KeyboardButton("🔙orqag"))



@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.send_message(message.from_user.id,"Assalomuy alekum bu bot🤖 universitetlarga ro'yhatdan o'tkazadi ",reply_markup=button1)
    bot.register_next_step_handler(message,get_info)
    # print(message.from_user.id)






@bot.message_handler(func=lambda message: True)

def get_info(message):
    info=message.text
    if info=="Universitedlarni tanlash👩‍🏫":
        bot.send_message(message.from_user.id,"Universitetlarni tanlashingiz mumkin👥",reply_markup=button2)
        bot.register_next_step_handler(message,get_cours)
    else:
        bot.send_message(message.from_user.id,"Iltimos faqat pastagi tugmalarni tanlang",reply_markup=button2)

    
    

     


def get_cours(message):
    kurs=message.text
    if kurs=="🔙orqag":
        bot_funk=bot.send_message(message.from_user.id,"Assalomuy alekum bu bot🤖 universitetlarga ro'yhatdan o'tkazadi ",reply_markup=button1)  
        bot.register_next_step_handler(bot_funk,get_name)       
    elif kurs=="O'zbekiston milliy universiteti":
        bot_funk=bot.send_message(message.from_user.id,"O'zbekiston milliy universitetini tanlamoqchi bolsangiz ismingizni qoldiring",reply_markup=orqaga)
        bot.register_next_step_handler(bot_funk,get_name) 
    elif kurs=="Toshkent davlat texnika universiteti":
        bot_funk=bot.send_message(message.from_user.id,"Toshkent davlat texnika universitetini tanlamoqchi bolsangiz ismingizni qoldiring",reply_markup=orqaga)
        bot.register_next_step_handler(bot_funk,get_name)   
    elif kurs=="Toshkent davlat iqtisodiyot universiteti":
        bot_funk=bot.send_message(message.from_user.id,"Toshkent davlat iqtisodiyot universitetini tanlamoqchi bolsangiz ismingizni qoldiring",reply_markup=orqaga)
        bot.register_next_step_handler(bot_funk,get_name) 
    elif kurs=="O'zbekiston davlat jahon tillari universiteti":
        bot_funk=bot.send_message(message.from_user.id,"O'zbekiston davlat jahon tillari universitetini tanlamoqchi bolsangiz ismingizni qoldiring",reply_markup=orqaga) 
        bot.register_next_step_handler(bot_funk,get_name) 

def get_name(meessage):
    name=meessage.text  
    if name=="🔙orqag":
        bot_funk=bot.send_message(meessage.from_user.id,"Universitedlarni tanlashingiz mumkin",reply_markup=button2)  
        bot.register_next_step_handler(bot_funk,get_name) 
    elif name.isalpha():
        bot_funk=bot.send_message(meessage.from_user.id,f"xurmatli {name} yoshingizni kiriting!",reply_markup=orqaga)  
        bot.register_next_step_handler(bot_funk,get_age,name=name)
def get_age(message,name) :
    age = message.text
    if age.isalpha:
        bot_funk=bot.send_message(message.from_user.id,f"xurmatli {name} Telfon raqamingizni kiriting!",reply_markup=button3)
        bot.register_next_step_handler(bot_funk,get_phone,name=name,age=age)




def get_phone(message,age,name):
    if 'contact' in message.content_type:
        phone=message.contact.phone_number
        bot_funk = bot.send_message(message.from_user.id,"Pastdagi tugma orqali manzilingizni qoldiring !!!",reply_markup=button4)
        bot.register_next_step_handler(bot_funk,get_place,age=age,name=name)
    else:
        bot_funk = bot.send_message(message.from_user.id,f"{name} telfon raqamingizni faqat pastdagi tugma orqali qoldiring ",reply_markup=button3)
        bot.register_next_step_handler(bot_funk,get_phone,age=age,name=name,phone=phone)              




def get_place(message,name,age):
    phone = message.text
    if 'location' in message.content_type:
        yangi_zakaz = f"Ismi : {name.title()}\n yoshi : {age}\nTelfon : {phone}\n Manzil : "
        manzil = message.location
        bot.send_message(admin,yangi_zakaz)
        bot.send_location(admin,latitude = manzil.latitude, longitude=manzil.longitude)
        bot.send_message(message.from_user.id,f"Hurmatli {name} sizning ovqatingiz qabul qilindi",reply_markup=button1)
    else:
        bot_funk = bot.send_message(message.from_user.id,"Xato Faqat Pastdagi tugma orqali manzil qoldiring !!!",reply_markup=button4)
        bot.register_next_step_handler(bot_funk,get_place,name=name,age=age) 













bot.infinity_polling()